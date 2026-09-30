#!/usr/bin/env python3
"""Where does each resource come from? Reads docs/series/items/yields/<mod>.json and lists every source.

Each file: {"mod", "version", "source", "entries": [{"resource", "form", "source", "tier"?, "power", "stage", "note"}], "note"?}
`stage` is bootstrap (first way to get it) or scale (how to get more). Numbers come from the mod's own data
and are unverified in-game.

Usage:
    python3 scripts/series-yields.py report <resource>      # every way to get iron, by stage
    python3 scripts/series-yields.py resources               # resources and how many sources each has
    python3 scripts/series-yields.py mods                    # which mods have yield data
"""
import collections
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
YIELDS = os.path.join(HERE, "..", "docs", "series", "items", "yields")


def packs(mod, root=os.path.join(HERE, "..", "..")):
    """Which packs carry this mod (V E I L), from the sibling repos' mods/ folders."""
    out = ""
    for letter, pack in (("V", "verdant"), ("E", "elysian"), ("I", "influx"), ("L", "liminal")):
        if os.path.exists(os.path.join(root, f"minecraft-modpack-cp-{pack}", "mods", mod + ".pw.toml")):
            out += letter
    return out or "-"


def load():
    for p in sorted(glob.glob(os.path.join(YIELDS, "*.json"))):
        yield json.load(open(p, encoding="utf-8"))


def main():
    a = sys.argv[1:]
    if a[:1] == ["report"] and len(a) == 2:
        res = a[1].lower()
        rows = [(d["mod"], e) for d in load() for e in d["entries"] if e["resource"].lower() == res]
        if not rows:
            print(f"no source for {res}")
            return 1
        for stage in ("bootstrap", "scale"):
            sel = [(m, e) for m, e in rows if e.get("stage") == stage]
            if sel:
                print(f"\n{stage.upper()}")
                for m, e in sel:
                    t = f" [{e['tier']}]" if e.get("tier") else ""
                    print(f"  {m} (packs: {packs(m)}): {e['form']}{t}; power: {e['power']}\n      {e['note']}")
        return 0
    if a[:1] == ["resources"]:
        c = collections.defaultdict(set)
        for d in load():
            for e in d["entries"]:
                c[e["resource"]].add(d["mod"])
        for r, mods in sorted(c.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            print(f"{len(mods):2}  {r:24} {', '.join(sorted(mods))}")
        return 0
    if a[:1] == ["mods"]:
        for d in load():
            print(f"{d['mod']:28} {len(d['entries']):4} entries  {d.get('note', '')[:70]}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
