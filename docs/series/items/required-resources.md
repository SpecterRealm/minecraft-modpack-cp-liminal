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

### Sources found later (maintainer-supplied repos, scanned)

- **Cobblegen Galore** (`JDKDigital/cobblegengalore`, dev-1.21.1): 7 block generators from stone to netherite tier, but the metal tiers are **speed upgrades, not metal producers**. Its `blockgen` recipes list stone types, **netherrack, obsidian and basalt**, so a pack can get netherrack without the Nether. That covers part of the nether agglomeratio (Mystical Agriculture) and crushed netherrack (Ex Deorum). Verdant already gates the chain with `cobblegen_chain.js`.
- **Silent Gear Metalworks** (`JDKDigital/sgearmetalworks`, dev-1.21.1, 94 fluid items) and **Productive Metalworks** (`JDKDigital/productivemetalworks`, dev-1.21.1, 202 items: foundry, casting, fire bricks) give casting for Silent Gear's gem and alloy materials. Built-in support covers Create, Mekanism, Mystical Agriculture and Productive Bees, so it fits the existing pack mods.
- **KubeJS Metalworks** (`senuko228/KubeJS-Metalworks`): scripting add-on for custom casting recipes. Candidate only.
- **Ars Mekanica** (`meigoc/Ars-Mekanica`): one block, a Source to Mekanism power bridge. Liminal's job if wanted.
- **More Thermal Evaporation** (`A8T1N/MoreThermalevaporation`, 1.21.1): Mekanism evaporation plant sizes only.
- **Extreme Reactors Create compat** (`ZeroNoRyouki/ExtremeReactors2-CreateCompat`): only a 1.20 branch exists, so there is no 1.21.1 source to scan.
- **Iron's Lib**: the link supplied is a Patreon post, not a repo; still unresolved.

## 3b. Elysian and Influx: what their own mods already bootstrap (source read)

### Elysian: Occultism is the bootstrap, with one chokepoint

Occultism (`klikli-dev/occultism`, 1.21.1 release) lets the player bind spirits that **mine a dimension** and deliver items. From its recipe data (`recipe/miner/`):

| Miner | Gives |
|---|---|
| Basic resources (foliot) | stone types, blackstone, **end stone, netherrack**, deepslate, andesite, diorite, granite, basalt, mossy stone |
| Ores (djinni) | iron, gold, copper, diamond, emerald, lapis, redstone, coal and dozens of modded ores |
| Deeps | deepslate versions of the main ores |
| Eldritch | **ancient debris**, raw iron, raw gold, raw copper, raw crimson iron, raw azure silver, quartz, rubies and other gems |
| Master | ancient debris, iesnium ore |

So Occultism alone can supply the stone types, the Nether and End blocks, every base metal, and ancient debris that the netherite tier needs. That answers most of Elysian's bootstrap questions without Ex Deorum.

**The chokepoint**: the first foliot needs a ritual with **an iron ingot and an iesnium pickaxe** (`craft_miner_foliot_unspecialized`), and the djinni needs a foliot, a gold ingot, lapis and a spirit-attuned crystal. The pickaxe is made from **iesnium ingots**, and iesnium ore is **Nether worldgen** only (`ore_iesnium`, height 0 to 128 in Nether biomes). In a void start the first iesnium ingot cannot be found, and nothing in Elysian's quest chapters or docs mentions iesnium. This is the gap to close.

Options to close it (decide later; KubeJS fits the pattern from Verdant's `blazing_path.js`):
1. A KubeJS recipe that makes the first iesnium ingot from something the player has (for example iron plus a spirit item), with a meaningful cost.
2. A single quest reward of an iesnium pickaxe or ingot, plus a recovery recipe so a lost one never blocks.
3. Fall back to Ex Deorum manual-only for this one item (most expensive option for one item).

Also needed: **one iron ingot** for the first ritual. Elysian's quests already hand out inferium seeds and a Silent Gear pickaxe, so a starter iron ingot as a reward is in the same style.

Not yet checked: Theurgy (Elysian's other bootstrap candidate), Apothic Spawners and Gateways to Eternity drops.

### Influx: the ship design already answers the first unit

Influx's own docs set the start as a ship: "thin scrap / authored crates feed early convert", then typed matter (Replication), then genetics, then EMC as the destination (ProjectE, Replication, AutoEMC). So the first units are **authored salvage crates**, not a world resource. What is missing is the **crate contents list**: exactly which items and how many of each, sized to cover the first gear tiers and the first blaze egg. That list is the required-resource list for Influx.

Influx's quest chapters so far: Welcome, Ship Camp, Typed Matter, Genetics Lab, EMC Ladder (ProjectE, transmutation table), Spanner Workspace, Specimen Loop, Azurum Mass, AppliedE. Spanner, Specimen Loop, Azurum Mass and AppliedE are stubs. The current text steers advanced materials through AgriCraft genetics; the maintainer direction is moving genetics toward mobs and the egg, spawner, Hostile Neural Networks arc (see `capstones-and-gear.md`).

### Verdict so far

| Pack | Needs Ex Deorum? | What it needs instead |
|---|---|---|
| Verdant | already has it | (the required-resource list, for later chapters) |
| Elysian | **probably not** | Close the iesnium and first-iron chokepoint (KubeJS or a quest reward) |
| Influx | **probably not** | Author the salvage crate contents; add the egg and spawner recipes |

Ex Deorum manual-only stays the fallback if Theurgy and the crates turn out to leave gaps.

## 4. Decision direction (maintainer)

- **Ex Deorum as the manual kickstart fallback for every pack**, with the automated parts removed: no Mechanical Sieve, no Mechanical Hammer, no powered crushing. What stays is the manual sieve, barrel, crucible and hand hammer. The player can start, then has to ask how to automate it, which pushes them to the pack's own systems (magical crops in Elysian, conversion in Influx).
- **Use it as a fallback, not a first choice.** First look at what each pack's own mods can do; only then fall back.
- **KubeJS for true one-offs.** When only a recipe is missing, write a meaningful recipe with a real cost instead of adding a mod for one or two items. A mod earns its place by adding much more than the items we need from it (not "one of 27").
- Overturns the `pack-architecture.md` line "Elysian: no sieve loop" if chosen; the edit is deliberate and comes after the required list is complete.

## 5. Next

1. Finish the input list (full Silent Gear pass, machines, animal drops).
2. For Elysian and Influx, list each input with its bootstrap route from the pack's own mods first (Occultism, Theurgy, Ars, ProjectE, Replication, HNN, the Genetics egg path).
3. Whatever is left: Ex Deorum manual-only, or a KubeJS recipe.
4. Check Theurgy, Apothic Spawners and Gateways drops for Elysian; write the Influx crate contents list.
