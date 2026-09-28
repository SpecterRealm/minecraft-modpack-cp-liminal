# Colony Protocol: Liminal — identity

**Theme (LOCKED):** Planetfall kitchen-sink inherit — reunite V/E/I systems + combat / colonial settle on a lived world.

**Loader:** Minecraft 1.21.1 · NeoForge 21.1.228 (match Verdant).

**Mod set:** **Verdant ∪ Elysian ∪ Influx** — full kitchen-sink reunite (**133** `.pw.toml` pins). Verdant teaching pillars (Create / Mek / AE2 / Ex Deorum / power / Terralith) + Elysian magic/skyblock (Ars / MA / Occultism / Iron's / … + soft deps) + Influx landings (HNN / Placebo / Azurum). Shared QoL dual-sourced where CF API-excludes (More Overlays, Entity Culling, Extreme Reactors Create Compat).

## Not in this scaffold

- Full quest chapters (quest worker owns SNBT; early/mid spine + late stubs present)
- ProjectE / AppliedE / AgriCraft / Replication — Influx-first candidates not pinned in V/E/I yet
- Recovery Bay / gem bootstrap KubeJS — design first, then implement
- FancyMenu brand assets (mod pinned; chrome TBD — see art PR)

## Design pointers

Project store: docs/pack-architecture.md §Liminal · pack-progression-arcs.md §L · series-todos.md (port teaching packs; cross-pack bridges default here).

## How to add mods

```bash
packwiz curseforge add <slug>   # or packwiz modrinth add …
make refresh
```

Pin Soft / candidate jars only after 1.21.1 confirm + smoke-test. Prefer documenting TODOs over guessing pins.
