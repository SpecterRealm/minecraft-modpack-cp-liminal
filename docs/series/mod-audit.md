# Mod Audit — overlap and reasons

A running work list, not a set of decisions. It tracks where mods overlap in function, so packs stay on theme and Liminal does not bloat into a kitchen-sink pack.

> Rules live in [`pack-architecture.md`](pack-architecture.md#ownership-principle): a mod from another pack needs a **reason** to be here; multiple routes to the same resource are welcome; exact duplicates are trimmed, and the mod goes to the pack whose theme it fits. The `mods/` folder in each repo is authoritative for what is actually shipped.

Pack letters: **V** Verdant · **E** Elysian · **I** Influx · **L** Liminal.

## Clusters

| Cluster | Mods (where) | Overlap | Question |
|---|---|---|---|
| **Mining / getting ore** | Ex Deorum sieve (V, L) · Mekanism Digital Miner (V, L) · Azurum Miner (I, L) | Three ways to get ore: sieve it, dig it with a machine, or work asteroid/debris with a single-block miner | Influx has no Mekanism. Is Azurum Miner the right single-block answer for asteroid/debris mining, or would Digital Miner do the same job in Influx? In Liminal, do both earn a place? |
| **Plants and crops** | AgriCraft (I, L) · Botany Pots + Tiers + Trees (E, I, L) · Mystical Agriculture (E, L) · Productive Trees (I, L) | AgriCraft is the crop-genetics pillar; Botany Trees (where/how trees are planted) and Productive Trees (what trees produce) complement each other | Verify Productive Trees species can be grown via Botany Trees. |
| **Passive production** | Productive Bees (I, L) | Bees give a compact non-crop route to resources | Keep as Influx's compact, passive answer? |
| **Item transfer** | Translocators (E, L) · Ars Nouveau Starbuncles (E, L) · Ender Storage (E, L) · AE2 (V, I, L) · Create belts (V, L) · Mekanism transporters (V, L) | Translocators is the non-powered, magic-flavored option: no pipes, no motor, no power | Translocators is fixed/chest-to-chest and needs no power; Starbuncles are mobile familiars. Do Starbuncles offer the same filtering and routing? (Unverified — check before relying on them.) Where in Elysian's and Liminal's chapters does Translocators come in? |
| **EMC / matter conversion** | ProjectE + Useful ProjectE + ProjectE Integration + AutoEMC + AppliedE + Replication (I) | Six mods, one destination: EMC as the way things get made (a Star Trek-style replicator) | Kept as a stack. Still to decide: what each piece does on the ladder, and Useful ProjectE's role (not yet reviewed). |
| **Stone generation** | Create Cobblestone + Cobblegen Galore (V, L) | Tiered by design in Verdant (Create-scaled, then single-block) | Does Liminal need both? |
| **Mob drops** | Mob Grinding Utils (V, L) · Hostile Neural Networks (I, L) | Different modes (farming vs. simulation) | Reason for both in Liminal? |
| **Building assist** | Building Wands (V, E, L) · Building Gadgets + Charging Gadgets (V, L) | Tiered: wands early, FE-powered gadgets late | Fine in Liminal, or trim to one? |
| **Power** | Mekanism Generators, Extreme Reactors, Flux Networks (V, L) | Influx has no generators | What powers Azurum Miner in Influx? |
| **Storage** | Sophisticated Storage (all) · AE2 (V, I, L) · Ender Storage (E, L) | Tiered by design | — |

## Decided so far

- **Crops:** AgriCraft is Influx's crop-genetics pillar; **Productive Farming removed** from Influx and Liminal (duplicate).
- **Trees:** Botany Trees and Productive Trees both stay (different jobs); verify they work together.
- **EMC:** it is the destination — AutoEMC and the ProjectE stack stay.
- Charging Gadgets, Energy Meter, and Mob Grinding Utils out of Elysian (tech aesthetic).
- Translocators stays in Elysian and Liminal (non-powered, no-pipe transfer).
- Azurum Miner stays in Influx as asteroid/debris mining, with the power scale lesson.
- AE2 is welcome in Influx for automation in limited space.

## Tickets

- Influx [#28](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/28) — set up a void world option for testing.
- Influx [#29](https://github.com/SpecterRealm/minecraft-modpack-cp-influx/issues/29) — test the Azurum Miner in a void world (settles the mining cluster).

## Next

Go cluster by cluster: name the pack that owns each theme, pick the pillar, and move or trim the rest. Update `mods/` and this table as each is resolved.
