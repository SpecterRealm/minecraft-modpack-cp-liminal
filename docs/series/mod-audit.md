# Mod Audit — overlap and reasons

A running work list, not a set of decisions. It tracks where mods overlap in function, so packs stay on theme and Liminal does not bloat into a kitchen-sink pack.

> Rules live in [`pack-architecture.md`](pack-architecture.md#ownership-principle): a mod from another pack needs a **reason** to be here; multiple routes to the same resource are welcome; exact duplicates are trimmed, and the mod goes to the pack whose theme it fits. The `mods/` folder in each repo is authoritative for what is actually shipped.

Pack letters: **V** Verdant · **E** Elysian · **I** Influx · **L** Liminal.

## Clusters

| Cluster | Mods (where) | Overlap | Question |
|---|---|---|---|
| **Mining / getting ore** | Ex Deorum sieve (V, L) · Mekanism Digital Miner (V, L) · Azurum Miner (I, L) | Three ways to get ore: sieve it, dig it with a machine, or work asteroid/debris with a single-block miner | Influx has no Mekanism. Is Azurum Miner the right single-block answer for asteroid/debris mining, or would Digital Miner do the same job in Influx? In Liminal, do both earn a place? |
| **Plants and crops** | AgriCraft (I, L) · Botany Pots + Tiers + Trees (E, I, L) · Mystical Agriculture (E, L) · Productive Farming / Trees (I, L) | Several crop systems; Botany Trees and Productive Trees look like the clearest overlap | Which system is Influx's crop pillar? Which of the tree mods stays? |
| **Passive production** | Productive Bees (I, L) | Bees give a compact non-crop route to resources | Keep as Influx's compact, passive answer? |
| **Item transfer** | Translocators (L) · Ars Nouveau Starbuncles (E, L) · Ender Storage (E, L) · AE2 (V, I, L) · Create belts (V, L) · Mekanism transporters (V, L) | Translocators is the non-powered, magic-flavored option: no pipes, no motor, no power | Confirm Starbuncles + Ender Storage leave no transfer gap in Elysian. Where in Liminal's chapters does Translocators come in? |
| **EMC / matter conversion** | ProjectE + Useful ProjectE + ProjectE Integration + AutoEMC + AppliedE + Replication (I) | Six mods around one idea | Is the whole stack needed, or is there a smaller set that keeps "pattern first, then convert"? |
| **Stone generation** | Create Cobblestone + Cobblegen Galore (V, L) | Tiered by design in Verdant (Create-scaled, then single-block) | Does Liminal need both? |
| **Mob drops** | Mob Grinding Utils (V, L) · Hostile Neural Networks (I, L) | Different modes (farming vs. simulation) | Reason for both in Liminal? |
| **Building assist** | Building Wands (V, E, L) · Building Gadgets + Charging Gadgets (V, L) | Tiered: wands early, FE-powered gadgets late | Fine in Liminal, or trim to one? |
| **Power** | Mekanism Generators, Extreme Reactors, Flux Networks (V, L) | Influx has no generators | What powers Azurum Miner in Influx? |
| **Storage** | Sophisticated Storage (all) · AE2 (V, I, L) · Ender Storage (E, L) | Tiered by design | — |

## Decided so far

- Charging Gadgets, Energy Meter, and Mob Grinding Utils out of Elysian (tech aesthetic).
- Translocators out of Elysian for now; in Liminal.
- Azurum Miner stays in Influx as asteroid/debris mining, with the power scale lesson.
- AE2 is welcome in Influx for automation in limited space.

## Next

Go cluster by cluster: name the pack that owns each theme, pick the pillar, and move or trim the rest. Update `mods/` and this table as each is resolved.
