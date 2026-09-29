# Mod Audit — overlap and reasons

A running work list, not a set of decisions. It tracks where mods overlap in function, so packs stay on theme and Liminal does not bloat into a kitchen-sink pack.

> Rules live in [`pack-architecture.md`](pack-architecture.md#ownership-principle): a mod from another pack needs a **reason** to be here; multiple routes to the same resource are welcome; exact duplicates are trimmed, and the mod goes to the pack whose theme it fits. The `mods/` folder in each repo is authoritative for what is actually shipped.

Pack letters: **V** Verdant · **E** Elysian · **I** Influx · **L** Liminal.

## Clusters

| Cluster | Mods (where) | Overlap | Question |
|---|---|---|---|
| **Mining / getting ore** | Ex Deorum sieve (V, L) · Mekanism Digital Miner (V, L) · Azurum Miner (I, L) | Three ways to get ore: sieve it, dig it with a machine, or work asteroid/debris with a single-block miner | Influx has no Mekanism. Is Azurum Miner the right single-block answer for asteroid/debris mining, or would Digital Miner do the same job in Influx? In Liminal, do both earn a place? |
| **Plants and crops** | AgriCraft (I, L) · Productive Farming (I, L) · Botany Pots + Tiers + Trees (E, I, L) · Mystical Agriculture (E, L) · Productive Trees (I, L) | AgriCraft is a hands-on genetics system; Productive Farming is crop content plus flower/bee breeding; both do trait breeding. Botany Trees (where/how trees are planted) and Productive Trees (what trees produce) complement each other | Keep both, or pick a pillar? How do they work with Botany Pots, Productive Bees, Mystical Agriculture and the core farming mods? See [#31](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/31). |
| **Passive production** | Productive Bees (I, L) | Bees give a compact non-crop route to resources | Keep as Influx's compact, passive answer? |
| **Item transfer** | Translocators (E, L) · Ars Nouveau Starbuncles (E, L) · Ender Storage (E, L) · AE2 (V, I, L) · Create belts (V, L) · Mekanism transporters (V, L) | Translocators is the non-powered, magic-flavored option: no pipes, no motor, no power | Translocators is fixed/chest-to-chest and needs no power; Starbuncles are mobile familiars. Do Starbuncles offer the same filtering and routing? (Unverified — check before relying on them.) Where in Elysian's and Liminal's chapters does Translocators come in? |
| **EMC / matter conversion** | ProjectE + Useful ProjectE + ProjectE Integration + AutoEMC + AppliedE + Replication (I) | Six mods, one destination: EMC as the way things get made (a Star Trek-style replicator) | Kept as a stack. Still to decide: what each piece does on the ladder, and Useful ProjectE's role (not yet reviewed). |
| **Stone generation** | Create Cobblestone + Cobblegen Galore (V, L) | Tiered by design in Verdant (Create-scaled, then single-block) | Does Liminal need both? |
| **Mob drops** | Mob Grinding Utils (V, L) · Hostile Neural Networks (I, L) | Different modes (farming vs. simulation) | Reason for both in Liminal? |
| **Building assist** | Building Wands (V, E, L) · Building Gadgets + Charging Gadgets (V, L) | Tiered: wands early, FE-powered gadgets late | Fine in Liminal, or trim to one? |
| **Power** | Mekanism Generators, Extreme Reactors, Flux Networks (V, L) | Influx has no generators | What powers Azurum Miner in Influx? |
| **Storage** | Sophisticated Storage (all) · AE2 (V, I, L) · Ender Storage (E, L) | Tiered by design | — |

## Full audit

The cluster table above covers known overlaps. The full audit walks **every** mod. The objective data — which packs ship each mod, side, and pin source — is generated in [`mod-inventory.md`](mod-inventory.md) by `scripts/series-mod-inventory.py`; rerun the script rather than editing that file. For each mod the audit records a category, why it is in each pack that carries it, and a decision (keep / trim / move / question).

**Method, per group:** (1) classify each mod; (2) for any mod outside its home pack, state the reason it is there; (3) mark keep / trim / move; (4) record decisions here.

### Groups (as of 2026-09-29)

| Group | Count | What it is |
|---|---|---|
| Shared core (V E I L) | 70 | Libraries, quest and UI stack, storage, recipe viewers, client performance, farming and quality-of-life mods |
| Verdant-owned (V L) | 44 | Create, Mekanism, AE2 add-ons, Ex Deorum, Terralith and friends |
| Elysian-owned (E L) | 40 | Ars Nouveau and add-ons, Iron's, Apotheosis, Mystical Agriculture, Occultism, Theurgy |
| Influx-owned (I L) | 16 | ProjectE and EMC stack, Replication, AgriCraft, Productive family, Azurum, HNN |
| Liminal-only (L) | 22 | Bridges, structures, Twilight Forest, Draconic Evolution, libraries |
| V E L (not Influx) | 8 | Tough As Nails (+ vanilla pack), Essential Mod, Baubley Heart Canisters, Building Wands, KubeJS Tweaks, GeckoLib, GlitchCore |
| V I L (not Elysian) | 1 | Applied Energistics 2 |
| E I L (not Verdant) | 7 | Botany Pots (+ Tiers, Trees, KubeJS), Placebo, FastSuite, FastWorkbench |

### First-pass observations

**Release risk — Modrinth-pinned mods.** 19 mods are pinned from Modrinth rather than CurseForge, including several Elysian pillars (Ars Nouveau, Occultism, Theurgy, Mystical Agriculture, Iron's Spells 'n Spellbooks, Modonomicon, Ender Storage, Skyblock Builder) and Liminal's Ars Mekanica. Each repo's `docs/curseforge-export.md` explains the CurseForge moderation rules for the packs' export; check every Modrinth pin against them before a CurseForge release.

**Shared core.** Of the 70, 21 are libraries and 6 are client/performance mods; the rest are the quest and UI stack, storage, recipe viewers, and quality of life. (Across all four packs there are 39 libraries.) Questions:
- **Wooden Shears** exists for Verdant's early leaf harvesting before iron. Does it belong in Elysian, Influx, and Liminal?
- **Silent Gear** is in all four packs as the shared tool system — confirm that is intended.
- **Comforts, Simple Magnets, Morph-o-Tool, More Tier Upgrade, Target Dummy, Akashic Tome** — each is a general quality-of-life choice; confirm none fights a pack's theme.

**V E L, not Influx.** Should Influx (a real ship, in flight) have **Tough As Nails** (thirst and temperature)? **Essential Mod** is a client-side social/cosmetics mod rather than a gameplay mod — why is it in packs at all, and should it be in all four or none? **Baubley Heart Canisters** and **KubeJS Tweaks**: are they wanted everywhere?

**E I L, not Verdant.** **FastSuite / FastWorkbench** are crafting quality-of-life mods that Verdant lacks — put them in the shared core or drop them. **Placebo** is a dependency (Apotheosis in Elysian, Hostile Neural Networks in Influx).

**Verdant-owned (44) in Liminal.** Liminal's mechanical path needs a reason for each. Candidates to trim from Liminal as late-game add-ons rather than path essentials: Better P2P, Extended Terminal, MEGA Cells, ME Requester, AE2 Tangible Bookmarks, Better Fusion Reactor PLUS, Mekanism: More Thermal Evaporation, Mekanism Unleashed, Building Gadgets + Charging Gadgets, Energy Meter. Which subset does Liminal's mechanical path actually assume?

**Elysian-owned (40).** Ars Nouveau plus eight add-ons (Additions, Caelum, Controle, Elemancy, Elemental, Ocultas, Polymorphia, Zero) and Not Enough Glyphs is a lot of add-ons — does each earn its place? In particular **Ars Elemental vs. Ars Elemancy**. Occultism and Theurgy are both "magical labor" systems with different jobs. The Apotheosis suite is four mods.

**Influx-owned (16).** Already covered by the cluster table, plus: **Useful ProjectE** has not been reviewed; **Productive Metalworks** and **Silent Gear Metalworks** are a foundry plus its Silent Gear bridge (decided: both stay, in all packs).

**Liminal-only (22).** **The Twilight Forest**, **Draconic Evolution**, and **Animal Pens** have no stated story role yet; the five bridges, eleven structure mods, and three libraries follow from the finale design.

## Review notes (from maintainer feedback)

**Pins: CurseForge over Modrinth.** Modrinth-pinned mods can misbehave in the CurseForge app, so every mod should pin to CurseForge where a NeoForge 1.21.1 file exists. Nineteen ids are Modrinth-pinned today (Ars Nouveau, Ars Mekanica, Occultism, Theurgy, Modonomicon, Mystical Agriculture, Mystical Automation, Translocators, Ender Storage, CodeChicken Lib, CB Multipart, Iron's Spells, LibX, Cucumber, SmartBrainLib, PlayerAnimator, Skyblock Builder, Tough As Nails (vanilla pack), Inventory Tweaks Emu). The migration needs CurseForge API access (`packwiz curseforge add <slug> --file-id ...`), which the cloud container does not have (403), so it runs from a local checkout. Any mod with no CurseForge build (or API-excluded) keeps a Modrinth pin and is listed in the pack's `docs/curseforge-export.md`.

**Wooden Shears (Verdant).** Added so Tough As Nails leaf armor works before iron shears. Prefer no extra mod: options are a KubeJS recipe for vanilla shears from a cheaper material, or a flint/copper-tier shears recipe. Decide when the mod is reviewed.

**Animal Pens (Influx).** Stores animals in pens, aquariums and aviaries while keeping breeding, shearing, milking and drops working; reduces entity lag. It fits a space-limited ship (compact livestock), so a natural Influx candidate rather than Liminal-only. [Source](https://modrinth.com/project/K5CAV4wi).

**Twilight Forest, Draconic Evolution.** Added for extra content and things to do. Keep for now; cut if they add no value once story roles are settled.

**Ars Nouveau add-ons (Elysian).** Nobody on the team has played Ars Nouveau yet, so each add-on is judged by what it adds:

| Add-on | What it adds | Initial call |
|---|---|---|
| Ars Additions | Small tweaks and quality-of-life for Ars Nouveau | Low-cost; keep pending playtest |
| Ars Caelum | Skyblock support: rituals for cobblestone, islands, geodes; Crush acts as a hammer with ore drops | Overlaps Ex Deorum in Verdant; check whether Elysian needs it |
| Ars Controle | Remote entity control, portable relayed rituals, scroll holder | Utility; review |
| Ars Elemental | Four elemental schools: focuses, armor sets, new glyphs | Core add-on; likely keep |
| Ars Elemancy | Dual/quad-element armor and foci; requires Ars Elemental | Depends on Elemental; keep only if Elemental stays |
| Ars Ocultas | Occultism bridge: spirits in containment jars, sacrificial altar | Keep only if Occultism stays in Elysian |
| Ars Polymorphia | Polymorph selection for Storage Lectern crafting | QoL; low value if the lectern is unused |
| Ars Zero | New cast devices and glyphs | Review |
| Not Enough Glyphs | Utility glyphs, SpellBinder | Popular; likely keep |

Sources: Ars Caelum, Elemental, Elemancy, Ocultas, Polymorphia and Additions listings on CurseForge/Modrinth; Ars Controle, Zero and Not Enough Glyphs descriptions were thin, so their calls need a playtest.

## Decided so far

- **Crops:** *reopened.* Productive Farming was removed as a "duplicate" of AgriCraft, then restored — it is content-heavy (about 160 crops, flower/dye breeding, bee integration), not a duplicate. Keeping both for now; the choice is tracked in Influx [#31](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/31).
- **Trees:** Botany Trees and Productive Trees both stay (different jobs); verify they work together.
- **EMC:** it is the destination — AutoEMC and the ProjectE stack stay.
- **Metalworking:** Productive Metalworks and Silent Gear Metalworks change how gear is made, so they go in **all four packs** (Tinkers' Construct-style melt, alloy and cast). The bridge only works with the foundry, so they stay together. Verdant's and Elysian's early game relies on Silent Gear grid crafting, so the rollout needs a test and quest rewrites; tracked in [#42](https://github.com/SpecterRealm/minecraft-modpack-cp-liminal/issues/42).
- Charging Gadgets, Energy Meter, and Mob Grinding Utils out of Elysian (tech aesthetic).
- Translocators stays in Elysian and Liminal (non-powered, no-pipe transfer).
- Azurum Miner stays in Influx as asteroid/debris mining, with the power scale lesson.
- AE2 is welcome in Influx for automation in limited space.

## Tickets

- Influx [#28](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/28) — set up a void world option for testing.
- Influx [#31](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/31) — review whether to keep AgriCraft, Productive Farming, or both.
- Influx [#29](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/29) — test the Azurum Miner in a void world (settles the mining cluster).

## Next

Go cluster by cluster: name the pack that owns each theme, pick the pillar, and move or trim the rest. Update `mods/` and this table as each is resolved.
