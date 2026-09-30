#!/usr/bin/env python3
"""
CP Liminal — Recipe Wiki Builder

Entry point for `make recipe-wiki` / `python3 scripts/build_recipe_wiki.py`.
Assembles recipe_wiki_core.py from .github/recipe-wiki-parts when missing,
then runs recipe_wiki_render.main.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

CORE = HERE / "recipe_wiki_core.py"
if not CORE.exists():
    parts_dir = REPO / ".github" / "recipe-wiki-parts"
    parts = sorted(parts_dir.glob("core.part*"))
    if not parts:
        raise SystemExit(
            f"Missing {CORE.name} and no parts under {parts_dir}"
        )
    CORE.write_text("".join(p.read_text(encoding="utf-8") for p in parts), encoding="utf-8")

from recipe_wiki_render import main

if __name__ == "__main__":
    main()
