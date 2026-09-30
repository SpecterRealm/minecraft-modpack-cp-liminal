#!/usr/bin/env python3
"""Find mods that may not earn their place, from the catalog data. Writes docs/series/items/cleanup.md.

Inputs: scan/<mod>.json (class, purpose, tags, compat), sources.json, the sibling pack repos (mods/ and kubejs/).
Flags:
  library-unused   a library class mod that no other pack mod's source depends on or references
  addon-unused     a KubeJS add-on whose target mod's namespace never appears in any pack's kubejs/ scripts
  overlapped       a content mod whose every capability (function + power type) is also provided by other mods
  isolated         a content mod with no support to or from other pack mods\n  no-source        no public source, so dependents and items could not be read (check in game)
  dev-only         only test or dev items
These are *prompts to look*, not verdicts: a flag means "ask why this mod is here".

Usage:  python3 scripts/series-cleanup.py [--root ..] > docs/series/items/cleanup.md
"""
import argparse
import collections
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "docs", "series", "items")
PACKS = (("V", "verdant"), ("E", "elysian"), ("I", "influx"), ("L", "liminal"))
STD = {"jei", "emi", "jade", "patchouli", "curios", "kubejs", "cloth-config", "architectury-api", "rhino", "bookshelf", "guideme"}
KJS_TARGET = {"kubejs-create": "create", "kubejs-mekanism": "mekanism", "kubejs-ars-nouveau": "ars_nouveau", "kubejs-botany-pots": "botanypots",
              "kubejs-delight": "farmersdelight", "kubejs-irons-spells": "irons_spellbooks", "kubejs-projecte": "projecte",
              "occultism-kubejs": "occultism", "theurgy-kubejs": "theurgy", "kubejs-ex-deorum": "exdeorum",
              "kubejs-create-automation": "create", "kubejs-eyejs": "eyejs", "kubejs-tweaks": "kubejs"}
CAP_KINDS = {"machine", "multiblock", "gadget", "tool", "weapon", "armor", "storage", "block"}


def load(root):
    mods = {}
    for p in sorted(glob.glob(os.path.join(ITEMS, "scan", "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        if "same_repo_as" in d:
            continue
        mods[os.path.basename(p)[:-5]] = d
    src = json.load(open(os.path.join(ITEMS, "sources.json"), encoding="utf-8"))["mods"]
    packs = collections.defaultdict(str)
    kjs = {}
    for letter, pack in PACKS:
        base = os.path.join(root, f"minecraft-modpack-cp-{pack}")
        for f in glob.glob(os.path.join(base, "mods", "*.pw.toml")):
            packs[os.path.basename(f)[:-8]] += letter
        text = ""
        for f in glob.glob(os.path.join(base, "kubejs", "**", "*.js"), recursive=True):
            try:
                text += open(f, encoding="utf-8", errors="ignore").read()
            except OSError:
                pass
        kjs[letter] = text
    return mods, src, packs, kjs


def caps(d):
    """Power capabilities only: what a mod's machines make, store or move, by fuel and power type.
    Specific on purpose: 'generate + fe' alone would overlap with everything."""
    out = collections.Counter()
    for it in d.get("items", {}).values():
        t = it.get("tags", [])
        if not ({x.split(":")[1] for x in t if x.startswith("kind:")} & CAP_KINDS):
            continue
        roles = {x.split(":")[1] for x in t if x.startswith("power-role:")}
        ptype = [x.split(":")[1] for x in t if x.startswith("power-type:") and x != "power-type:none"]
        fuel = [x.split(":")[1] for x in t if x.startswith("fuel:")] or ["unknown"]
        for p in ptype:
            if "makes" in roles:
                for f in fuel:
                    out[f"makes {p} from {f}"] += 1
            if "stores" in roles:
                out[f"stores {p}"] += 1
            if "transfers" in roles:
                out[f"moves {p}"] += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="..")
    a = ap.parse_args()
    mods, src, packs, kjs = load(a.root)
    dependents = collections.defaultdict(set)
    supported = collections.defaultdict(set)
    for m, d in mods.items():
        for c in d.get("compat", []):
            if c["slug"] == m:
                continue
            supported[c["slug"]].add(m)
            if "dependency" in c.get("evidence", {}):
                dependents[c["slug"]].add(m)
    capmap = {m: caps(d) for m, d in mods.items()}
    cand_early = {m for m in mods if src.get(m, {}).get("candidate")}
    providers = collections.defaultdict(dict)
    for m, c in capmap.items():
        if m in cand_early:
            continue
        for k, n in c.items():
            providers[k][m] = n
    rows = []
    cand = {m for m in mods if src.get(m, {}).get("candidate")}
    for m, d in mods.items():
        if m in cand:
            continue
        r = d.get("review") or {}
        cls = r.get("class", "content" if d.get("items") else "?")
        flags = []
        closed = src.get(m, {}).get("status") in ("not-found", "closed-or-private")
        if closed or not src.get(m, {}).get("repo"):
            flags.append("no-source")
        if cls == "library" and not dependents.get(m) and not supported.get(m) and not closed:
            flags.append("library-unused")
        if cls == "kubejs-addon" and m in KJS_TARGET:
            ns = KJS_TARGET[m]
            used = {L for L, t in kjs.items() if re.search(r"\b" + re.escape(ns) + r"\b", t) and L in packs.get(m, "")}
            if not used:
                flags.append("addon-unused")
        c = capmap[m]
        if c:
            over = [k for k in c if any(o != m and n >= c[k] and set(packs.get(o, "")) & set(packs.get(m, "")) for o, n in providers[k].items())]
            if len(over) == len(c) and len(c) >= 1:
                flags.append("overlapped")
        infra = lambda x: (mods.get(x, {}).get("review") or {}).get("class") in ("library", "guide", "viewer", "perf-client", "qol-client") or x in STD
        outs = {c["slug"] for c in d.get("compat", []) if not infra(c["slug"]) and c["slug"] != m}
        if cls == "content" and d.get("items") and not closed and not outs and not {x for x in supported.get(m, set()) if not infra(x)} and not dependents.get(m):
            flags.append("isolated")
        if d.get("items") and all("role:dev-only" in i.get("tags", []) for i in d["items"].values()):
            flags.append("dev-only")
        rows.append((m, d, r, cls, flags, dependents.get(m, set()), supported.get(m, set()), c))
    print("# Pack cleanup candidates\n")
    print("Generated by `scripts/series-cleanup.py` from the catalog. A flag is a prompt to ask *why is this mod here*, not a verdict. Packs: V Verdant, E Elysian, I Influx, L Liminal.\n")
    by = collections.Counter(r[3] for r in rows)
    print("## Mods by class\n")
    print("| Class | Mods |\n|---|---|")
    for k, v in sorted(by.items(), key=lambda kv: -kv[1]):
        print(f"| {k} | {v} |")
    def section(title, flag, blurb):
        sel = [r for r in rows if flag in r[4]]
        print(f"\n## {title} ({len(sel)})\n\n{blurb}\n")
        if not sel:
            print("_None._")
            return
        print("| Mod | Packs | Items | What it is | Notes |\n|---|---|---|---|---|")
        for m, d, r, cls, flags, dep, sup, c in sel:
            note = ""
            if flag == "overlapped":
                others = sorted({o for k in c for o in providers[k] if o != m})[:6]
                note = "overlaps " + ", ".join(others)
            if flag == "library-unused":
                note = "nothing in the pack references it"
            print(f"| {m} | {packs.get(m, '-')} | {d.get('item_count', 0)} | {(r.get('purpose') or '')[:70]} | {note} |")
    section("Libraries nothing depends on", "library-unused", "Library mods that no other pack mod's source declares as a dependency or references. Libraries are often pulled in by closed-source mods, so check the mod page before removing.")
    section("KubeJS add-ons no script uses", "addon-unused", "The add-on's target mod never appears in the pack's `kubejs/` scripts. Keep-for-now items from the audit; use them or remove them.")
    section("Power mods fully overlapped", "overlapped", "Every power capability this mod has (making power by fuel, storing it, moving it) is also provided by another mod in the same pack with at least as many items. These are the first to question for the power stack (Liminal #45). Only power is compared; other overlaps are in the cluster table of the mod audit.")
    section("Isolated content mods", "isolated", "Content mods with no built-in support for any other pack mod, and that no other pack mod supports (standard viewers like JEI/EMI/Jade ignored). They stand alone, so they earn their place only through what they add themselves. Check these for overlap by hand.")
    section("Dev-only mods", "dev-only", "Only test or dev items.")
    nosrc = sorted(m for m in src if m not in mods and not src[m].get("candidate") and packs.get(m) and src[m].get("status"))
    print(f"\n## No public source ({len(nosrc)})\n\nNo repo we can read, so items and dependents are unknown; look at these in the game. Status: not-found = no repo found, closed-or-private = exists but not readable, own = ours.\n")
    print("| Mod | Packs | Status |\n|---|---|---|")
    for m in nosrc:
        print(f"| {m} | {packs.get(m, '-')} | {src[m].get('status') or '-'} |")
    print("\n## Out-of-theme items by mod (hide / uncraftable input)\n")
    print("Items whose tags say they need world ore, the Nether or the End, in mods that ship in Verdant, Elysian or Influx (where ore worldgen is off and Nether/End are not progression paths). Decoration and material items are included; this is an input for the hide lists, not a decision.\n")
    print("| Mod | Packs | needs ore | needs Nether | needs End | Items |\n|---|---|---|---|---|---|")
    rows2 = []
    for m, d in mods.items():
        if m in cand or not set(packs.get(m, "")) & set("VEI"):
            continue
        n = collections.Counter()
        for it in d.get("items", {}).values():
            for k in ("ore", "nether", "end"):
                if f"needs:{k}" in it.get("tags", []):
                    n[k] += 1
        if sum(n.values()):
            rows2.append((sum(n.values()), m, n, d.get("item_count", 0)))
    for tot, m, n, cnt in sorted(rows2, reverse=True)[:30]:
        print(f"| {m} | {packs.get(m, '-')} | {n['ore']} | {n['nether']} | {n['end']} | {cnt} |")
    print("\n## Named-item clusters (same job, different mods)\n")
    print("Items whose id contains these words, by mod. Where several mods each add one, pick a primary or test whether one tool replaces the rest.\n")
    print("| Word | Mods (count) |\n|---|---|")
    for word in ("wrench", "hammer", "paxel", "magnet", "jetpack", "teleporter", "backpack", "barrel", "sieve", "crucible", "wand", "pickaxe", "sword"):
        who = collections.Counter()
        for m, d in mods.items():
            if m in cand:
                continue
            c = sum(1 for k in d.get("items", {}) if re.search(r"(^|_)" + word + r"(s)?($|_)", k.split(":")[1]))
            if c:
                who[m] = c
        if len(who) >= 2:
            print(f"| {word} | " + ", ".join(f"{m} ({c})" for m, c in who.most_common(10)) + " |")
    print("\n## Candidates not in any pack\n")
    print("Mods we looked at but did not add. For each capability, who in the packs already provides it, and what it would add.\n")
    print("| Candidate | Items | Capabilities it would add | Already covered by |\n|---|---|---|---|")
    for m in sorted(cand):
        c = capmap[m]
        d = mods[m]
        new = [k for k in c if c[k] >= 2 and not providers.get(k)]
        cov = {k: sorted(providers.get(k, {}), key=lambda o: -providers[k][o])[:3] for k in c if c[k] >= 2 and providers.get(k)}
        print(f"| {m} | {d.get('item_count', 0)} | {', '.join(new) or 'nothing new'} | " + "; ".join(f"{k}: {', '.join(v)}" for k, v in list(cov.items())[:6]) + " |")
    print("\n## Hubs (mods other mods build support for)\n")
    hubs = sorted(((len(v), k) for k, v in supported.items() if k not in STD and k in mods), reverse=True)[:15]
    print("| Mod | Supported by |\n|---|---|")
    for n, k in hubs:
        print(f"| {k} | {n} |")
    print("\n## Capability overlaps (who provides what)\n")
    print("A power capability (make power by fuel and type, store it, move it), from machines, multiblocks, gadgets and storage (any count).\n")
    print("| Capability | Mods |\n|---|---|")
    for k, v in sorted(providers.items(), key=lambda kv: -len(kv[1])):
        if len(v) >= 3:
            print(f"| {k} | " + ", ".join(f"{m} ({n})" for m, n in sorted(v.items(), key=lambda x: -x[1])[:8]) + " |")


if __name__ == "__main__":
    main()
