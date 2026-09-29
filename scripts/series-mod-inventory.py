#!/usr/bin/env python3
"""Generate docs/series/mod-inventory.md from the four Colony Protocol pack repos.

Reads mods/*.pw.toml in each sibling repo (verdant, elysian, influx, liminal) and groups every
mod by which packs ship it. The `mods/` folders are the source of truth; this file is derived.

Usage (from the liminal repo root, with the other repos cloned alongside it):
    python3 scripts/series-mod-inventory.py [--root ..]  > docs/series/mod-inventory.md
"""
import argparse, collections, glob, os, re, sys, datetime

PACKS = {'V': 'verdant', 'E': 'elysian', 'I': 'influx', 'L': 'liminal'}
ORDER = 'VEIL'

# Ids known to be libraries / dependencies (not player-facing). Extend as the audit proceeds.
LIBS = {
    'architectury-api', 'balm', 'bookshelf', 'cloth-config', 'curios', 'jamlib', 'konkrete', 'kotlin-for-forge',
    'libipn', 'melody', 'rhino', 'searchables', 'selene', 'silent-lib', 'simple-custom-early-loading',
    'supermartijn642s-config-lib', 'supermartijn642s-core-lib', 'txnilib', 'sophisticated-core', 'ftb-library-forge',
    'geckolib', 'glitchcore', 'placebo', 'titanium', 'cucumber', 'libx', 'atlas-api', 'codechicken-lib', 'cb-multipart',
    'smartbrainlib', 'playeranimator', 'irons-lib', 'myotus-lib', 'zerocore', 'cristel-lib', 'lithostitched',
    'brandons-core', 'terrablender', 'prickle',
}
CLIENT_PERF = {'sodium', 'iris', 'modernfix', 'ferritecore', 'entityculling', 'more-overlays-updated'}

def parse(path):
    t = open(path, encoding='utf-8').read()
    def g(pat):
        m = re.search(pat, t, re.M); return m.group(1) if m else None
    name = g(r'^name = "(.*)"') or os.path.basename(path)[:-8]
    side = g(r'^side = "(.*)"') or '?'
    src = 'CF' if '[update.curseforge]' in t else ('MR' if '[update.modrinth]' in t else '?')
    return name, side, src

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--root', default='..'); a = ap.parse_args()
    mods = collections.defaultdict(lambda: {'name': None, 'packs': set(), 'side': set(), 'src': set()})
    for k, r in PACKS.items():
        for f in sorted(glob.glob(os.path.join(a.root, f'minecraft-modpack-cp-{r}', 'mods', '*.pw.toml'))):
            i = os.path.basename(f)[:-8]; n, s, c = parse(f)
            m = mods[i]; m['name'] = m['name'] or n; m['packs'].add(k); m['side'].add(s); m['src'].add(c)
    if not mods: sys.exit('no mods found — check --root')
    groups = collections.defaultdict(list)
    for i, m in mods.items():
        groups[''.join(c for c in ORDER if c in m['packs'])].append((i, m))
    def cat(i, m):
        if i in LIBS: return 'library'
        if i in CLIENT_PERF or m['side'] == {'client'}: return 'client / perf'
        return ''
    titles = {
        'VEIL': 'Shared core — in all four packs',
        'VEL': 'Verdant + Elysian + Liminal (not Influx)', 'VIL': 'Verdant + Influx + Liminal (not Elysian)',
        'EIL': 'Elysian + Influx + Liminal (not Verdant)',
        'VL': 'Verdant-owned (also in Liminal)', 'EL': 'Elysian-owned (also in Liminal)',
        'IL': 'Influx-owned (also in Liminal)', 'L': 'Liminal-only',
    }
    counts = {p: sum(1 for m in mods.values() if p in m['packs']) for p in ORDER}
    print('# Mod inventory\n')
    print('> **Generated** by `scripts/series-mod-inventory.py` on %s from the `mods/` folders of all four repos. Do not edit the tables by hand — edit the *Decision* notes in [`mod-audit.md`](mod-audit.md) or rerun the script.\n' % datetime.date.today())
    print('Pack totals: ' + ' · '.join(f'**{p}** {counts[p]}' for p in ORDER) + f' · **unique** {len(mods)}\n')
    print('Category is filled only where obvious (library, client / perf). Blank means "not yet classified" — that is the audit work list.\n')
    print('Columns: **Side** = packwiz side (both / client). **Src** = where the pin comes from (CF = CurseForge, MR = Modrinth).\n')
    for g in ['VEIL', 'VL', 'EL', 'IL', 'L', 'VEL', 'VIL', 'EIL']:
        if g not in groups: continue
        rows = sorted(groups[g], key=lambda x: x[1]['name'].lower())
        print(f'## {titles[g]} ({len(rows)})\n')
        print('| Mod | Id | Side | Src | Category |'); print('|---|---|---|---|---|')
        for i, m in rows:
            print(f"| {m['name']} | `{i}` | {'/'.join(sorted(m['side']))} | {'/'.join(sorted(m['src']))} | {cat(i, m)} |")
        print()

if __name__ == '__main__':
    main()
