#!/usr/bin/env python3
"""Validate item tags against docs/series/items/tags.md, and find items to revisit.

Usage:
    python3 scripts/series-item-tags.py check               # unknown tags in data/*.json
    python3 scripts/series-item-tags.py check --missing     # entries missing power-role / power-type / kind / function
    python3 scripts/series-item-tags.py find facet:value ... [--all]  # items carrying ALL the given tags (--all adds auto-tagged scan items)
    python3 scripts/series-item-tags.py stats               # tag counts over the auto-tagged scan items
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "docs", "series", "items")
REQUIRED = ("kind", "function", "power-role", "power-type")


def vocab():
    out = {}
    for line in open(os.path.join(ITEMS, "tags.md"), encoding="utf-8"):
        m = re.match(r"^\| `([a-z-]+)` \| ([^|]+) \|", line)
        if m and m.group(1) != "Facet":
            out[m.group(1)] = {v.strip() for v in m.group(2).split(",")}
    return out


def entries():
    for p in sorted(glob.glob(os.path.join(ITEMS, "data", "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        for it in d.get("items", []):
            yield d.get("name", d.get("mod")), it


def scan_entries():
    """Auto-tagged items from scan/*.json (first pass)."""
    for p in sorted(glob.glob(os.path.join(ITEMS, "scan", "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        for key, it in d.get("items", {}).items():
            yield os.path.basename(p)[:-5], {"id": key, "name": it["name"], "tags": it.get("tags", []), "kind_raw": it["kind"]}


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    v = vocab()
    if args[0] == "check":
        bad = 0
        for mod, it in entries():
            tags = it.get("tags", [])
            for t in tags:
                f, _, val = t.partition(":")
                if f not in v or val not in v[f]:
                    print(f"unknown tag {t!r} on {mod} / {it.get('name')}")
                    bad += 1
            if "--missing" in args:
                have = {t.partition(":")[0] for t in tags}
                miss = [f for f in REQUIRED if f not in have]
                if miss:
                    print(f"{mod} / {it.get('name')}: missing {', '.join(miss)}")
        return 1 if bad else 0
    if args[0] == "find":
        want = {a for a in args[1:] if not a.startswith("--")}
        for mod, it in entries():
            if want <= set(it.get("tags", [])):
                print(f"{mod} / {it.get('name')}")
        if "--all" in args:  # also the auto-tagged scan items
            for mod, it in scan_entries():
                if want <= set(it["tags"]):
                    print(f"{mod} / {it['name']}  ({it['id']}, auto)")
        return 0
    if args[0] == "stats":
        from collections import Counter
        c = Counter()
        n = 0
        for _, it in scan_entries():
            n += 1
            c.update(it["tags"])
        print(f"{n} scanned items")
        for t, k in sorted(c.items(), key=lambda kv: (kv[0].split(":")[0], -kv[1])):
            print(f"{k:6}  {t}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
