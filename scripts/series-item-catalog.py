#!/usr/bin/env python3
"""Compare items across mods from docs/series/items/data/*.json.

One JSON file per mod (see docs/series/items/README.md). This script does not read the game or
the mod jars; it only reads those files.

Usage:
    python3 scripts/series-item-catalog.py list                    # mods and item counts
    python3 scripts/series-item-catalog.py report [--category generator]
    python3 scripts/series-item-catalog.py levers [--mod powah]    # what can be tuned, and where
"""
import argparse
import glob
import json
import os
import sys

DATA = os.path.join(os.path.dirname(__file__), "..", "docs", "series", "items", "data")


def load():
    mods = []
    for path in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        with open(path, encoding="utf-8") as f:
            mods.append(json.load(f))
    return mods


def fmt(n):
    if isinstance(n, (int, float)):
        if n >= 1_000_000_000:
            return f"{n / 1_000_000_000:g}B"
        if n >= 1_000_000:
            return f"{n / 1_000_000:g}M"
        if n >= 1_000:
            return f"{n / 1_000:g}k"
        return f"{n:g}"
    return str(n)


def stat_range(item, key):
    values = item.get("stats", {}).get(key)
    if not values:
        return "-"
    return fmt(values[0]) if len(values) == 1 else f"{fmt(values[0])} to {fmt(values[-1])}"


def cmd_list(mods):
    for m in mods:
        print(f"{m['name']:<28} {len(m['items']):>3} entries   packs: {', '.join(m.get('packs', []))}")


def cmd_report(mods, category):
    groups = {}
    for m in mods:
        for item in m["items"]:
            cat = item["category"]
            if category and cat != category:
                continue
            groups.setdefault(cat, []).append((m, item))
    if not groups:
        print("nothing matches", file=sys.stderr)
        return 1
    for cat, rows in sorted(groups.items()):
        print(f"\n## {cat}  ({len({m['mod'] for m, _ in rows})} mod(s), {len(rows)} entries)\n")
        print("| Mod | Item | Kind | Output (FE/t) | Capacity (FE) | Transfer (FE/t) | Needs ore | Tunable via |")
        print("|---|---|---|---|---|---|---|---|")
        for m, item in sorted(rows, key=lambda r: (r[1].get("subcategory", ""), r[0]["name"])):
            print(
                f"| {m['name']} | {item['name']} | {item.get('subcategory', '-')} | {stat_range(item, 'output_fe_t')} | "
                f"{stat_range(item, 'capacity_fe')} | {stat_range(item, 'transfer_fe_t')} | "
                f"{'yes' if item.get('needs_ore') else ('no' if 'needs_ore' in item else '?')} | "
                f"{', '.join(item.get('tunable', [])) or '?'} |"
            )
    return 0


def cmd_levers(mods, mod):
    for m in mods:
        if mod and m["mod"] != mod:
            continue
        print(f"\n## {m['name']} (pinned {m.get('version_pinned', '?')})\n")
        for t in m.get("tuning", []):
            print(f"- **{t['lever']}** `{t['where']}`: {t['effect']}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    r = sub.add_parser("report")
    r.add_argument("--category")
    lv = sub.add_parser("levers")
    lv.add_argument("--mod")
    args = p.parse_args()
    mods = load()
    if args.cmd == "list":
        cmd_list(mods)
        return 0
    if args.cmd == "report":
        return cmd_report(mods, args.category)
    return cmd_levers(mods, args.mod)


if __name__ == "__main__":
    sys.exit(main())
