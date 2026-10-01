# Recipe analyze summary

Generated: `2026-10-01T16:46:38.943078+00:00`

Regenerate after mod list / KubeJS changes: `make recipe-audit`.

## Recipe dump

- Source: `docs/recipe_data.json`
- Dump generated: `2026-10-01T16:46:37.729479+00:00`
- Items: **10293**
- Mods with result items: **91**
- Items whose recipes are all inactive (load condition not met in this pack): 1161, not counted

### Namespaces with no installed jar

30 namespaces appear in the dump only because an installed mod ships
compat recipes for them. They are not in the pack; do not count them as mods.

| Namespace | Items |
|-----------|------:|
| `ae2helpers` | 1 |
| `apotheosis` | 15 |
| `apothic_enchanting` | 38 |
| `ars_elemancy` | 21 |
| `ars_elemental` | 98 |
| `ars_scalaes` | 1 |
| `ars_technica` | 34 |
| `ars_trinkets` | 2 |
| `arsomega` | 8 |
| `biomeswevegone` | 68 |
| `buildinggadgets2` | 6 |
| `cobblegengalore` | 7 |
| `createaddition` | 34 |
| `exmachinis` | 8 |
| `hostilenetworks` | 8 |
| `irons_jewelry` | 2 |
| `irons_spellbooks` | 160 |
| `modonomicon` | 1 |
| `more_tier_upgrade` | 14 |
| `morethermalevaporation` | 16 |
| `not_enough_glyphs` | 24 |
| `occultism` | 278 |
| `productivelib` | 3 |
| `productivemetalworks` | 150 |
| `replication` | 5 |
| `sauce` | 1 |
| `sgearmetalworks` | 44 |
| `simplemagnets` | 4 |
| `theurgy` | 220 |
| `toomanyglyphs` | 14 |

### Per-mod counts (top by items)

| Mod | Items | Jar recipes on results | Seed-like ids |
|-----|------:|-----------------------:|--------------:|
| `productivetrees` | 2775 | 3152 | 0 |
| `minecraft` | 1050 | 3737 | 4 |
| `create` | 637 | 1152 | 0 |
| `botanypotstiers` | 552 | 1467 | 0 |
| `mekanism` | 409 | 848 | 0 |
| `ars_nouveau` | 370 | 570 | 0 |
| `twilightforest` | 357 | 455 | 0 |
| `mysticalagriculture` | 341 | 449 | 104 |
| `ae2` | 330 | 518 | 0 |
| `silentgear` | 279 | 572 | 1 |
| `occultism` | 278 | 380 | 0 |
| `productivebees` | 225 | 373 | 0 |
| `theurgy` | 220 | 683 | 0 |
| `botanypots` | 183 | 244 | 0 |
| `draconicevolution` | 164 | 179 | 0 |
| `irons_spellbooks` | 160 | 195 | 0 |
| `farmersdelight` | 151 | 182 | 2 |
| `productivemetalworks` | 150 | 333 | 0 |
| `exdeorum` | 141 | 458 | 1 |
| `powah` | 133 | 171 | 0 |
| `sophisticatedstorage` | 116 | 251 | 0 |
| `projecte` | 107 | 135 | 0 |
| `ars_elemental` | 98 | 104 | 0 |
| `megacells` | 82 | 105 | 0 |
| `biomeswevegone` | 68 | 118 | 0 |
| `advanced_ae` | 63 | 73 | 0 |
| `ars_additions` | 58 | 66 | 0 |
| `sophisticatedbackpacks` | 49 | 76 | 0 |
| `sgearmetalworks` | 44 | 73 | 0 |
| `azurum_miner` | 42 | 67 | 1 |
| `apothic_enchanting` | 38 | 38 | 0 |
| `ars_zero` | 38 | 38 | 0 |
| `appliedcreate` | 35 | 37 | 0 |
| `mob_grinding_utils` | 35 | 40 | 0 |
| `ars_technica` | 34 | 35 | 0 |
| `createaddition` | 34 | 44 | 1 |
| `comforts` | 33 | 66 | 0 |
| `mekanismgenerators` | 31 | 31 | 0 |
| `toughasnails` | 31 | 31 | 0 |
| `bhc` | 29 | 36 | 0 |
| … | (51 more mods in `by-mod/`) | | |

### Farming / resource-crop namespaces

| Namespace | Items | Seed-like |
|-----------|------:|----------:|
| `mysticalagriculture` | 341 | 104 |
| `agricraft` | 7 | 0 |
| `productivefarming` | 0 | 0 |
| `productivetrees` | 2775 | 0 |
| `botanypots` | 183 | 0 |

Seed-like lists: `mysticalagriculture-seeds.txt`, `agricraft-seeds.txt`, …
Full per-mod item lists: `by-mod/<mod>.txt`.

## AgriCraft plant datapacks

- Plants found: **299**
- Mods dir: `~/Library/Application Support/PrismLauncher/instances/CP-Liminal-Dev/minecraft/mods`

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
