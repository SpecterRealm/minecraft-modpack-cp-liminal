#!/usr/bin/env python3
"""Remove known-bad orphan files from the Prism instance that packwiz-installer leaves behind.

packwiz-installer downloads and updates pack files but does **not** delete paths
removed from the pack (or never indexed). A common failure mode: uppercase
README.md under kubejs/data/ (Minecraft datapack paths must be lowercase).

Used by: make prune-instance-orphans (optional after pack removals / before smoke).
Set DRY_RUN=1 to list without deleting.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

PRISM_DATA = Path(
    os.environ.get(
        "PRISM_DATA",
        Path.home() / "Library/Application Support/PrismLauncher",
    )
)
PRISM_INSTANCE = os.environ.get("PRISM_INSTANCE", "CP-Liminal-Dev")
DEV_MC_DIR = Path(
    os.environ.get("DEV_MC_DIR", PRISM_DATA / "instances" / PRISM_INSTANCE / "minecraft")
)

# Relative to instance minecraft/. Globs are matched case-sensitively for the
# README.md filename (the crash we care about); parents may vary.
KNOWN_ORPHAN_GLOBS: tuple[str, ...] = (
    "kubejs/data/**/README.md",
    "kubejs/assets/**/README.md",
)


def collect_orphans() -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for pattern in KNOWN_ORPHAN_GLOBS:
        for path in sorted(DEV_MC_DIR.glob(pattern)):
            if not path.is_file():
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            found.append(path)
    return found


def main() -> int:
    dry_run = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")
    if not DEV_MC_DIR.is_dir():
        print(f"✗ instance minecraft folder not found: {DEV_MC_DIR}", file=sys.stderr)
        return 1

    orphans = collect_orphans()
    if not orphans:
        print(f"✓ {PRISM_INSTANCE}: no known orphan paths under {DEV_MC_DIR}")
        return 0

    print(f"→ {len(orphans)} known orphan(s) in {DEV_MC_DIR}:")
    for p in orphans:
        print(f"   {p.relative_to(DEV_MC_DIR)}")
    if dry_run:
        print("  (DRY_RUN — not deleting)")
        return 0

    for p in orphans:
        p.unlink()
    print(f"✓ removed {len(orphans)} orphan(s)")
    print("  tip: packwiz does not delete removed pack files — re-run after pack cleanups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
