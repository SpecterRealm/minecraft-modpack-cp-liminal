#!/usr/bin/env python3
"""Mod-level profiles for go/no-go: feel, main contribution, gap, fit per pack.

Reads docs/series/items/profiles.json; writes docs/series/items/mod-profiles.md.
Usage:
    python3 scripts/series-profiles.py check            # vocabulary and missing-mod check
    python3 scripts/series-profiles.py report [--root ..] > docs/series/items/mod-profiles.md
"""
import argparse
import collections
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "docs", "series", "items")
FEEL = {"tech", "magic", "alchemy", "nature", "breeding", "steampunk", "sci-fi", "survival", "neutral"}
ADD = {"resources", "power", "tooling", "armor", "storage", "processing", "automation", "combat", "content", "food", "building", "integration", "qol", "library"}
RATE = {"good", "partial", "poor"}
PACKS = (("V", "verdant"), ("E", "elysian"), ("I", "influx"), ("L", "liminal"))


def load():
    d = json.load(open(os.path.join(ITEMS, "profiles.json"), encoding="utf-8"))
    return d["mods"]


def membership(root):
    m = collections.defaultdict(str)
    for L, p in PACKS:
        for f in glob.glob(os.path.join(root, f"minecraft-modpack-cp-{p}", "mods", "*.pw.toml")):
            m[os.path.basename(f)[:-8]] += L
    return m


def check():
    mods = load()
    bad = 0
    for m, p in mods.items():
        for f in p["feel"]:
            if f not in FEEL:
                print(f"{m}: unknown feel {f}"); bad += 1
        if p["add"] not in ADD:
            print(f"{m}: unknown add {p['add']}"); bad += 1
        for a in p.get("also", []):
            if a not in ADD:
                print(f"{m}: unknown also {a}"); bad += 1
        for k, (r, _) in p.get("fit", {}).items():
            if r not in RATE:
                print(f"{m}: unknown rating {r}"); bad += 1
    scans = {os.path.basename(x)[:-5] for x in glob.glob(os.path.join(ITEMS, "scan", "*.json"))}
    miss = sorted(scans - set(mods))
    if miss:
        print("no profile:", ", ".join(miss))
    return 1 if bad else 0


def report(root):
    mods = load()
    mem = membership(root)
    skip = {"library", "qol", "integration"}
    print("# Mod profiles (go/no-go input)\n")
    print("Generated from `profiles.json` by `scripts/series-profiles.py`. **Nothing here is a verdict.** Every mod starts `pending`; go/no-go is decided per pack after its deep review, on three things: does it fit the pack's world, does it fill a gap (how we obtain or process something), and what does it add. `feel` is the story/aesthetic (two or more values = hybrid). Fit ratings are first reads to be argued with.\n")
    print("Packs: V Verdant (overworld, no ore, tech-first), E Elysian (void, magic only, no sieve), I Influx (ship, space-limited, closed loops, EMC), L Liminal (union, bridges).\n")
    print("## Content and capability mods\n")
    print("| Mod | Packs | Feel | Main add | Also | Gap it fills | V | E | I | L |\n|---|---|---|---|---|---|---|---|---|---|")
    rows = sorted(((m, p) for m, p in mods.items() if p["add"] not in skip), key=lambda x: (x[1]["add"], x[0]))
    for m, p in rows:
        cells = []
        for L, _ in PACKS:
            f = p.get("fit", {}).get(L)
            cells.append(f"{f[0]}" if f else ("" if L in mem.get(m, "") else "-"))
        print(f"| {m} | {mem.get(m, '-')} | {'+'.join(p['feel'])} | {p['add']} | {', '.join(p['also'])} | {p['gap'][:70]} | " + " | ".join(cells) + " |")
    print("\n## Feel by pack (which mods sit outside a pack's theme)\n")
    for L, name in (("V", "Verdant"), ("E", "Elysian"), ("I", "Influx")):
        by = collections.defaultdict(list)
        for m, p in mods.items():
            if L in mem.get(m, "") and p["add"] not in skip:
                for f in p["feel"]:
                    by[f].append(m)
        print(f"**{name}:** " + "; ".join(f"{f} ({len(v)})" for f, v in sorted(by.items(), key=lambda kv: -len(kv[1]))))
        if L == "E":
            print(f"\nTech-feel mods in Elysian (pure tech, no magic co-feel): " + ", ".join(sorted(m for m, p in mods.items() if "E" in mem.get(m, "") and "tech" in p["feel"] and "magic" not in p["feel"] and p["add"] not in skip)) + "\n")
        if L == "V":
            print(f"\nMagic-feel mods in Verdant: " + (", ".join(sorted(m for m, p in mods.items() if "V" in mem.get(m, "") and "magic" in p["feel"] and p["add"] not in skip)) or "none") + "\n")
    print("\n## Main add by pack\n")
    print("What each pack's non-library mods mainly contribute; a pack with nothing under a heading has a gap there.\n")
    print("| Main add | Verdant | Elysian | Influx |\n|---|---|---|---|")
    for a in ("resources", "processing", "power", "tooling", "armor", "storage", "automation", "combat", "content", "food", "building"):
        cols = []
        for L in "VEI":
            ms = sorted(m for m, p in mods.items() if L in mem.get(m, "") and p["add"] == a)
            cols.append(", ".join(ms) or "**none**")
        print(f"| {a} | " + " | ".join(cols) + " |")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check", "report"])
    ap.add_argument("--root", default="..")
    a = ap.parse_args()
    sys.exit(check() if a.cmd == "check" else report(a.root))
