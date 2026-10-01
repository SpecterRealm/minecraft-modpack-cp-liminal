# Reachability check

`scripts/series-reach.py` answers "from this pack's starting resources, can the player make X?" using the recipe dump (`docs/recipe_data.json`).

```bash
python3 scripts/series-reach.py check docs/series/items/reach/verdant.json     # all targets in targets.json
python3 scripts/series-reach.py why docs/series/items/reach/verdant.json minecraft:iron_ingot
python3 scripts/series-reach.py blocked docs/series/items/reach/verdant.json minecraft:netherite_ingot
python3 scripts/series-reach.py tags docs/series/items/reach/verdant.json      # tags nothing resolves
```

| File | What |
|---|---|
| `verdant.json` | Start set for Verdant: surface world, no ore generation, Ex Deorum sieve. Hand-written; edit it to test another start |
| `targets.json` | The items the packs must be able to get (gear tiers, Powah, Silent Gear alloys, AE2 and Create starts) |

## What it models, and what it does not

- Recipes in the dump whose ingredients could be read. Recipes with no readable item ingredient (fluid-only casting, loot, worldgen, mob drops, villager trades) are not routes: put those sources in the start file.
- The Ex Deorum sieve counts its mesh as an ingredient. Sieve chances, machines, fuel, power and fluids are not modelled: this answers "is there a route", not "how fast".
- A recipe's own result used as an ingredient is a catalyst (Theurgy's reformation target); `--strict` turns that off.
- Recipes marked `inactive` (load conditions not met in this pack) are ignored. Block-state ingredients (Cobblegen Galore) count as items; water and lava are treated as world sources. Fluids made by melting (Productive Metalworks casting) are **not** modelled yet, so metals that only come through casting show as no route.
- Tags come from the mods' tag files, the Minecraft jar and the NeoForge jar when the dump has them, otherwise from name rules. `tags` lists the ones nothing resolves.
- The dump must include vanilla recipes. Dumps made before this change had none (only mod jars were scanned), so a furnace or a stick showed as missing. Re-run `make recipe-sync` first.

## Reading the first run (old dump, before the extraction change)

Treat it as a test of the tool, not as a finding: 19 of the 28 targets were reachable and the rest were blocked by missing vanilla recipes, unread tags and fluid-only recipes. The one real signal: **diamond, iron, gold and copper have sieve routes from gravel, sand and dirt** in Ex Deorum, which matches Verdant's design. Re-run on a fresh dump before using any "no route" result.
