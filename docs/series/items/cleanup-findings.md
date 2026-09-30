# Pack cleanup: first findings

Goal: a clean pack with few wasted mods. Every mod has to add a feature or fill a gap, not just fit the theme. This is a first read of the catalog; the tables behind it are generated in [`cleanup.md`](cleanup.md) (`python3 scripts/series-cleanup.py --root ..`). These are **proposals to decide**, not decisions; record decisions in [`../mod-audit.md`](../mod-audit.md).

> **Read this as early observations, not decisions.** Every mod in the packs was added on a guess, without data. The go/no-go call for each mod is made per pack during the deep review, using its profile in [`mod-profiles.md`](mod-profiles.md): does it fit the pack's theme, does it fill a gap (how we obtain or process something), and what does it add (resources, power, tooling, content and so on). The flags below are where the data says to look first.

All 176 mods with readable source are catalogued and classed (library, client, QoL, AE2 add-on, compat, content, and so on). 32 mods have no public source and need a look in the game.

## 1. Power stack (Liminal #45)

Power is where the overlap is. By capability (from [`cleanup.md`](cleanup.md#capability-overlaps-who-provides-what)):

| Capability | Who provides it |
|---|---|
| Make FE from nuclear fuel | Extreme Reactors, Mekanism (fission), Powah reactor, Better Fusion Reactor, Draconic reactor |
| Make FE from solid fuel | Powah (7 tiers), Mekanism heat generator, AE2 vibration chamber, Draconic generator |
| Make FE from kinetic | Create Additions alternator, Mekanism turbine, Extreme Reactors turbine |
| Store FE | Mekanism energy cubes and induction, Powah cells, Draconic core, Create Additions accumulator, Extreme Reactors energy core |
| Move FE | AE2 cables, Powah cables, Draconic crystals, Flux Networks, Create Additions connectors, Mekanism cables |

Proposals:

- **Extreme Reactors: cut candidate (strongest case).** In Verdant and Elysian its fuel (yellorium) comes only from yellorite ore, and ore worldgen is off there, with no Ex Deorum sieve recipe for it, so it can't work. It has no built-in support for any pack mod except ZeroCore, and its nuclear, turbine and storage roles are all covered by Mekanism, Powah and Draconic. Cutting it also removes ZeroCore and the Create compat mod.
- **Better Fusion Reactor for Mekanism: cut candidate.** Release-candidate pin; overlaps every nuclear source above; needs world ore for irradiated ores.
- **Ender IO and RFTools Power: do not add.** Both are catalogued as candidates. Neither adds a power capability the packs lack (storage, transfer and generation are all covered). Ender IO's capacitor bank is the same idea as the Draconic Energy Core and Create Additions' accumulator, and its alloys would add an ore-dependent metal tier. It does integrate with AE2 and Mekanism through conduits, but that is not a gap we have.
- **Tier the rest instead of cutting it.** A workable ladder: Create Additions (stress to FE, early) then Powah (starter to mid, tiered, non-ore fuel) then Mekanism (scale) with Flux Networks for wireless transfer, and Draconic as Liminal's cap. For storage: accumulator (early), Powah cells (mid), Mekanism induction (late), Draconic core (cap). That needs a per-pack decision on which of these show in each pack.
- **Charging Gadgets:** one item, overlaps Flux Networks charging; a cut candidate unless Verdant's quests use it.
- **Elysian has no power by design** but carries FE machines: Mystical Agriculture's reprocessor, harvester, soul extractor, essence furnace and soulium spawner, plus Mystical Automation. Decide whether to hide them, or accept a small power source there. Ars Nouveau's sourcelinks are the magic generator that fits.

## 2. Mods nothing uses (use or remove)

- **KubeJS add-ons no script uses** (Ars Nouveau, Botany Pots, Iron's Spells, ProjectE, Occultism, Theurgy): six flagged in `cleanup.md`. Matches the audit's keep-for-now rule; each is removed unless a script uses it when the pack is customized.
- **Libraries nothing in the catalog depends on** (7): atlas-api, ftb-filter-system, kotlin-for-forge, resourceful-config, selene, and the SuperMartijn642 config and core libs. Libraries are often required by closed-source mods, so check each mod page before removing; the list is where to look.
- **Dev-only mods**: Skyblock Builder (structure tools; remove once Elysian and Influx structures are final) and ProjectExtendedAdvancedAE (example items only).
- **Isolated content mods** (no support to or from any other pack mod): Animal Pens, Azurum Miner, Charging Gadgets, Replication, Tough As Nails, Wooden Shears. Each stands on its own; Azurum Miner, Replication and Animal Pens are Influx pillars, Wooden Shears is already slated for removal (Verdant #331).

## 3. Big content mods to question

- **The Twilight Forest (995 items).** Adds a whole dimension; no other pack mod integrates with it (only viewers and book mods reference it). Kept "for extra things to do" in the audit; the biggest item-count cost for the least integration.
- **Draconic Evolution (188).** Endgame power and gear, Liminal only. Its energy core is the multiblock battery we wanted, so it earns a place if the power ladder uses it.
- **Apothic Enchanting and Apotheosis (Elysian).** Gear-and-loot layers with no progression yield; decide after the Elysian gear plan.

## 4. Hide and uncraftable input

`cleanup.md` lists items that need world ore, the Nether or the End in mods that ship in Verdant, Elysian or Influx. Largest: Extreme Reactors (56 ore items, which goes away if it is cut), Silent Gear (30 Nether items, mostly netherwood), Botany Pots Tiers (36, Nether and End pot variants), Ex Deorum (20, crushed Nether/End blocks and Nether wood), Productive Bees (15). This is the input for the hide-from-EMI and uncraftable lists.

## 5. Same job, different mods

From the named-item clusters in `cleanup.md`:

- **Wrenches:** AE2 (2), Create, Extreme Reactors, Powah. Morph-o-Tool is the test candidate to replace them.
- **Hammers and paxels:** Ex Deorum hammers are the sieve tools; Silent Gear, ProjectE and Mekanism paxels are gear. Not duplicates.
- **Magnets:** Sophisticated Storage and Backpacks (upgrades), Simple Magnets, Draconic, Create. Simple Magnets is decided (keep).
- **Storage:** Ex Deorum barrels (sieving), Sophisticated Storage (bulk), Mekanism bins, AE2. Tiered by design.

## What this data cannot tell us

- Yields and power numbers are mostly source defaults; Productive Bees and Replication yields, Hostile Neural Networks drops and Azurum Miner output are unverified.
- Pack membership comes from the sibling repos checked out next to this one; refresh them before relying on it.
- Closed-source mods (Productive Metalworks, Silent Gear Metalworks, Terralith, Xaero, the structure mods, Essential, Useful ProjectE, Tough As Nails Vanilla Pack) have no item list here.
- Flags are prompts. "Nothing depends on it" and "overlaps" are not reasons to cut on their own.
