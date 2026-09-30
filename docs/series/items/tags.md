# Item tag vocabulary

Every item gets several tags, written `facet:value`. An item can carry many values of a facet (a Powah reactor is `kind:multiblock`, `function:generate`, `power:makes` and `power:uses`). New values are added **here first**, then used. `scripts/series-item-tags.py check` rejects tags not listed below.

## Facets

| Facet | Values | Question |
|---|---|---|
| `kind` | weapon, armor, tool, block, machine, multiblock, storage, food, consumable, ingredient, material, decoration, transport, mob, fluid, gadget | What is it? |
| `function` | generate, store, transfer, process, craft, farm, mine, automate, defend, travel, light, cook, enchant, research | What job does it do for the player? |
| `power-role` | makes, stores, uses, transfers, none | Group 1: what it does with power (several allowed) |
| `power-type` | fe, stress, mana, source, emc, heat, chemical, none | Group 2: which kind of power (several allowed) |
| `fuel` | solid, liquid, gas, chemical-fuel, nuclear, sun, wind, water, kinetic, biomass, none | What it burns or draws from, when it makes power |
| `needs` | ore, nether, end, void-start, water, sun, spell-tech, none | What it depends on (this is where theme conflicts show) |
| `tier` | primitive, early, mid, late, endgame, n/a | Where it sits in progression (filled in during review) |
| `role` | core, optional, hidden-gem, dev-only | Carries progression, optional, an item players might miss, or dev-only |
| `fit` | fits, gated, hide, unknown | Outcome of our review (default `unknown`) |
| `review` | auto, checked | Whether a person (or a source read) confirmed the tags, or they are the keyword first pass |
| `scale` | fixed, tiered, size-scaled, count-scaled | How a bigger or better version changes output (see below) |

Notes:
- `review:auto` is set by the keyword tagger; `review:checked` means the item was read against source or the game and the tags confirmed. Loop-back work is the `review:auto` list.
- `needs:ore` means the item needs ore **in the world** (mined ore, raw ore). Ore chunks from Ex Deorum sieving are `needs:none`: sieving is how Verdant gets metal without ore.
- `power-type:source` is Ars Nouveau's Source; `mana` stays for Iron's Spells and general mana. Keep them apart so Ars and Iron's are not treated as one system.
- `power-role` and `power-type` are separate on purpose: `power-role:makes` + `power-type:fe` + `fuel:solid` is a solid-fuel FE generator. A Create Additions alternator is `makes`/`fe` with `fuel:kinetic`; an electric motor is `uses` `fe` and `makes` `stress`.
- `heat` (Thermo Generator, Mekanism Heat Generator, Blaze Burner) and `emc` (ProjectE) are power types so they show up in gap analysis.
- `fit` and `tier` start as `unknown` / `n/a` and are set during review. They are the decision layer.

## Multiblock scaling

Multiblocks carry a `scaling` block in the catalog entry, not just a tag:

```json
"scaling": {
  "model": "count-scaled",
  "driver": "fuel assemblies",
  "formula": "burn rate = assemblies x burnPerAssembly",
  "min": null, "max": "see multiblock size limit",
  "source": "FissionReactorMultiblockData.java:475"
}
```

`scale` tag values: `fixed` (one size, no scaling), `tiered` (fixed size, higher tier means more), `size-scaled` (a bigger structure directly changes output), `count-scaled` (output scales with the number of a part inside the structure, such as fuel rods, assemblies, blades).

## Passes

1. **First pass:** tag each mod's items from source (item names, config, what it consumes or produces). Items added later get the same pass.
2. **Loop-back pass:** after the first pass across a group, re-read earlier entries against any new tags or facet values added since, and fill the gaps. `scripts/series-item-tags.py check --missing` lists entries missing a facet, and a tag added to this file lists which mods to revisit.
3. **Review pass:** set `tier`, `role`, `fit`.

## Auto first pass

`scripts/series-item-autotag.py run` tags every item in `scan/<mod>.json` from its id and name (weapons, armor, tools, storage, machines, generators, batteries, cables, farm items, food, materials, decoration, plus `needs:` hints for ore, Nether, End, and spell-tech mods). It only writes power tags where the wording is clear, so power tagging stays a review job. Things to know:

- It is a keyword pass, so it over- and under-tags. Treat `auto` tags as a starting point, and hand-curated entries in `data/<mod>.json` win.
- Re-running `series-mod-scan.py run` regenerates the scan files; run the auto tagger again after it.
- `series-item-tags.py stats` shows tag counts; `find <tags> --all` searches curated and auto-tagged items together.
- The loop-back list is what the tagger could not place: items with no `kind:` tag (mostly plain items) and machines without a `power-role`.

## Review record (date and version)

Every hand-checked entry carries a `review` block so we can tell what is worth checking again:

```json
"review": {"status": "checked", "date": "2026-09-30", "mod_version": "10.7.19.85", "pass": "first", "note": ""}
```

- `date`: when it was last reviewed. `mod_version`: the version or ref the review was done against (the pinned tag or branch in `sources.json`).
- `pass`: `first`, `loop-back`, or `review`.
- Auto-tagged scan files carry file-level `tagged_on` and `tagged_version` instead; every item in them is `review:auto` until checked.
- `python3 scripts/series-item-tags.py stale` lists entries to revisit: no review record, reviewed against an older version than the current pin, or still `review:auto`. Run `series-mod-sources.py check` first so the current refs are up to date.

## Loop-back pass, per mod

Work one mod at a time, reading the whole item list (`series-item-review.py list <mod>`), then write `review/<mod>.json` with rules that correct the auto tags (see the script docstring) and run `series-item-review.py apply <mod>`. That marks every item in the mod `review:checked` and stamps the file with date, version and pass. `series-item-review.py status` shows which mods are done. Each review file also carries a short `note` (what the mod is for in the pack, and what it supports), and the rules are reproducible: re-scan, re-auto-tag, re-apply.
