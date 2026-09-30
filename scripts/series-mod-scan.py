#!/usr/bin/env python3
"""Clone each mod's source (shallow, at the matching ref), list its items, and scan for built-in support
for other pack mods. Writes docs/series/items/scan/<mod>.json and docs/series/items/compat.md.

Usage (from the liminal repo root, with the other pack repos alongside for slugs):
    python3 scripts/series-mod-scan.py run    [--root ..] [--work DIR] [--only ID ...] [--jobs 4]
    python3 scripts/series-mod-scan.py report [--root ..]     # rewrite compat.md from scan/*.json

Sources come from docs/series/items/sources.json. Repos with no matching ref are scanned at the default
branch and flagged `ref_kind: default` (lower confidence, may be another version).
"""
import argparse
import concurrent.futures as cf
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "docs", "series", "items")
SCAN = os.path.join(ITEMS, "scan")
spec = importlib.util.spec_from_file_location("compat", os.path.join(HERE, "series-mod-compat.py"))
compat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compat)

NOISE = re.compile(r"(tooltip|desc|config|advancement|command|death|gui|key|jei|emi|jade|subtitle|itemGroup|creativetab|"
                   r"patchouli|ponder|book|manual|message|tag\.|effect\.|enchantment\.|potion|stat\.|container\.|sounds?)", re.I)


def own_ids(src):
    ids = set()
    for p in glob.glob(os.path.join(src, "**", "neoforge.mods.toml"), recursive=True):
        try:
            d = tomllib.load(open(p, "rb"))
        except Exception:
            continue
        for m in d.get("mods", []):
            if m.get("modId"):
                ids.add(m["modId"])
    for p in glob.glob(os.path.join(src, "**", "assets", "*", "lang", "en_us.json"), recursive=True):
        ids.add(p.split(os.sep + "assets" + os.sep)[1].split(os.sep)[0])
    return ids


def items(src, ids):
    out = {}
    for p in glob.glob(os.path.join(src, "**", "assets", "*", "lang", "en_us.json"), recursive=True):
        mid = p.split(os.sep + "assets" + os.sep)[1].split(os.sep)[0]
        if mid in ("minecraft",):
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for k, v in d.items():
            m = re.match(r"^(block|item|entity|fluid)\.([a-z0-9_]+)\.([a-z0-9_./]+)$", k)
            if m:
                kind, ns, name = m.groups()
            else:  # SuperMartijn642 style: <modid>.item.<name>
                m = re.match(r"^([a-z0-9_]+)\.(block|item|entity|fluid)\.([a-z0-9_./]+)$", k)
                if not m:
                    continue
                ns, kind, name = m.groups()
            if not isinstance(v, str) or NOISE.search(name):
                continue
            out[f"{ns}:{name}"] = {"kind": kind, "name": v}
    return out


def scan_compat(src, ids, slugs):
    found = compat.scan(src, ids)
    rows = []
    for mid, kinds in found.items():
        slug = compat.resolve(mid, slugs)
        if slug:
            rows.append({"id": mid, "slug": slug, "evidence": {k: len(v) for k, v in sorted(kinds.items())}})
    rows.sort(key=lambda r: r["slug"])
    return rows


def one(mod, info, slugs, work):
    dest = os.path.join(work, mod)
    ref = info["ref"] if info.get("ref") else None
    cmd = ["git", "clone", "-q", "--depth", "1"] + (["--branch", ref] if ref else []) + [f"https://github.com/{info['repo']}", dest]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        return mod, {"error": r.stderr.strip()[-200:], "repo": info["repo"]}
    try:
        ids = own_ids(dest)
        its = items(dest, ids)
        res = {"repo": info["repo"], "ref": ref or "default", "ref_kind": info.get("ref_kind") or "default",
               "mod_ids": sorted(ids), "item_count": len(its), "compat": scan_compat(dest, ids, slugs), "items": its}
    finally:
        shutil.rmtree(dest, ignore_errors=True)
    return mod, res


def cmd_run(a):
    src = json.load(open(os.path.join(ITEMS, "sources.json")))["mods"]
    slugs = compat.pack_slugs(a.root)
    todo = {k: v for k, v in src.items() if v.get("repo") and (not a.only or k in a.only)}
    os.makedirs(SCAN, exist_ok=True)
    os.makedirs(a.work, exist_ok=True)
    done = {}
    # Mods that share a repo (Mekanism modules) are scanned once per repo.
    seen = {}
    for k, v in list(todo.items()):
        key = (v["repo"], v.get("ref"))
        if key in seen:
            done[k] = seen[key]
            del todo[k]
        else:
            seen[key] = k
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        for mod, res in ex.map(lambda kv: one(kv[0], kv[1], slugs, a.work), todo.items()):
            json.dump(res, open(os.path.join(SCAN, f"{mod}.json"), "w"), indent=1, ensure_ascii=False)
            print(mod, res.get("error") or f"{res['item_count']} items, {len(res['compat'])} compat")
    for mod, canon in done.items():
        json.dump({"same_repo_as": canon}, open(os.path.join(SCAN, f"{mod}.json"), "w"), indent=1)


def cmd_report(a):
    rows = []
    links = {}
    for p in sorted(glob.glob(os.path.join(SCAN, "*.json"))):
        mod = os.path.basename(p)[:-5]
        d = json.load(open(p))
        if "same_repo_as" in d:
            continue
        rows.append((mod, d))
        for slug in {c["slug"] for c in d.get("compat", [])}:
            if slug != mod:
                links.setdefault(slug, []).append(mod)
    print("# Built-in support scan\n")
    print("Generated by `scripts/series-mod-scan.py`. For each mod with public source: how many items it adds, and which **other pack mods** its source has code or data for. Standard integrations (JEI, EMI, Jade, Patchouli, Curios, KubeJS) are listed but carry little weight. Mods sharing one repo (Mekanism modules) appear once.\n")
    std = {"jei", "emi", "jade", "patchouli", "curios", "kubejs", "cloth-config", "architectury-api", "rei", "ftb-library", "ftb-teams"}
    print("## Per mod\n")
    print("| Mod | Items | Ref | Supports (other pack mods) |")
    print("|---|---|---|---|")
    for mod, d in rows:
        if d.get("error"):
            print(f"| {mod} | - | error | {d['error'][:60]} |")
            continue
        sup = ", ".join(sorted({c["slug"] for c in d["compat"] if c["slug"] not in std and c["slug"] != mod})) or "-"
        print(f"| {mod} | {d['item_count']} | {d['ref_kind']} | {sup} |")
    print("\n## Most supported by others (hubs)\n")
    print("| Mod | Supported by |")
    print("|---|---|")
    for slug, who in sorted(links.items(), key=lambda kv: -len(kv[1])):
        if slug in std:
            continue
        print(f"| {slug} | {len(who)}: {', '.join(sorted(who))[:200]} |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "report"])
    ap.add_argument("--root", default="..")
    ap.add_argument("--work", default=os.path.join(os.environ.get("TMPDIR", "/tmp"), "series-scan"))
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    {"run": cmd_run, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
