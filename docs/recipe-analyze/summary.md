# Recipe analyze summary

Generated: `2026-09-30T13:11:34.894619+00:00`

Regenerate after mod list / KubeJS changes: `make recipe-audit`.

## Recipe dump

`docs/recipe_data.json` is **missing**.
Run `make recipe-wiki` on a machine with `CP-Liminal-Dev` mod JARs,
then re-run `make recipe-analyze` (or `make recipe-audit`).

Do not copy Verdant `recipe_data.json` into this pack.

## AgriCraft plant datapacks

- Plants found: **299**
- Mods dir: AgriCraft jar only (cloud partial scan); Michael should re-run `make recipe-audit` on CP-Liminal-Dev for full dump + all jars

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
