#!/usr/bin/env python3
"""Validate item tags against docs/series/items/tags.md, and find items to revisit.

Usage:
    python3 scripts/series-item-tags.py check               # unknown tags in data/*.json
    python3 scripts/series-item-tags.py check --missing     # entries missing power-role / power-type / kind / function
    python3 scripts/series-item-tags.py find facet:value ...  # items carrying ALL the given tags
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
        want = set(args[1:])
        for mod, it in entries():
            if want <= set(it.get("tags", [])):
                print(f"{mod} / {it.get('name')}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
