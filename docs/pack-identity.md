# Colony Protocol: Liminal — identity

**Theme (LOCKED):** Planetfall kitchen-sink inherit — reunite the Verdant, Elysian, and Influx systems, plus combat and colonial settlement, on a lived world.

**Loader:** Minecraft 1.21.1 · NeoForge 21.1.228 (series-wide; match `pack.toml`).

**Series context:** Liminal is pack 4 and the series source of truth. Story, pack roles, and mod ownership are in [`series/`](series/README.md) — this file covers only what Liminal itself owns.

## What Liminal owns

- **World:** a lived planet — not a classroom void, not the ship.
- **Loop:** the three literacies (mechanical, magic, lab) running in parallel and reuniting; then settle, resist, TechnoMage.
- **Mods:** the full union of Verdant, Elysian, and Influx, plus the Liminal-only additions (cross-pack bridges, Twilight Forest, Draconic Evolution, structures). The lists and counts are in [`series/pack-architecture.md`](series/pack-architecture.md#mod-overlap); the `mods/` folder is authoritative.
- **Colony and settlement features** — Verdant only has villagers; Liminal wraps the colony fantasy up fully. The mod (MineColonies is a candidate) is still to be chosen.
- **The full explanation of the Veil** and the TechnoMage revelation — see [`story.md`](story.md).
- **Cross-pack bridges** (Ars ↔ Mekanism and friends) — they default here and nowhere else.
- **Quest chapters:** Welcome, First Foothold, Mechanical / Magic / Lab Path, Cross Bridges, Colonial Settle, Resistance, TechnoMage, Side Quests.

## Not yet done

- Late chapters (Colonial Settle, Resistance, TechnoMage) are stubs; path chapters are partly built.
- Recovery Bay / gem bootstrap KubeJS — design first, then implement.
- Full FancyMenu Bridge chrome (buttons / CALIBRATE) — title, drippy, level-loading, and pause backgrounds ship under `config/fancymenu/`.
- Prism smoke test of the full union.

## How to add mods

```bash
packwiz curseforge add <slug>   # or packwiz modrinth add …
make refresh
```

Pin soft / candidate jars only after 1.21.1 confirm + smoke-test. Prefer documenting TODOs over guessing pins. If a mod belongs to Verdant, Elysian, or Influx, update **that** pack first, then bring it here.

## Recipe viewer defaults

Shipped EMI/JEI configs match the series pattern (`index-source = registered`, EMI++ stack groups on, JEI `maxColumns = 12`). Sophisticated Storage wood-variant barrels/chests collapse via `kubejs/assets/cpliminal/stack_groups/ss_*.json`. Verify barrel page count in Prism after pull.
