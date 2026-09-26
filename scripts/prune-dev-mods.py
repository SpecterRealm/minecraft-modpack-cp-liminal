#!/usr/bin/env python3
"""Remove mod JARs in the Prism dev instance that are not listed in mods/*.pw.toml.

packwiz-installer downloads and updates mods but does not delete superseded JARs
(e.g. after pinning Sodium 0.6.13, an old 0.8.12-alpha jar can remain and crash Iris).

Used by: make dev (before launch). Set DRY_RUN=1 to list removals without deleting.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODS_DIR = REPO_ROOT / "mods"
FILENAME_RE = re.compile(r'^filename\s*=\s*"(.+)"\s*$', re.M)

PRISM_DATA = Path(
    os.environ.get(
        "PRISM_DATA",
        Path.home() / "Library/Application Support/PrismLauncher",
    )
)
PRISM_INSTANCE = os.environ.get("PRISM_INSTANCE", "CP-Liminal-Dev")
DEV_MC_DIR = Path(os.environ.get("DEV_MC_DIR", PRISM_DATA / "instances" / PRISM_INSTANCE / "minecraft"))
INSTANCE_MODS = DEV_MC_DIR / "mods"


def expected_filenames() -> set[str]:
    names: set[str] = set()
    for pw in sorted(MODS_DIR.glob("*.pw.toml")):
        text = pw.read_text(encoding="utf-8")
        m = FILENAME_RE.search(text)
        if not m:
            print(f"⚠️  no filename in {pw.name}", file=sys.stderr)
            continue
        name = m.group(1)
        if name in names:
            print(f"⚠️  duplicate filename {name!r} ({pw.name})", file=sys.stderr)
        names.add(name)
    return names


def main() -> int:
    dry_run = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")
    if not INSTANCE_MODS.is_dir():
        print(f"✗ mods folder not found: {INSTANCE_MODS}", file=sys.stderr)
        return 1

    expected = expected_filenames()
    if not expected:
        print("✗ no filenames found in mods/*.pw.toml", file=sys.stderr)
        return 1

    stale: list[Path] = []
    for jar in sorted(INSTANCE_MODS.glob("*.jar")):
        if jar.name not in expected:
            stale.append(jar)

    if not stale:
        print(f"✓ {INSTANCE_MODS.name}: no stale mod JARs ({len(expected)} expected)")
        return 0

    print(f"→ {len(stale)} stale mod JAR(s) in {INSTANCE_MODS}:")
    for p in stale:
        print(f"   {p.name}")
    if dry_run:
        print("  (DRY_RUN — not deleting)")
        return 0

    for p in stale:
        p.unlink()
    print(f"✓ removed {len(stale)} stale JAR(s); {len(expected)} pack mods expected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
