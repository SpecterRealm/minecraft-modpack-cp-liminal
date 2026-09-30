#!/usr/bin/env python3
"""Loop-back review: apply per-mod correction rules to the auto-tagged scan items and mark them checked.

A review file docs/series/items/review/<mod>.json holds the decisions made while reading a mod's whole item list:

    {
      "note": "what the mod is for in the pack, anything odd",
      "rules": [
        {"match": "_ore_chunk$", "kind": "item",            # regex on the id after the colon; optional block|item|entity|fluid
         "clear": ["kind", "needs"],                        # drop every tag of these facets first
         "set": ["kind:material", "needs:none"],            # then add these tags
         "default": ["power-role:none"],                    # add a tag only when its facet has none yet
         "ui": false}                                       # true: UI/label text, no tags at all
      ]
    }

Rules run in order on each item's existing (auto) tags. Every item in the mod ends up `review:checked` with a
file-level record (date, version, pass) — only run this after reading the whole list. Re-running is safe
(idempotent), so after `series-mod-scan.py run` + `series-item-autotag.py run` just apply again.

Usage:
    python3 scripts/series-item-review.py apply <mod> [--dry]
    python3 scripts/series-item-review.py list <mod>         # id + tags, to read before writing rules
    python3 scripts/series-item-review.py status             # reviewed mods, and the biggest unreviewed ones
"""
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "docs", "series", "items")
SCAN = os.path.join(ITEMS, "scan")
REVIEW = os.path.join(ITEMS, "review")


def load(mod):
    return json.load(open(os.path.join(SCAN, mod + ".json"), encoding="utf-8"))


def apply(mod, dry=False):
    rules = json.load(open(os.path.join(REVIEW, mod + ".json"), encoding="utf-8"))
    d = load(mod)
    changed = 0
    for key, it in d["items"].items():
        name = key.split(":", 1)[1]
        before = [t for t in it.get("tags", []) if not t.startswith("review:")]
        tags = list(before)
        for r in rules["rules"]:
            if r.get("kind") and r["kind"] != it["kind"]:
                continue
            m = re.search(r["match"], name)
            if not m:
                continue
            if r.get("ui"):
                tags = []
                break  # UI text: no tags, ignore later rules
            for facet in r.get("clear", []):
                tags = [t for t in tags if not t.startswith(facet + ":")]
            for t in r.get("set", []):
                t = t.format(*m.groups()) if "{" in t else t  # e.g. "yields:{1}" from a capture group
                if t not in tags:
                    tags.append(t)
            for t in r.get("default", []):  # add only if the facet has no tag yet
                if not any(x.startswith(t.split(":")[0] + ":") for x in tags):
                    tags.append(t)
            for t in r.get("remove", []):
                if t in tags:
                    tags.remove(t)
        changed += tags != before
        it["tags"] = tags + ["review:checked"]
    d["review"] = {"status": "checked", "date": datetime.date.today().isoformat(), "mod_version": re.sub(r"^v", "", str(d.get("ref") or "")),
                   "pass": "loop-back", "note": rules.get("note", "")}
    if dry:
        print(f"{mod}: would change tags on {changed} of {len(d['items'])} items")
        return
    json.dump(d, open(os.path.join(SCAN, mod + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{mod}: {changed} of {len(d['items'])} items changed; all marked review:checked")


def status():
    done, todo = [], []
    for p in sorted(glob.glob(os.path.join(SCAN, "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        if "same_repo_as" in d or not d.get("items"):
            continue
        mod = os.path.basename(p)[:-5]
        (done if d.get("review") else todo).append((mod, len(d["items"]), d.get("review")))
    print(f"{len(done)} mods reviewed, {len(todo)} to go")
    for mod, n, r in done:
        print(f"  done  {mod:30} {n:5} items  {r['date']}  {r['mod_version']}")
    for mod, n, _ in sorted(todo, key=lambda x: -x[1])[:15]:
        print(f"  todo  {mod:30} {n:5} items")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["apply"] and len(a) >= 2:
        apply(a[1], "--dry" in a)
    elif a[:1] == ["list"] and len(a) >= 2:
        for k, it in load(a[1])["items"].items():
            print(f"{k.split(':', 1)[1]:40} {it['kind'][:2]} {','.join(t for t in it.get('tags', []) if not t.startswith('review:')) or '-'}")
    elif a[:1] == ["status"]:
        status()
    else:
        print(__doc__)
