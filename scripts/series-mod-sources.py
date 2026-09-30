#!/usr/bin/env python3
"""Track where each mod's source code lives, and which ref matches our pin.

Reads docs/series/items/sources.json (mod id -> repo, status, note), and the pins from the
sibling pack repos (mods/*.pw.toml). Public repos are checked with `git ls-remote` (no clone).

Usage (from the liminal repo root, with the other repos cloned alongside it):
    python3 scripts/series-mod-sources.py check  [--root ..] [--only ID ...]   # verify repos, find refs
    python3 scripts/series-mod-sources.py report [--root ..]  > docs/series/items/sources.md

Status values: (blank = has a repo), not-found, closed-or-private, own.
After `check`, each mod with a repo has: verified, ref, ref_kind (tag | branch | none).
"""
import argparse
import concurrent.futures as cf
import glob
import json
import os
import re
import subprocess
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(HERE, "..", "docs", "series", "items", "sources.json")
PACKS = {"V": "verdant", "E": "elysian", "I": "influx", "L": "liminal"}
MC_VERSIONS = {"1.21", "1.21.1", "21.1", "1.21.11", "1.21.0"}
BRANCH_PATTERNS = (r"(?<![\d.])1\.21\.1(?!\d)", r"(?<![\d.])1\.21\.x", r"(?<![\d.])1\.21(?![\d.]*\d)", r"(?<!\d)21\.1(?!\d)", r"(?<!\d)2101(?!\d)", r"neoforge")


def load():
    with open(SOURCES, encoding="utf-8") as f:
        return json.load(f)


def save(data):
    with open(SOURCES, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def pins(root):
    out = {}
    for letter, pack in PACKS.items():
        for path in glob.glob(os.path.join(root, f"minecraft-modpack-cp-{pack}", "mods", "*.pw.toml")):
            mid = os.path.basename(path)[: -len(".pw.toml")]
            with open(path, "rb") as f:
                d = tomllib.load(f)
            e = out.setdefault(mid, {"name": d.get("name", mid), "filename": d.get("filename", ""), "packs": ""})
            if letter not in e["packs"]:
                e["packs"] += letter
    return out


def versions(filename):
    return [v for v in re.findall(r"\d+(?:\.\d+)+", filename or "") if v not in MC_VERSIONS]


def ls(repo, kind):
    r = subprocess.run(
        ["git", "ls-remote", f"--{kind}", "--refs", f"https://github.com/{repo}"],
        capture_output=True, text=True, timeout=90,
        env={"GIT_TERMINAL_PROMPT": "0", "PATH": os.environ.get("PATH", "/usr/bin:/bin")},
    )
    if r.returncode:
        return None
    return [line.split(f"refs/{kind}/")[1] for line in r.stdout.splitlines()]


OTHER_MC = re.compile(r"(?<![\d.])1\.(?:1[0-9]|20)(?:\.\d+)?(?![\d])")


def pick_ref(tags, heads, vers):
    """Prefer a tag that contains the pinned version and does not name another Minecraft version."""
    suspect = None
    for v in vers:
        for t in tags:
            if t.lstrip("v") == v or v in t:
                if OTHER_MC.search(t.replace(v, "")):
                    suspect = suspect or t
                    continue
                return t, "tag"
    usable = [h for h in heads if "fabric" not in h.lower() and "forge-1.20" not in h.lower()]
    for pat in BRANCH_PATTERNS:
        for h in usable:
            if re.search(pat, h):
                return h, "branch"
    if suspect:
        return suspect, "tag?"
    return None, "none"


def check_one(item):
    mid, entry, filename = item
    repo = entry["repo"]
    try:
        tags = ls(repo, "tags")
    except subprocess.TimeoutExpired:
        return mid, {"verified": False, "ref": None, "ref_kind": "none", "check": "timeout"}
    if tags is None:
        return mid, {"verified": False, "ref": None, "ref_kind": "none", "check": "unreachable"}
    heads = ls(repo, "heads") or []
    ref, kind = pick_ref(tags, heads, versions(filename))
    return mid, {"verified": True, "ref": ref, "ref_kind": kind, "check": "ok"}


def cmd_check(root, only):
    data = load()
    pin = pins(root)
    todo = [
        (mid, e, pin.get(mid, {}).get("filename", ""))
        for mid, e in data["mods"].items()
        if e.get("repo") and (not only or mid in only)
    ]
    with cf.ThreadPoolExecutor(3) as ex:
        for mid, res in ex.map(check_one, todo):
            data["mods"][mid].update(res)
    save(data)
    kinds = {}
    for mid, e in data["mods"].items():
        if e.get("repo"):
            kinds[e.get("ref_kind", "unchecked")] = kinds.get(e.get("ref_kind", "unchecked"), 0) + 1
    print("checked", len(todo), "repos:", kinds)


def link(repo):
    return f"[{repo}](https://github.com/{repo})"


def cmd_report(root):
    data = load()["mods"]
    pin = pins(root)
    rows = []
    for mid, e in sorted(data.items()):
        p = pin.get(mid, {})
        rows.append((mid, p.get("name", mid), p.get("packs", ""), p.get("filename", ""), e))

    def section(title, pred, cols):
        sel = [r for r in rows if pred(r[4])]
        print(f"\n## {title} ({len(sel)})\n")
        if not sel:
            print("None.")
            return
        print("| Mod | Packs | Pin | " + " | ".join(cols[0]) + " |")
        print("|---|---|---|" + "---|" * len(cols[0]))
        for mid, name, packs, fn, e in sel:
            print(f"| {name} | {packs} | `{fn}` | " + " | ".join(cols[1](e)) + " |")

    total = len(rows)
    with_repo = [r for r in rows if r[4].get("repo")]
    print("# Mod sources\n")
    print(f"> Generated by `scripts/series-mod-sources.py report`. Data: `sources.json`. {total} mods; {len(with_repo)} have a suggested repo.\n")
    print("Goal: read each mod's source (item list, config, data, recipes) at the ref that matches our pin, instead of opening jars. See [README](README.md).")
    print("\n**Legend.** *tag* = a tag matches the pinned version. *branch* = a branch for our Minecraft version. *tag?* = a tag has the version but names another Minecraft version (check). *none* = repo found, no clear ref. *unchecked* = repo not verified yet.")

    def refcell(e):
        if not e.get("verified"):
            return "unchecked" if "verified" not in e else "unreachable"
        return f"{e['ref_kind']}: `{e['ref']}`" if e.get("ref") else "none"

    section("Source found, ref matches pin (tag)", lambda e: e.get("repo") and e.get("ref_kind") == "tag",
            (["Repo", "Ref", "Note"], lambda e: [link(e["repo"]), refcell(e), e.get("note", "")]))
    section("Source found, Minecraft-version branch", lambda e: e.get("repo") and e.get("ref_kind") == "branch",
            (["Repo", "Ref", "Note"], lambda e: [link(e["repo"]), refcell(e), e.get("note", "")]))
    section("Source found, no clear ref (or not verified)", lambda e: e.get("repo") and e.get("ref_kind") not in ("tag", "branch"),
            (["Repo", "Ref", "Note"], lambda e: [link(e["repo"]), refcell(e), e.get("note", "")]))
    section("No public source found", lambda e: e.get("status") == "not-found",
            (["Note"], lambda e: [e.get("note", "")]))
    section("Closed source, private, or no repo", lambda e: e.get("status") == "closed-or-private",
            (["Note"], lambda e: [e.get("note", "")]))
    section("Ours", lambda e: e.get("status") == "own", (["Note"], lambda e: [e.get("note", "")]))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["check", "report"])
    p.add_argument("--root", default=os.path.join(HERE, "..", ".."))
    p.add_argument("--only", nargs="*")
    a = p.parse_args()
    if a.cmd == "check":
        cmd_check(a.root, set(a.only or []))
    else:
        cmd_report(a.root)


if __name__ == "__main__":
    sys.exit(main())
