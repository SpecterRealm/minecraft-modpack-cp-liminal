# Colony Protocol — Pack Architecture

What each pack **owns**, what it inherits, and where the boundaries are. Story lives in [`story.md`](story.md); this file is design and mods.

## Ownership principle

- A pack **owns** the systems it teaches: its world model, resource loop, teaching mods, KubeJS gates, and quest chapters.
- Mods and systems are **taught once, in the earliest pack that owns them.** Later packs may include the jars but do not re-teach them.
- **Liminal includes everything** (Verdant ∪ Elysian ∪ Influx) plus its own additions, and is the default home for cross-pack bridges.
- A pack's docs describe only its own slice. Series-wide statements go here.

## World models

The three teaching packs differ in *what is scarce*. That is the whole design.

| Pack | Start | What is scarce | The answer |
|------|-------|----------------|------------|
| **Verdant** | Normal overworld (Terralith). Caves and villages exist. Ore worldgen stripped. Wandering traders off. | Ore veins | **Sieve it.** Ex Deorum hammer → sieve → chunks → 2×2 ore block → smelt. |
| **Elysian** | Void / skyblock shell | Ground and materials | **Shape it.** Magic obtains what you can't mine or craft: spells, essence crops, spirit labor. No sieve loop. |
| **Influx** | Prebuilt ship in the void | **Space.** You are locked in a ship and cannot just build another floor. | **Use what you have.** Make everything from what's aboard through recycling, conversion, and breeding — tight loops, compact machines, and workspaces that open *inward*, not outward. |
| **Liminal** | A lived planet | Safety and time | **Settle and resist.** Bring whichever literacy you learned, or arrive cold. |

### Verdant — "Learn to grow what you cannot mine"

- Overworld spawn; **not** a void skyblock. Nether/End are not progression paths.
- All metal via sieving. Ore chunks do not smelt directly.
- Tech-first arc: Survive → Establish → Automate → Infrastructure → Computing → Networks → Scale → Command.
- Teaching pillars: **Create**, **Mekanism** (+ Generators/Tools), **AE2** (+ addon ecosystem), power (Extreme Reactors, Flux Networks). Storage: Sophisticated Storage.
- Verdant is also the tooling reference for the series.

### Elysian — "Learn to shape what you cannot craft"

- Void / skyblock start. Magic is the only obtain path; **no sieve loop.**
- Leans (soft-pinned, not final): Ars Nouveau + addons for spell literacy → Mystical Agriculture for bulk materials → Occultism / Theurgy for magical labor and auto-craft; Iron's Spells 'n Spellbooks for combat; Apotheosis and Gateways to Eternity for gear and challenge.
- **Botania is not a pillar.** Cobblegen Galore and Building Gadgets are excluded (tech aesthetic); Building Wands stays.
- Carries the Veil doctrine (see [`story.md`](story.md#the-veil)).

### Influx — "Use what you have to make everything"

- You live on a prebuilt ship in the void. **You are locked in.** There is no next island, no second floor, no new land to claim. The constraint is *space*, and the design question is *what do you do when you can't just expand?*
- Resources come from what's aboard and what you can recover: salvage and debris are converted to typed matter, and typed matter feeds breeding and genetics for advanced materials. Every loop is closed — outputs become inputs.
- **Pattern first, then convert.** Efficiency ladders (ProjectE-style EMC, Replication) reward having a first copy; they are not a "make anything from nothing" button. Do **not** pitch Influx as "EMC solves everything."
- Space is solved by going *in*: compact production (Productive Bees / Trees / Farming, AgriCraft), dense storage, and **AE2 Spanner** — pocket dimensions that can be used for almost anything (farms, labs, storage, machines) — rather than by building outward. Spanner is the answer to "I can't build another floor", not a second resource philosophy.
- Leans (soft-pinned, not final): salvage / Recovery Bay bootstrap → genetics and breeding → digital workspace tools. Recovery Bay is a KubeJS fallback only.
- Owns Hostile Neural Networks, Placebo, and Azurum Miner (moved out of Verdant).

### Liminal — "Reunite, settle, resist"

- Planetfall on a lived world. Not another classroom void; not the ship.
- Mechanical (sieve literacy), magic (obtain), and lab (genetics / digital) paths run in parallel and reunite. **Cross-pack bridges default here.** Progressive Field Manual for players arriving cold — not a day-one dump.
- Adds combat and colonial pressure: settle, resist the hostile biosphere, and the TechnoMage synthesis.
- **Liminal-only additions** are listed below; they are the only mods Liminal teaches that no other pack owns.

## Mod overlap

Counts are a snapshot (2026-09-29) and go stale fast. **The `mods/` folder in each repo is the source of truth**; do not copy these numbers into prose elsewhere.

| Set | Count | Notes |
|-----|-------|-------|
| Verdant | 123 | |
| Elysian | 128 | |
| Influx | 94 | |
| **Shared core** (in V, E and I) | 70 | See below |
| Verdant ∪ Elysian ∪ Influx | 186 | |
| Liminal-only additions | 22 | |
| **Liminal total** | **208** | = 186 + 22 |

Liminal is a strict superset: every mod in V, E, or I is also in Liminal.

**Shared core (all four packs):** FTB Quests / Teams / Library / Filter System / XMod Compat, Certain Questing Additions, KubeJS (+ Rhino, KubeJS Delight), Patchouli, GuideME, FancyMenu, SpecterRealm Core, Sophisticated Storage / Backpacks / Core, Silent Gear + Silent Lib, Farmer's Delight, Farming for Blockheads, EMI (+ EMI++, Patternizer), JEI, Jade, Inventory Profiles Next, Xaero's Minimap and World Map, Comforts, Gravestone, FallingTree, RightClickHarvest, Simple Magnets, and the client-performance stack (Sodium, Iris, ModernFix, FerriteCore, Entity Culling).

**Liminal-only additions:**

| Group | Mods |
|-------|------|
| Cross-pack bridges | Ars Mekanica, Ars Creo, Ars Technica, Ars Énergistique, ProjectExtendedAdvancedAE |
| Endgame / dimension | The Twilight Forest, Draconic Evolution (+ Brandon's Core) |
| Structures & world | Wizard Tower, Skeleton Ghost Ship, Ruined Lighthouse, Illager Arena, Underwater Village, Jungle Treehouse Village, Towns and Towers, Structory: Towers, Forest Watchtower, Lithostitched, Improved Village Placement |
| Other | Animal Pens, KubeJS EyeJS, Cristel Lib |

To recompute: `for r in verdant elysian influx liminal; do ls minecraft-modpack-cp-$r/mods/*.pw.toml | wc -l; done`.

## Quest book structure

Sidebar groups are stable labels across the series; each pack shows 1–2 chapters per group (a "semester"). Quests **teach and reward; they never hard-gate**, and rewards are QoL plus Field Manual pages — not the only path to a resource.

| Pack | Chapters (player-facing) |
|------|--------------------------|
| Verdant | Welcome · Make Camp · Work the Earth · Automate It · Infrastructure · Processing · Networks · Scale · Command · Side Quests |
| Elysian | Welcome · Void Camp · First Source · Grow the Garden · Spirit Labor · Dense Magic · Iron's Combat · Side Quests |
| Influx | Welcome · Ship Camp · Typed Matter · Genetics Lab · EMC Ladder · Spanner Workspace · Specimen Loop · Azurum Mass · AppliedE · Side Quests |
| Liminal | Welcome · First Foothold · Mechanical Path · Magic Path · Lab Path · Cross Bridges · Colonial Settle · Resistance · TechnoMage · Side Quests |

Chapter *status* (built vs stub) is tracked in each repo, not here.

## Change control

- Changing a pack's role, world, or contingency → edit this file (and `story.md` if the fiction changes) **first**, then the pack repo.
- Moving a mod between packs → update the owning pack's `mods/`, `CHANGELOG.md`, and the tables above.
- Never restate this file's content in a pack repo — link to it.
