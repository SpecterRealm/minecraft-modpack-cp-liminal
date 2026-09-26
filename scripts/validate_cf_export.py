#!/usr/bin/env python3
"""
Validate a packwiz CurseForge export zip against mods/*.pw.toml.

Compares manifest.json (CurseForge project/file IDs) and overrides/mods/*.jar
to the pack index so release artifacts match what maintainers pin in git.

Usage:
  python3 scripts/validate_cf_export.py --zip dist/Colony-Protocol-Verdant-0.2.0-curseforge.zip
  python3 scripts/validate_cf_export.py --export
  make validate-export   # uses dist/*-curseforge.zip from pack.toml version
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[no-redef]


DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class PackMod:
    slug: str
    name: str
    filename: str
    source: str  # "curseforge" | "override"
    project_id: int | None = None
    file_id: int | None = None


@dataclass(frozen=True)
class ManifestEntry:
    project_id: int
    file_id: int


def load_pack_mods(mods_dir: Path) -> list[PackMod]:
    mods: list[PackMod] = []
    for path in sorted(mods_dir.glob("*.pw.toml")):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        slug = path.stem.replace(".pw", "")
        name = str(data.get("name", slug))
        filename = str(data["filename"])
        update = data.get("update") or {}
        cf = update.get("curseforge")
        if cf:
            mods.append(
                PackMod(
                    slug=slug,
                    name=name,
                    filename=filename,
                    source="curseforge",
                    project_id=int(cf["project-id"]),
                    file_id=int(cf["file-id"]),
                )
            )
        else:
            mods.append(
                PackMod(
                    slug=slug,
                    name=name,
                    filename=filename,
                    source="override",
                )
            )
    return mods


def load_zip_export(zip_path: Path) -> tuple[list[ManifestEntry], set[str], list[str]]:
    with zipfile.ZipFile(zip_path) as zf:
        all_names = zf.namelist()
        try:
            manifest_raw = zf.read("manifest.json")
        except KeyError as exc:
            raise SystemExit(f"{zip_path}: missing manifest.json") from exc
        manifest = json.loads(manifest_raw)
        files = manifest.get("files") or []
        entries: list[ManifestEntry] = []
        for item in files:
            entries.append(
                ManifestEntry(
                    project_id=int(item["projectID"]),
                    file_id=int(item["fileID"]),
                )
            )
        override_jars: set[str] = set()
        prefix = "overrides/mods/"
        for name in zf.namelist():
            if name.startswith(prefix) and name.endswith(".jar"):
                override_jars.add(Path(name).name)
    return entries, override_jars, all_names


def validate_export_layout(all_names: list[str]) -> list[str]:
    """CurseForge zip layout checks beyond mod manifest parity."""
    errors: list[str] = []
    nested = [n for n in all_names if "overrides/overrides/" in n]
    if nested:
        errors.append(
            "bad zip layout: paths under overrides/overrides/ (index used "
            f"repo overrides/ — use config/ and options.txt only; {len(nested)} file(s))"
        )
    tmp_paths = [n for n in all_names if "/.tmp/" in n or n.startswith("overrides/.tmp/")]
    if tmp_paths:
        errors.append(
            f"dev scratch in export: {len(tmp_paths)} path(s) under .tmp/ — "
            "add .tmp/ to .packwizignore and packwiz refresh"
        )
    config_paths = [n for n in all_names if n.startswith("overrides/config/") and not n.endswith("/")]
    if len(config_paths) < 80:
        errors.append(
            f"thin config export: only {len(config_paths)} file(s) under overrides/config/ "
            "(ensure config/ is complete — make config-pull after playtest, then make config-ship-full; see docs/config-workflow.md)"
        )
    if "overrides/config/fml.toml" not in all_names:
        errors.append(
            "missing overrides/config/fml.toml (macOS/CurseForge setup may hang — "
            "run make config-ship-full to seed fml.toml from pack-bootstrap/)"
        )
    return errors


def run_export(repo_root: Path, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"→ Running packwiz curseforge export → {out_path}")
    subprocess.run(
        ["packwiz", "curseforge", "export", "-o", str(out_path)],
        cwd=repo_root,
        check=True,
    )


def validate(zip_path: Path, pack_mods: list[PackMod]) -> int:
    manifest, override_jars, all_names = load_zip_export(zip_path)

    cf_mods = [m for m in pack_mods if m.source == "curseforge"]
    override_mods = [m for m in pack_mods if m.source == "override"]

    pack_by_project = {m.project_id: m for m in cf_mods}
    pack_cf_pairs = {(m.project_id, m.file_id) for m in cf_mods}
    manifest_by_project = {e.project_id: e for e in manifest}
    manifest_pairs = {(e.project_id, e.file_id) for e in manifest}

    errors: list[str] = list(validate_export_layout(all_names))

    # Manifest entries with no packwiz pin (removed mod still in export)
    for entry in manifest:
        mod = pack_by_project.get(entry.project_id)
        if mod is None:
            errors.append(
                "manifest orphan: CurseForge project "
                f"{entry.project_id} file {entry.file_id} is in the zip "
                "but not in mods/*.pw.toml"
            )
            continue
        if entry.file_id != mod.file_id:
            errors.append(
                f"manifest stale file: {mod.name} ({mod.slug}.pw.toml) pins "
                f"file {mod.file_id}, export has {entry.file_id} "
                f"(project {entry.project_id})"
            )

    # Packwiz CF mods missing from manifest
    for mod in cf_mods:
        entry = manifest_by_project.get(mod.project_id)
        if entry is None:
            errors.append(
                f"manifest missing: {mod.name} ({mod.slug}.pw.toml) "
                f"project {mod.project_id} file {mod.file_id} not in manifest.json"
            )

    # Duplicate project IDs in manifest (unexpected)
    if len(manifest_by_project) != len(manifest):
        errors.append(
            f"manifest duplicate project IDs: {len(manifest)} entries, "
            f"{len(manifest_by_project)} unique projects"
        )

    expected_override_names = {m.filename for m in override_mods}
    extra_jars = override_jars - expected_override_names
    missing_jars = expected_override_names - override_jars

    for jar in sorted(extra_jars):
        errors.append(
            f"override extra: overrides/mods/{jar} is in the zip "
            "but no mods/*.pw.toml uses that filename"
        )
    for mod in sorted(override_mods, key=lambda m: m.filename):
        if mod.filename in missing_jars:
            errors.append(
                f"override missing: {mod.name} ({mod.slug}.pw.toml) expects "
                f"overrides/mods/{mod.filename} in the zip"
            )

    # Summary
    print(f"Zip: {zip_path}")
    print(
        f"Pack: {len(pack_mods)} mods "
        f"({len(cf_mods)} CurseForge manifest, {len(override_mods)} bundled overrides)"
    )
    print(
        f"Export: {len(manifest)} manifest entries, "
        f"{len(override_jars)} override JAR(s)"
    )

    if not errors:
        print("✓ Export matches mods/*.pw.toml")
        return 0

    print("\n✗ Export validation failed:\n")
    for msg in errors:
        print(f"  • {msg}")

    only_in_manifest = manifest_pairs - pack_cf_pairs
    only_in_pack = pack_cf_pairs - manifest_pairs
    if only_in_manifest or only_in_pack:
        print("\nCurseForge (projectID, fileID) diff:")
        for pair in sorted(only_in_manifest):
            print(f"  + in zip only: {pair}")
        for pair in sorted(only_in_pack):
            print(f"  - in packwiz only: {pair}")

    if extra_jars or missing_jars:
        print("\noverrides/mods/ diff:")
        for jar in sorted(extra_jars):
            print(f"  + in zip only: {jar}")
        for jar in sorted(missing_jars):
            print(f"  - expected from packwiz: {jar}")

    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate CurseForge export zip vs mods/*.pw.toml",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--zip",
        type=Path,
        help="Path to an existing CurseForge export zip",
    )
    group.add_argument(
        "--export",
        action="store_true",
        help="Run packwiz curseforge export to a temp zip, then validate",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help="Pack repository root (default: parent of scripts/)",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    mods_dir = repo_root / "mods"

    if args.export:
        with tempfile.TemporaryDirectory(prefix="cf-export-validate-") as tmp:
            zip_path = Path(tmp) / "export.zip"
            run_export(repo_root, zip_path)
            pack_mods = load_pack_mods(mods_dir)
            return validate(zip_path, pack_mods)

    zip_path = args.zip.resolve()
    if not zip_path.is_file():
        raise SystemExit(f"Zip not found: {zip_path}")

    pack_mods = load_pack_mods(mods_dir)
    return validate(zip_path, pack_mods)


if __name__ == "__main__":
    sys.exit(main())
