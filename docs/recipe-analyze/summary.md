# Recipe analyze summary

Generated: `2026-10-01T17:06:01.081180+00:00`

Regenerate after mod list / KubeJS changes: `make recipe-audit`.

## Recipe dump

- Source: `docs/recipe_data.json`
- Dump generated: `2026-10-01T17:05:59.743298+00:00`
- Items: **10683**
- Mods with result items: **96**
- Items whose recipes are all inactive (load condition not met in this pack): 1296, not counted
- Fluids and chemicals made by recipes (pseudo items): 198, not counted as items

### Namespaces with no installed jar

33 namespaces appear in the dump only because an installed mod ships
compat recipes for them. They are not in the pack; do not count them as mods.

| Namespace | Items |
|-----------|------:|
| `ae2helpers` | 1 |
| `apotheosis` | 21 |
| `apothic_enchanting` | 50 |
| `ars_elemancy` | 105 |
| `ars_elemental` | 146 |
| `ars_scalaes` | 1 |
| `ars_technica` | 34 |
| `ars_trinkets` | 2 |
| `arsomega` | 8 |
| `biomeswevegone` | 68 |
| `botania` | 2 |
| `buildinggadgets2` | 6 |
| `cobblegengalore` | 7 |
| `createaddition` | 42 |
| `exmachinis` | 8 |
| `forbidden_arcanus` | 1 |
| `gateways` | 1 |
| `hostilenetworks` | 8 |
| `irons_jewelry` | 2 |
| `irons_spellbooks` | 160 |
| `modonomicon` | 1 |
| `more_tier_upgrade` | 14 |
| `morethermalevaporation` | 16 |
| `not_enough_glyphs` | 24 |
| `occultism` | 282 |
| `productivelib` | 3 |
| `productivemetalworks` | 113 |
| `replication` | 5 |
| `sauce` | 1 |
| `sgearmetalworks` | 37 |
| `simplemagnets` | 4 |
| `theurgy` | 219 |
| `toomanyglyphs` | 14 |

### Per-mod counts (top by items)

| Mod | Items | Jar recipes on results | Seed-like ids |
|-----|------:|-----------------------:|--------------:|
| `productivetrees` | 2775 | 3152 | 0 |
| `minecraft` | 1110 | 4458 | 4 |
| `create` | 634 | 1229 | 0 |
| `botanypotstiers` | 552 | 1467 | 0 |
| `mysticalagriculture` | 526 | 706 | 106 |
| `twilightforest` | 373 | 475 | 0 |
| `ars_nouveau` | 370 | 575 | 0 |
| `mekanism` | 353 | 566 | 0 |
| `ae2` | 331 | 540 | 0 |
| `occultism` | 282 | 394 | 0 |
| `silentgear` | 279 | 618 | 1 |
| `productivebees` | 228 | 502 | 0 |
| `theurgy` | 219 | 682 | 0 |
| `botanypots` | 183 | 244 | 0 |
| `farmersdelight` | 166 | 235 | 2 |
| `draconicevolution` | 164 | 181 | 0 |
| `irons_spellbooks` | 160 | 210 | 0 |
| `ars_elemental` | 146 | 152 | 0 |
| `exdeorum` | 141 | 458 | 1 |
| `powah` | 134 | 182 | 0 |
| `sophisticatedstorage` | 117 | 265 | 0 |
| `productivemetalworks` | 113 | 172 | 0 |
| `projecte` | 107 | 135 | 0 |
| `ars_elemancy` | 105 | 250 | 0 |
| `megacells` | 82 | 111 | 0 |
| `biomeswevegone` | 68 | 118 | 0 |
| `advanced_ae` | 66 | 78 | 0 |
| `ars_additions` | 58 | 66 | 0 |
| `sophisticatedbackpacks` | 57 | 97 | 0 |
| `azurum_miner` | 51 | 78 | 1 |
| `apothic_enchanting` | 50 | 50 | 0 |
| `createaddition` | 42 | 63 | 0 |
| `toughasnails` | 42 | 44 | 0 |
| `ars_zero` | 41 | 44 | 0 |
| `sgearmetalworks` | 37 | 38 | 0 |
| `mob_grinding_utils` | 36 | 42 | 0 |
| `appliedcreate` | 35 | 37 | 0 |
| `ars_technica` | 34 | 47 | 0 |
| `comforts` | 33 | 66 | 0 |
| `bhc` | 29 | 36 | 0 |
| … | (56 more mods in `by-mod/`) | | |

### Farming / resource-crop namespaces

| Namespace | Items | Seed-like |
|-----------|------:|----------:|
| `mysticalagriculture` | 526 | 106 |
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
