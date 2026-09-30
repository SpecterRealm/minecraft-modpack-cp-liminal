# How to review a mod for the pack

Used for every mod, in any order. The goal is the full item list plus an honest answer to "does this earn its place, and what does it overlap?" Mods add things that are out of theme, so nothing is assumed from the mod's description.

## 1. Get the source (public repo first)

- Look the mod up in [`sources.md`](sources.md). If it has a repo and a matching ref, clone it at that ref (`git clone --depth 1 --branch <ref> <repo>`).
- No repo, closed source, or no clear ref: go to step 5 (load the game).

## 2. Pull the item list from source

- `assets/<modid>/lang/en_us.json`: every block, item, entity, and fluid name. Often under `src/generated/resources` or `src/main/resources`.
- Drop the noise (tooltips, config screen text, advancements) and keep blocks and items.
- Note the things that do not fit the pack theme (for packs 1 to 3: no ore, no Nether/End, no void start). These are hide/uncraftable candidates.

## 3. Numbers and tuning levers

- Config class defaults, then generated data (`data/<modid>`): recipes, data maps, tags, loot.
- Record which levers can change each item: config, data map or datapack, KubeJS (see README).
- Mark `unverified` on anything not read from a running game.

## 4. Built-in support for other mods

If the author wrote code or data for another mod, the two were meant to work together. That weights the pairing in favor of keeping both, and weighs against a rival that has no integration.

Run:

```
python3 scripts/series-mod-compat.py <source-dir> --self <modid> [...] --root ..
```

It reports which **pack** mods the source touches, and how:

| Evidence | Meaning |
|---|---|
| `dependency` | Listed in `neoforge.mods.toml` (optional or required) |
| `isLoaded` | Code path switched on when the other mod is present |
| `mod_loaded` | Data guarded by a `neoforge:conditions` mod check |
| `compat-import` | Java in a `compat`/`integration` package uses the other mod's API |
| `data-ref` | Recipes, tags or loot that name another mod's items |

Read the hits before trusting them: `data-ref` can be as small as one tag entry (for example Extreme Reactors lists Powah's dry ice in a tag). Record the useful ones in the mod's `compat` field (see below) with a one-line note on what the support does.

Standard integrations (JEI, EMI, Jade, Patchouli, Curios) are expected and carry little weight. Weight the rest: a storage or energy mod with FE support for Flux Networks, or a machine mod with AE2 or Create recipes, matters.

## 5. Load the game when source is not enough

Do this when the mod has no public source, no clear ref, or the item list looks like it might be a fit and needs proof:

- Pull the item list from the game (registry dump, or the EMI/JEI export); record it as `unverified: false` only for what you actually saw.
- Confirm defaults in the shipped config file, not just the source defaults.
- Check recipes in the viewer, because KubeJS and datapacks in the pack change them.

## 6. Write the catalog entry

`data/<mod>.json` with: `mod`, `name`, `version_pinned`, `source`, `tuning`, `compat`, `items`. Use the category names in the README so the overlap report can compare mods.

`compat` entries look like:

```json
"compat": [
  {"mod": "applied-energistics-2", "kind": "data-ref", "what": "Mekanism ships AE2 recipes/tags", "weight": "medium"}
]
```

## 6b. Record what it yields (progression paths)

For any mod that produces a resource (crops, bees, sieves, machines), write `yields/<mod>.json` so we can answer "how do I get my first iron, and how do I scale it up". Each entry has a `resource`, the `form` (chunk, essence, comb), the `source`, its `power`, a `stage` (`bootstrap` for the first way to get it, `scale` for the ways to get more), and a `note`. Item lists alone cannot show this: in data-driven mods (Productive Bees, Mystical Agriculture, Botany Pots) the crops and species are defined in data or Java, so read those. Then `python3 scripts/series-yields.py report iron` lists every source with the packs that carry it. A mod with no yields still gets a file with a `note`, so we know it was checked.

## 7. Decide

Run `python3 scripts/series-item-catalog.py report --category <c>` for overlaps. For each overlap group, prefer:

1. The mod with built-in support for mods we already keep.
2. The one that can be tuned (config or data map) into a tier rather than a duplicate.
3. The one that fits the pack's story and progression.

Record the call in [`../mod-audit.md`](../mod-audit.md).

## 8. Clean up

After a mod is catalogued and classed, run `python3 scripts/series-cleanup.py --root .. > docs/series/items/cleanup.md`. It flags libraries nothing uses, KubeJS add-ons no script uses, power capabilities another mod already covers, and content mods with no support to or from any other mod, and lists out-of-theme items for the hide lists. Candidate mods we did not add (Ender IO, RFTools Power) are scanned the same way and compared against what the packs already provide. Read the flags in [`cleanup-findings.md`](cleanup-findings.md) and record decisions in the mod audit.
