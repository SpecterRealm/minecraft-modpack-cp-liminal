# Recipe analyze summary

Generated: `2026-10-01T15:41:11.503269+00:00`

Regenerate after mod list / KubeJS changes: `make recipe-audit`.

## Recipe dump

- Source: `docs/recipe_data.json`
- Dump generated: `2026-10-01T15:41:10.396520+00:00`
- Items: **11581**
- Mods with result items: **142**

### Per-mod counts (top by items)

| Mod | Items | Jar recipes on results | Seed-like ids |
|-----|------:|-----------------------:|--------------:|
| `productivetrees` | 2776 | 3153 | 0 |
| `minecraft` | 670 | 2565 | 5 |
| `create` | 642 | 1177 | 0 |
| `botanypotstiers` | 552 | 1467 | 0 |
| `mekanism` | 411 | 917 | 0 |
| `productivebees` | 390 | 615 | 0 |
| `mysticalagriculture` | 387 | 527 | 136 |
| `ars_nouveau` | 370 | 572 | 0 |
| `theurgy` | 358 | 1485 | 0 |
| `twilightforest` | 357 | 455 | 0 |
| `ae2` | 330 | 518 | 0 |
| `productivefarming` | 316 | 318 | 47 |
| `silentgear` | 279 | 572 | 1 |
| `occultism` | 278 | 380 | 0 |
| `exdeorum` | 229 | 728 | 1 |
| `botanypots` | 183 | 244 | 0 |
| `draconicevolution` | 164 | 179 | 0 |
| `irons_spellbooks` | 160 | 195 | 0 |
| `productivemetalworks` | 158 | 557 | 0 |
| `farmersdelight` | 151 | 182 | 2 |
| `alltheores` | 137 | 137 | 0 |
| `powah` | 133 | 171 | 0 |
| `sophisticatedstorage` | 124 | 278 | 0 |
| `ftbmaterials` | 123 | 123 | 0 |
| `megacells` | 108 | 136 | 0 |
| `projecte` | 107 | 141 | 0 |
| `bigreactors` | 102 | 155 | 0 |
| `ars_elemental` | 98 | 104 | 0 |
| `biomeswevegone` | 89 | 174 | 0 |
| `sgearmetalworks` | 65 | 181 | 0 |
| `advanced_ae` | 63 | 76 | 0 |
| `mekanismtools` | 61 | 61 | 0 |
| `ars_additions` | 58 | 66 | 0 |
| `modern_industrialization` | 58 | 58 | 0 |
| `sophisticatedbackpacks` | 57 | 92 | 0 |
| `immersiveengineering` | 44 | 61 | 0 |
| `azurum_miner` | 42 | 67 | 1 |
| `silentgems` | 42 | 126 | 0 |
| `apothic_enchanting` | 39 | 39 | 0 |
| `ars_zero` | 38 | 38 | 0 |
| … | (102 more mods in `by-mod/`) | | |

### Farming / resource-crop namespaces

| Namespace | Items | Seed-like |
|-----------|------:|----------:|
| `mysticalagriculture` | 387 | 136 |
| `agricraft` | 7 | 0 |
| `productivefarming` | 316 | 47 |
| `productivetrees` | 2776 | 0 |
| `botanypots` | 183 | 0 |

Seed-like lists: `mysticalagriculture-seeds.txt`, `agricraft-seeds.txt`, …
Full per-mod item lists: `by-mod/<mod>.txt`.

## AgriCraft plant datapacks

- Plants found: **299**
- Mods dir: `/Users/michaelheaton/Library/Application Support/PrismLauncher/instances/CP-Liminal-Dev/minecraft/mods`

| Plant namespace | Count |
|----------------|------:|
| `mysticalagriculture` | 136 |
| `pamhc2crops` | 97 |
| `minecraft` | 32 |
| `agricraft` | 18 |
| `biomesoplenty` | 11 |
| `farmersdelight` | 4 |
| `immersiveengineering` | 1 |

Full list: [`agricraft-plants.txt`](agricraft-plants.txt).
These are datapack plant defs (products / genetics), not JEI craftable
seed recipes. Use both this file and `recipe_data.json` for lane work;
do not treat recipe-dump seed counts alone as the AgriCraft plant catalog.
