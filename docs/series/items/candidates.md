# Mods we do not have yet: first discovery pass

The packs were built on guesses, so this pass looks outside them for mods that answer a *need* better. Need first, then feel, then mod. The pool comes from All the Mods 10 (a 1.21.1 NeoForge kitchen-sink pack; its config and script names list roughly 100 mods we do not carry) plus mods the maintainers already knew. Each was scanned from public source like the pack mods (`scan/<mod>.json`, profile in `profiles.json`). Closed or unreachable sources (Productive Frogs, Hexerei, Quarry Plus, Create Ore Excavation) are not scanned; look at them in the game.

**Nothing here is a recommendation to add.** These are leads worth a deeper look, and each has to earn its place like any current mod. Adding a mod is a real cost: new items, new recipes, new quests, and overlap with what we have.

## Elysian: automation and resources without FE

Elysian needs farming, wood, ore and item moving with no tech power. The current answers are Botany Pots hoppers, Occultism foliots, Ars Nouveau familiars and Theurgy logistics. Leads:

| Lead | Feel | What it would answer | What the data shows | Works with our mods |
|---|---|---|---|---|
| **Botania** | nature + magic | Farming, wood and **ore with no power**: mana flowers do the work | Orechid and Orechid Ignem turn stone into ore; Pure Daisy makes living wood and rock; Agricarnation, Hopperhock and Rannuncarpus farm and move items; it ships a void start ("Garden of Glass"). Mana, not FE. | AE2, Occultism, Productive Bees |
| **Nature's Aura** | nature + magic | Aura-powered farming and crafting | Field creator (farming), auto crafter, item distributor, placer, animal spawner; generators that turn items into aura; RF converter if wanted. About 150 items. | none found |
| **Modular Routers** | neutral | Item routing with no power | Small routers with modules (extract, sort, place, filter); no pipes or FE | FTB filter |
| Blood Magic (Neovitae) | magic | Automation and content through rituals | Life-essence network, altars, sigils; complex | none found |
| Forbidden Arcanus, Eidolon, EvilCraft, Roots, Malum | magic | Content and gear, not a need | Mostly content; **Malum** supports Create, Farmer's Delight, Iron's Spells, Occultism and Twilight Forest, the widest integration here | see profiles |

Why it matters: Botania answers Elysian's three open needs (farming, wood, ore) in one nature-magic mod, with no power, and with the void start already in it. `pack-architecture.md` says Botania is not a pillar, so this reopens a decision; the maintainers should make that call.

## Verdant: a steampunk power and machine layer next to Create

| Lead | Feel | What the data shows | Works with our mods |
|---|---|---|---|
| **PneumaticCraft: Repressurized** | steampunk + tech | Power is **air pressure**, not FE: compressors, pressure tubes, assembly line, pressure chamber, heat system, plastic, drones. FE conversion exists. | Create, Mekanism, Occultism, Powah |
| Immersive Engineering | steampunk + tech | Dynamo, generators, windmill, wires, capacitors, excavator, crusher, arc furnace. About 150 real items (the rest are decor). Its ores would come from sieving. | none found |
| Actually Additions, Just Dire Things, Industrial Foregoing | tech | Machine sets on FE; overlap Mekanism and Create | Actually Additions supports Mekanism and Powah |
| Refined Storage 2 | tech | The alternative to AE2; replacing AE2 means replacing 41 add-ons | none found |

PneumaticCraft is the notable one: a second power system that fits Create's feel and works with our mods, where Immersive Engineering brings a third FE system.

## Influx: compact, closed loops

| Lead | Feel | What the data shows |
|---|---|---|
| **Compact Machines** | sci-fi | Pocket rooms inside a block: build inward, which is the space lesson. The scan found no lang items, so check in game. |
| Functional Storage | neutral | Dense drawer storage; overlaps Sophisticated Storage |
| Integrated Dynamics | tech | Programmed logistics; heavy |

## Liminal

| Lead | What the data shows |
|---|---|
| **MineColonies** | The colony mod the architecture names for Liminal. Scan found no lang items; check in game. |
| Waystones | Colony travel QoL |
| Supplementaries | Decor and small gadgets; wide integration with our mods (Ars Nouveau, Create, Farmer's Delight, Twilight Forest) |

## Mods we looked at and what they would not add

- **Ender IO, RFTools Power:** nothing new in power capability (see `cleanup.md`).
- **Thermal Expansion:** FE machines and dynamos; overlaps Mekanism and Powah. The scan found no items (check in game).
- **Create: Steam 'n' Rails:** trains, content not resources.

## Next

1. Pick two or three leads per pack and read them as closely as the pack mods (item list, power, what they need, how they scale). Botania, Nature's Aura, PneumaticCraft and Modular Routers first.
2. Check the ones the scan could not read (Compact Machines, MineColonies, Thermal) in the game.
3. Then compare each lead against the Elysian needs table before any go/no-go.
