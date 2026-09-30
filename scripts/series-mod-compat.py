#!/usr/bin/env python3
"""Find which other mods a mod's source has built-in support for.

Usage:
    python3 scripts/series-mod-compat.py <source-dir> [--self MODID ...] [--root ..]

Looks in a cloned source tree for signs the author wrote integration code:
  - optional/required dependencies in META-INF/neoforge.mods.toml
  - mod_loaded conditions in data JSON (neoforge:conditions)
  - ModList isLoaded("x") checks and compat/integration/jei/emi/kubejs packages in Java
  - recipe, tag and loot data that references another namespace (modid:thing)
Each found mod id is matched against the pack mod slugs in the sibling pack repos (mods/*.pw.toml),
so the output says which of *our* mods it integrates with. "Support" weights a pairing:
an author who built it usually means the two work well together.
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

PACKS = ("verdant", "elysian", "influx", "liminal")
# namespace -> pack slug where the mod id differs from the packwiz file name
ALIASES = {"ae2": "applied-energistics-2", "appeng": "applied-energistics-2", "create": "create",
           "kubejs": "kubejs", "ftbquests": "ftb-quests", "ars_nouveau": "ars-nouveau", "projecte": "projecte",
           "tfc": None, "mekanism": "mekanism", "botania": None, "patchouli": "patchouli", "curios": "curios"}
SKIP_IDS = {"minecraft", "neoforge", "forge", "c", "java", "fml", "mixin", "kotlinforforge", "lowcodefml"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def pack_slugs(root):
    slugs = {}
    for pack in PACKS:
        for p in glob.glob(os.path.join(root, f"minecraft-modpack-cp-{pack}", "mods", "*.pw.toml")):
            slugs.setdefault(norm(os.path.basename(p)[:-8]), os.path.basename(p)[:-8])
    return slugs


def walk(src):
    for base, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in (".git", "build", "node_modules", "gradle")]
        for f in files:
            yield os.path.join(base, f)


def scan(src, own_ids=()):
    own = {norm(x) for x in own_ids} | SKIP_IDS
    found = defaultdict(lambda: defaultdict(set))
    for path in walk(src):
        rel = os.path.relpath(path, src)
        name = os.path.basename(path)
        try:
            if name == "neoforge.mods.toml":
                txt = open(path, encoding="utf-8", errors="ignore").read()
                for blk in re.split(r"\[\[dependencies", txt)[1:]:
                    mid = re.search(r'modId\s*=\s*"([^"]+)"', blk)
                    if mid:
                        found[mid.group(1)]["dependency"].add(rel)
            elif name.endswith(".java"):
                txt = open(path, encoding="utf-8", errors="ignore").read()
                for m in re.finditer(r'isLoaded\(\s*"([a-z0-9_]+)"\s*\)', txt):
                    found[m.group(1)]["isLoaded"].add(rel)
                if any(p in ("compat", "integration", "compatibility") for p in rel.lower().split(os.sep)):
                    for m in re.finditer(r'\bimport\s+((?:[a-z0-9_]+\.){2,}[a-z0-9_]+)', txt):
                        for p in m.group(1).split(".")[:4]:
                            found[p]["compat-import"].add(rel)
            elif name.endswith(".json") and "/data/" in "/" + rel.replace(os.sep, "/"):
                txt = open(path, encoding="utf-8", errors="ignore").read()
                for m in re.finditer(r'"mod_id"\s*:\s*"([a-z0-9_]+)"', txt):
                    found[m.group(1)]["mod_loaded"].add(rel)
                for m in re.finditer(r'"([a-z0-9_]+):[a-z0-9_/.]+"', txt):
                    found[m.group(1)]["data-ref"].add(rel)
        except OSError:
            pass
    return {k: v for k, v in found.items() if norm(k) not in own}


def resolve(mid, slugs):
    return slugs.get(norm(mid)) or (ALIASES.get(mid) if ALIASES.get(mid) in slugs.values() else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--self", nargs="*", default=[])
    ap.add_argument("--root", default="..")
    ap.add_argument("--all", action="store_true", help="also list ids that are not pack mods (noisy)")
    a = ap.parse_args()
    slugs = pack_slugs(a.root)
    rows = []
    for mid, kinds in scan(a.src, a.self).items():
        slug = resolve(mid, slugs)
        rows.append((bool(slug), mid, slug or "-", kinds))
    rows.sort(key=lambda r: (not r[0], r[1]))
    print("| Pack mod? | Id | Pack slug | Evidence |")
    print("|---|---|---|---|")
    for inpack, mid, slug, kinds in rows:
        if not inpack and not a.all:
            continue
        ev = ", ".join(f"{k} ({len(v)})" for k, v in sorted(kinds.items()))
        print(f"| {'yes' if inpack else 'no'} | `{mid}` | {slug} | {ev} |")


if __name__ == "__main__":
    sys.exit(main())
