#!/usr/bin/env python3
"""
CP Liminal — Recipe Wiki Builder

Entry point for `make recipe-wiki` / `python3 scripts/build_recipe_wiki.py`.
Implementation lives in recipe_wiki_core.py + recipe_wiki_render.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow `python3 scripts/build_recipe_wiki.py` from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent))

from recipe_wiki_render import main

if __name__ == "__main__":
    main()
