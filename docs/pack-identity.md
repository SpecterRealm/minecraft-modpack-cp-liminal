# Colony Protocol: Liminal — identity

**Theme (LOCKED):** Planetfall kitchen-sink inherit — reunite V/E/I systems + combat / colonial settle on a lived world.

**Loader:** Minecraft 1.21.1 · NeoForge 21.1.228 (match Verdant).

**Mod set:** **Verdant ∪ Elysian ∪ Influx** — full kitchen-sink reunite (**190** `.pw.toml` pins). Verdant teaching pillars (Create / Mek / AE2 / Ex Deorum / power / Terralith) + Elysian magic/skyblock (Ars / MA / Occultism / Iron's / … + soft deps) + Influx landings (HNN / Placebo / Azurum) + L-only DE/TF/structures. Shared QoL dual-sourced where CF API-excludes (More Overlays, Entity Culling, Extreme Reactors Create Compat).

## Not in this scaffold

- Full quest chapters (quest worker owns SNBT; early/mid spine + late stubs present)
- ProjectE / AppliedE / AgriCraft / Replication — Influx-first candidates not pinned in V/E/I yet
- Recovery Bay / gem bootstrap KubeJS — design first, then implement
- Full FancyMenu Bridge chrome (buttons / CALIBRATE) — title, drippy, level-loading, and pause backgrounds ship under `config/fancymenu/`

## Design pointers

Project store: docs/pack-architecture.md §Liminal · pack-progression-arcs.md §L · series-todos.md (port teaching packs; cross-pack bridges default here).

## How to add mods

```bash
packwiz curseforge add <slug>   # or packwiz modrinth add …
make refresh
```

Pin Soft / candidate jars only after 1.21.1 confirm + smoke-test. Prefer documenting TODOs over guessing pins.

## Recipe viewer defaults

Shipped EMI/JEI configs match Verdant/Elysian patterns (`index-source = registered`, EMI++ stack groups on, JEI `maxColumns = 12`). Sophisticated Storage wood-variant barrels/chests collapse via `kubejs/assets/cpliminal/stack_groups/ss_*.json`. Verify barrel page count in Prism after pull.
