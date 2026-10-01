# Influx: partial-fit review (first pass)

Influx's theme: **use what you have, in a closed loop; space is the scarce resource.** The player is aboard the *Longwatch*: salvage crates, typed matter (Replication), genetics, then EMC (ProjectE) as the destination. Capstone: "look what the mad scientist made today" (Genetics: Resequenced and Mutant Monsters chosen). Genetics is moving from plants toward **engineering mobs and animals** (egg, spawner, Hostile Neural Networks arc), and utility RPG classes (Paladins & Priests, Bard) are the planned armor roles.

Same method and caveat as the Elysian and Verdant reviews: leanings to argue from, not verdicts. Usage from Influx's quests, KubeJS and docs.

## Mod by mod

| Mod | Items | Used in Influx | Leaning | Why |
|---|---|---|---|---|
| Extreme Reactors (+ ZeroCore) | 146 | Docs call it the power pillar for the Azurum Miner's power lesson; no quest yet | **Keep, but the fuel route is the open problem** | Influx has **no other FE generator** (no Powah, Mekanism or Create), so cutting it leaves nothing to run Replication or the Azurum Miner. The earlier "poor fit" came from yellorium being ore-only. Yellorium needs a route from Influx's own systems. Candidate: give yellorium an EMC value with the KubeJS ProjectE add-on already in the pack, so the EMC ladder supplies fuel. Not built; not checked in game. |
| Farming for Blockheads | 12 | No references | Lean cut | Influx already carries **Animal Pens** (pens, breeding, drops) for animals, and a market is out of place on a ship. |
| Dummmmmmy | 1 | No references | Question | One item. Useful for testing mob-gene powers and class gear, but a single item. |
| Productive Farming | 494 | No references (AgriCraft has 2 quest references) | Lean cut, with a caveat | About 160 content crops. With genetics moving to mobs, one plant-genetics system is enough, and AgriCraft is the hands-on one the quests use. Caveat: Productive Farming was dropped once on thin information and restored; ticket #31 holds the comparison and is still open. |
| Productive Trees | 3,904 | No references | Question for Influx; fine for Liminal | 163 tree species give wood, fruit, sap and rubber but no metal. Trees need room, and **space is Influx's scarce resource**. The 3,900 items also swell the recipe viewer. The wood variety fits a decoration sink (stage 6), which suits Liminal better than a ship. |

## Where this leaves Influx

- **Keep**: Extreme Reactors (it is the only generation), with a yellorium route to design.
- **Lean cut**: Farming for Blockheads, Productive Farming (pending #31).
- **Question**: Productive Trees (space), Dummmmmmy (one item).
- Productive Bees, AgriCraft, Replication, ProjectE, Hostile Neural Networks, Genetics: Resequenced and Mutant Monsters are the foundation direction and were not in this pass.

Nothing is removed. Influx's quest book is mostly stubs and waits until the mods are locked.

## Decisions (maintainer)

- **Extreme Reactors swapped for Powah** in Influx (SpecterRealm/minecraft-modpack-cp-influx#39; ZeroCore goes with it). Why it works: Powah needs no ore and Influx already has its required libraries (Cloth Config, GuideME). **Open**: Powah's starter path needs a lava bucket or blaze powder (dielectric paste) and a redstone block, and its higher tiers need crystals made from diamond, emerald, blaze rod or powder and a nether star (see `required-resources.md`; an earlier draft wrongly said netherite). The salvage crate list and the egg, spawner and Hostile Neural Networks arc have to supply them. Liminal keeps both Powah and Extreme Reactors.
- **Dummmmmmy kept.**
- **Farming for Blockheads and Productive Farming removed** from Influx (still in Liminal's union, each needing a reason there). This answers the Influx question in ticket #31.
- **Productive Trees**: not decided; the space question stands.

## Next

1. Maintainer call on the leanings above.
2. Cross-pack check of the union that stays in Liminal: each cut mod needs its own reason there, or removal.
3. Required-resource list for Influx's salvage crates.
