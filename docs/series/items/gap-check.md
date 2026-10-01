# Gap check after the 2026-10-01 removals

Question: after the removals (Wooden Shears, Better Fusion Reactor, Mekanism Tools, Extreme Reactors with its Create compat and ZeroCore, Farming for Blockheads, Productive Farming, and six Elysian mods) and the Powah swap in Influx, did we leave gaps or add new ones? This treats the open removal PRs as applied: Verdant #340, Elysian #39 and Liminal #77 (Influx #40 is a CHANGELOG line only).

## What was checked, and the result

| Check | Result |
|---|---|
| Mod counts after the removals | Verdant 120, Elysian 120, Influx 97, Liminal 199 (from 124, 121, 97, 204 before the open PRs) |
| Remaining mods that **require** a removed mod | None. The only references are soft: KubeJS Tweaks, Botany Pots, Productive Bees, Productive Trees and Mystical Agriculture carry optional data or compat for Extreme Reactors, Farming for Blockheads or Productive Farming, which simply goes unused |
| Verdant quest book integrity (after #340) | 295 quests, no dependency points at a missing quest, every quest has a title; the Mekanism fission hex now follows the quest before the removed reactor quest |
| Quest, KubeJS or config references in Elysian, Influx, Liminal | None found for any removed mod |
| Series docs still naming removed mods | `pack-architecture.md` (the series source of truth) still listed Extreme Reactors, Mekanism Tools and Productive Farming. **Fixed in this PR** |

## New gaps this round introduced

| # | Pack | Gap | Why | Suggested fix |
|---|---|---|---|---|
| 1 | Elysian | **No animal husbandry** | Farming for Blockheads (Chicken Nest, Feeding Trough) was the only mod there for it. The Elysian class armor needs leather, wool and string, and Mystical Agriculture's pig, cow and sheep crops need soul jars. In a void start nothing yet supplies the first animals | One of: spawn eggs as a quest reward or KubeJS recipe (the same egg idea as Influx), Mystical Agriculture's mob crops, or a small animal source. Decide with the first-soul question below |
| 2 | Verdant | **Powah has no teaching** | Powah is in the pack (pinned for a mid-game power test) but no quest, script or Field Manual page mentions it; the Scale chapter's only generator quests are now Mekanism's | Add a Powah quest and gate in the Scale chapter when the quest book is built (the quest book waits for locked mods) |
| 3 | Verdant | **Scale chapter lost its Extreme Reactors mainline** | The reactor then turbine path and the optional wrench quest are gone; the chapter has the Mekanism fission hex but no second power path | Same as #2: Powah as the second path |
| 4 | All | **Balm is now unused** | The only known dependent was Farming for Blockheads. Sophisticated Core only touches Balm in one optional trash-slot compat file. No other scanned mod requires it | Remove Balm from all four packs after confirming in game (a hard requirement we did not scan would show as a missing-dependency crash) |
| 5 | Influx | **Powah's first generator depends on the salvage crates** | Starter Furnator needs paste (coal, clay, lava or blaze powder), a capacitor and casing (iron, redstone) and a furnace. Nothing delivers those yet; coal supply is also open (Productive Bees or ProjectE are scale routes only) | Author the crate list (draft in `required-resources.md`, section 3c) |
| 6 | Influx | **Powah's top tier needs a nether star** | Nitro crystal needs one, and the Reactor tier needs uraninite ore. The earlier Extreme Reactors problem (ore fuel) moved rather than vanished | Stop the pack at Spirited, give the Wither route a decision, or skip the Reactor tier |

## Gaps that were already open and are unchanged

| Pack | Gap | Where tracked |
|---|---|---|
| Elysian | First iesnium ingot (Nether ore) and first iron ingot for Occultism's first miner ritual; first blaze, ghast and enderman souls for Mystical Agriculture; Nether items for the nether agglomeratio | `required-resources.md` section 3b |
| Elysian | `pack-architecture.md` still says "no sieve loop"; the fallback idea (Ex Deorum manual-only) would change it | `required-resources.md` section 4 |
| Verdant | **No turret or sentry for "automated defenses"**: the scans found only Mekanism's Laser and Robit and Mob Grinding Utils' Iron Spikes. The megabuild capstone calls for defenses the player builds | New: needs a gap search (what builds defenses from Create or Mekanism?) |
| Verdant | Early-leaf recipe is untested; Tough As Nails fit with the "calm teacher" idea is a flag | `verdant-review.md` |
| Influx | Productive Trees: space question; egg and spawner recipes not written; crate list not written | `influx-review.md`, `capstones-and-gear.md` |
| Liminal | New mobs undecided (Mowzie's Mobs and Deeper and Darker are candidates) | `rpg-classes.md`, `capstones-and-gear.md` |
| All | **Decided but not in any pack yet**: Spell Engine and the class mods (Archers to Verdant; Wizards and Rogues & Warriors to Elysian; Paladins & Priests and Bard to Influx), the cosmetic armor mod (all packs), Genetics: Resequenced and Mutant Monsters (Influx) | `capstones-and-gear.md`, `rpg-classes.md` |
| Repos | Useful ProjectE, Applied Create, Applied KubeJS, Iron's Lib, Inventory Profiles Next (Codeberg blocked), the Liminal structure mods, NoCubes Sea Dwellers | `sources.json` |

## Stage coverage (mods per progression stage, excluding libraries, QoL and integration)

Counts are from the profile stage field, so they only show where stages thin out, not whether the mods work.

| Stage | Verdant | Elysian | Influx |
|---|---|---|---|
| 0 start | 2 (was 3) | 2 (was 3) | 1, thin |
| 1 gather by hand | 5 | 4 | 2 |
| 2 store and sort | 5 | 2 | 3 |
| 3 automate gathering | 7 (was 8) | 6 (was 7) | 8 |
| 4 automate processing | 10 | 6 | 7 |
| 5 scale loop | 12 (was 13) | 4 | 8 |
| 6 capstone | 3 | 10 | 1, thin (Genetics and Mutant Monsters are decided but not added) |

Nothing dropped to zero. The Influx capstone and start are the thin spots, and both are known and tracked above.

## Verdict

- **Removing the mods did not break anything that is built**: no hard dependency, no dangling quest, no stale item in a script.
- **It did create gaps 1 to 6.** Gap 1 (Elysian animals) and gaps 2 and 3 (Verdant power teaching) are the ones with real content cost; 4 is a cleanup.
- **The biggest open risk is not from the removals**: it is the set of decisions that are made but not yet in any pack (classes, cosmetic armor, Genetics, Mutant Monsters), plus Verdant's missing automated-defense mod.

## Suggested next actions

1. Decide gap 1 (Elysian animals) together with the first-soul question.
2. Remove Balm after one in-game launch check.
3. Search for defense options for the Verdant megabuild (named gap: automated defenses built from Create or Mekanism).
4. Add the decided mods (Spell Engine and classes, cosmetic armor, Genetics: Resequenced, Mutant Monsters) to their packs, since the gaps above depend on them.
5. Author Influx's crate list.
