# Item catalog

Goal: one comparable list of what every mod adds, so we can see **gaps** (what the series lacks) and **overlaps** (several mods adding the same kind of item), and decide which is worth keeping. Examples: the generators from Mekanism, Powah, AE2, Create and the others; every mod that adds a sword or wrench; every mod that adds a storage block.

This is not a wish list. Each entry records what the item does, its numbers, what it needs, and **how it can be changed** (config, data map, recipe, KubeJS), so "could we make it scale better" has an answer.

## Layout

| Path | What |
|---|---|
| `data/<mod>.json` | One file per mod: pin, source, tuning levers, items |
| `sources.json` / [`sources.md`](sources.md) | Where each mod's source lives and which ref matches our pin (the running list) |
| `../../../scripts/series-mod-sources.py` | `check` verifies repos with `git ls-remote`; `report` writes `sources.md` |
| `../../../scripts/series-mod-compat.py` | Scans a cloned source for built-in support for other pack mods |
| `../../../scripts/series-mod-scan.py` | `run` clones each mod (shallow, at its ref), writes `scan/<mod>.json` (item list + pack-mod support); `report` writes `compat.md` |
| `scan/<mod>.json` | Generated item list (from lang files) and built-in support found in source. Raw input for the catalog; not hand-edited |
| `compat.md` | Generated: per-mod item count and supported mods, plus which mods other mods build support for |
| `tags.md` | Tag vocabulary (facets), multiblock scaling notes, the three passes |
| `../../../scripts/series-item-tags.py` | `check [--missing]`, `find facet:value ...` |
| `yields/<mod>.json` | What resources a mod can produce, how, and whether it is a bootstrap or scale route |
| `../../../scripts/series-yields.py` | `report <resource>`, `resources`, `mods` |
| `review/<mod>.json` | Per-mod loop-back corrections (see `series-item-review.py`) |
| `profiles.json` / `mod-profiles.md` | Mod-level profile (feel, main add, gap, fit per pack) and its generated tables; input to go/no-go. `../../../scripts/series-profiles.py` |
| `capstones-and-gear.md` | Why each pack is played (capstone) and the rule that every gear item needs a job, with Silent Gear data |
| `required-resources.md` | What each pack must be able to get (gear tiers, crops, machines) and the bootstrap versus scale routes per pack; Ex Deorum manual-only as the fallback |
| `elysian-review.md` | Elysian's partial-fit mods reviewed one by one, with the spell-system count the Wizards decision raises |
| `verdant-review.md` | Verdant's partial-fit mods reviewed one by one, with usage in quests and KubeJS |
| `influx-review.md` | Influx's partial-fit mods reviewed one by one; Powah is its generator |
| `gap-check.md` | Check after the 2026-10-01 removals: new gaps introduced, gaps still open, stage coverage |
| `rpg-classes.md` | RPG class mods: the chosen ones, five candidate add-ons (Berserker, Bard, Forcemaster, Witcher, Elemental Wizards), their library chain and fit |
| `candidates.md` | Discovery pass: mods not in any pack that answer a need, with scan evidence |
| `cleanup.md` | Generated cleanup candidates (unused libraries, KubeJS add-ons, power overlaps, out-of-theme items, named-item clusters); `../../../scripts/series-cleanup.py` |
| `cleanup-findings.md` | Hand-written first reading of the cleanup data, with proposals |
| `review-process.md` | The per-mod review procedure |
| `../../../scripts/series-item-catalog.py` | `list`, `report --category <c>`, `levers --mod <m>` |

The step-by-step review (source, item list, numbers, built-in compat with other mods, game check, decision) is in [`review-process.md`](review-process.md).

## How a mod gets catalogued

1. **Find the source** and check out the tag that matches our pin (public mods can be cloned; the file name in `mods/<mod>.pw.toml` gives the version). Read from the source, not the jar, when the source exists.
2. **Item list**: `src/main/resources/assets/<modid>/lang/en_us.json` lists every block and item name.
3. **Numbers**: the config class and its defaults (NeoForge `ModConfigSpec` or Cloth AutoConfig), plus generated data in `src/generated/resources/data/<modid>/` (recipes, data maps, tags, loot).
4. **Behavior**: the block or tile classes for anything the numbers do not explain (for example: what a generator burns, what limits output).
5. **Docs the author wrote**: a `guidebook/` folder or wiki lists the items the author wants players to notice.
6. Write `data/<mod>.json`, then run the report to compare with other mods.

Mark anything not verified in-game as such (`unverified` field). Numbers come from source defaults; the shipped config in a pack can override them.

## Entry fields

- `tags`: list of `facet:value` from [`tags.md`](tags.md); multiblocks also carry a `scaling` block
- Top-level `compat`: list of `{mod, kind, what, weight}` for built-in support for other pack mods
- `id`, `name`, `category`, `subcategory`, `tiers`
- `stats`: named arrays aligned to `tiers` (`output_fe_t`, `capacity_fe`, `transfer_fe_t`, more as needed)
- `input`: what it consumes or needs; `needs_ore`, `needs_power_to_start`
- `starter_recipe` / `obtain`: how a player first makes or finds it
- `tunable`: which of `config`, `datamap`, `recipe`, `kubejs` can change it
- `notes`: forgotten-item candidates (useful items players rarely discover), overlaps, tests

Categories in use: `generator`, `energy-storage`, `energy-transfer`, `crafting-station`, `tool`, `consumable`, `utility`. Add more as needed (weapons, armor, storage, automation, food).

## Tuning levers (the "before KubeJS" question)

Order to reach for, cheapest first:

1. **Config**: numbers the mod exposes (for example Powah's per-tier generation, capacity and transfer). No script, and easy to explain to players.
2. **Data maps and datapack files**: NeoForge data maps and generated data (Powah's magmator fuels, heat sources and coolants are data maps). Can be edited in a datapack or with KubeJS.
3. **KubeJS**: recipes, tags, loot, and mod-specific addon hooks, for anything the first two cannot change.

## Source coverage

`sources.md` is the running list of which mods have public source we can read, at which ref, and which do not. Refresh it with `python3 scripts/series-mod-sources.py check --root ..` then `report`. Mods with no public source (or closed source) can only be catalogued from the jar or the game.

## Status

| Mod | Catalogued | Notes |
|---|---|---|
| Mekanism Generators, Create Additions, Extreme Reactors | Generators, storage, transfer, compat | See `findings-generators.md` |
| Powah! | Partly (generators, storage, transfer, key tools) | Pilot; item list from `lang/en_us.json` still to be fully merged |
