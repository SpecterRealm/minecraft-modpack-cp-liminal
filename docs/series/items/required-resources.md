# Required resources: what each pack must be able to get, and how

Purpose: before adding any mod, list what the player **needs** (gear tiers, machines, crops) and check each pack has a route for it. Only then decide what to add. Method: start from the class mods and Silent Gear, list every input, then read each pack's routes from `yields/` (`series-yields.py`).

Two route kinds, from the `stage` field in `yields/`:
- **bootstrap**: gets the first units with no prior materials (manual, early).
- **scale**: repeatable or automatable once the player already has some materials.

## 1. Inputs needed so far (first pass)

Read from the recipe data of the chosen mods (see `capstones-and-gear.md`, section 4):

| Input | Needed by |
|---|---|
| Iron, gold, diamond ingots/gems | All class mods base tiers; Silent Gear |
| Leather, string, wool, rabbit hide, chain, stick | Archers, Rogues, Paladins armor and weapons |
| Lapis, prismarine shard | Wizards |
| Netherite ingot, netherite upgrade template | Top tier of every class mod |
| Ender pearl, blaze powder, ghast tear | Wizards, Paladins upper tiers |
| Silent Gear alloys (crimson iron, azure silver, tyrian steel, bort) | Silent Gear tiers (need Metalworks routes) |

Not done yet: a full Silent Gear material pass, machine and crop inputs, and the animal drops (leather, wool, string need live animals and spiders in a void start).

## 2. Routes per pack (from `yields/`)

| Resource | Verdant | Elysian | Influx |
|---|---|---|---|
| Iron | **bootstrap**: Ex Deorum. Scale: Create, Mekanism | scale only: Mystical Agriculture (seed needs an iron ingot), Occultism miner spirit, Theurgy (needs ore first) | scale only: ProjectE, Replication, Productive Bees, HNN |
| Gold | **bootstrap**: Ex Deorum. Scale: Create, Mekanism | scale only: Mystical Agriculture | scale only: Productive Bees |
| Copper | **bootstrap**: Ex Deorum | scale only: Mystical Agriculture | scale only: AgriCraft, Productive Bees |
| Diamond | (no route listed) | scale only: Mystical Agriculture | scale only: Productive Bees |
| Netherite | (Ex Deorum mesh sieve, recipes read) | scale only: Mystical Agriculture (seed needs an ingot) | scale only: Productive Bees |
| Coal, redstone, lapis, obsidian, prismarine, quartz, sulfur | not in `yields/` for Verdant | Mystical Agriculture | Productive Bees |

### What this shows

- **Only Verdant has a bootstrap route.** Elysian and Influx list only "scale" routes; every one of them needs the player to already hold the material or an ore. That is the gap.
- Elysian's Mystical Agriculture seeds need the material itself (iron seed needs an iron ingot). Occultism's miner spirit and Theurgy could start a loop, but each needs an input that has to come from somewhere; not yet checked.
- Influx's routes start from EMC, scanned matter or bees; ProjectE and Replication need an item to seed them.

## 3. Precedent already in Verdant

Verdant's KubeJS already closes Nether and End gaps with Ex Deorum sieve recipes plus data, instead of adding mods:
- `blazing_path.js`: blaze powder from gravel with a diamond or netherite mesh (Ex Deorum sieve recipes in `kubejs/data`), then magma cream from a Mob Grinding Utils farm for the sustained route.
- `shulker_shell_progression.js`: shulker shell from crushed end stone, then Create or Mekanism.
- `manual_recovery_recipes.js`: recovery crafts for lost quest-reward items, so nothing blocks the player.

The same pattern can serve the class-mod netherite tiers, and is the model for Elysian and Influx gaps.

## 4. Decision direction (maintainer)

- **Ex Deorum as the manual kickstart fallback for every pack**, with the automated parts removed: no Mechanical Sieve, no Mechanical Hammer, no powered crushing. What stays is the manual sieve, barrel, crucible and hand hammer. The player can start, then has to ask how to automate it, which pushes them to the pack's own systems (magical crops in Elysian, conversion in Influx).
- **Use it as a fallback, not a first choice.** First look at what each pack's own mods can do; only then fall back.
- **KubeJS for true one-offs.** When only a recipe is missing, write a meaningful recipe with a real cost instead of adding a mod for one or two items. A mod earns its place by adding much more than the items we need from it (not "one of 27").
- Overturns the `pack-architecture.md` line "Elysian: no sieve loop" if chosen; the edit is deliberate and comes after the required list is complete.

## 5. Next

1. Finish the input list (full Silent Gear pass, machines, animal drops).
2. For Elysian and Influx, list each input with its bootstrap route from the pack's own mods first (Occultism, Theurgy, Ars, ProjectE, Replication, HNN, the Genetics egg path).
3. Whatever is left: Ex Deorum manual-only, or a KubeJS recipe.
