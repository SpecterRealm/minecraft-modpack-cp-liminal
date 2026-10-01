# Adding the decided mods: commands, dependencies and expected effect

Decided but not in any pack yet (`gap-check.md`): Spell Engine and the class mods, the cosmetic armor mod, Genetics: Resequenced and Mutant Monsters; the Verdant defense candidate is listed at the end.

## Why this was not added directly

Adding a mod needs a packwiz pin (download URL and hash). From this environment Modrinth, CurseForge and their CDNs are blocked by organization policy (403), so valid pins cannot be created here, and a pin written without the real file hash would be invented. So this document gives the exact commands to run on a machine with access, plus the expected effect worked out from source.

## Required libraries, read from each mod's `neoforge.mods.toml`

| Mod | Required (besides NeoForge and Minecraft) |
|---|---|
| Spell Engine | Cloth Config, **Player Animator**, **Spell Power** |
| Wizards | **Armor Model API**, **Runes**, Spell Engine, **Structure Pool API** |
| Archers | Armor Model API, **Bundle API**, **Ranged Weapon API**, Spell Engine |
| Rogues & Warriors | Armor Model API, Spell Engine, Structure Pool API |
| Paladins & Priests | Armor Model API, Runes, Spell Engine |
| Bard | Armor Model API, **More RPG Library**, Ranged Weapon API, Spell Engine, Structure Pool API |
| More RPG Library | Spell Engine |
| Genetics: Resequenced | **AaronLib** (mod id `aaron`), Kotlin for Forge |
| Mutant Monsters | **Puzzles Lib** |
| Cosmetic Armor Reworked | none |

(Bold = not in any pack today. Cloth Config, Kotlin for Forge, Curios and GeckoLib already are; Player Animator is only in Elysian and Liminal.) Whether `armor_model_api` is provided by the AzureLib Armor jar the mod pages mention, or is its own library, was not confirmed.

packwiz asks for required dependencies when a mod is added, so only the top-level mods need adding by hand.

## Commands, per pack

Run in each pack repo, then `packwiz refresh` and commit. Slugs are from the mod pages; ones marked "?" were not confirmed and need a search.

| Pack | Add |
|---|---|
| Verdant | Spell Engine (pulled in by Archers), `archers` (CurseForge, project 932359), `cosmetic-armor-reworked`, `mekanism-turrets` (decided) |
| Elysian | `wizards`, `rogues-and-warriors` (CurseForge, project 1048409), `cosmetic-armor-reworked` |
| Influx | `paladins-and-priests`, `bard-more-rpg-classes`, `genetics-resequenced`, `mutant-monsters`, `cosmetic-armor-reworked` |
| Liminal | all of the above plus the candidates `berserker-rpg-class`, `forcemaster-rpg-class`, `elemental-wizards-rpg-class`, `witcher-rpg-class` if wanted |

Example: `packwiz modrinth add wizards` (or `packwiz curseforge add wizards` for packs that publish to CurseForge; match each pack's existing pin source). Use the same Spell Engine and library versions across packs so Liminal's union stays consistent.

## Expected effect (worked out from the scans)

| Pack | Mods added | Items added (scans) | New libraries | Notes |
|---|---|---|---|---|
| Verdant | Spell Engine, Archers, cosmetic armor | 54 | Armor Model API, Bundle API, Ranged Weapon API, Spell Power, Player Animator | Brings Spell Engine into the first pack; Archers upper tiers need netherite and crystals |
| Elysian | Spell Engine, Wizards, Rogues & Warriors, cosmetic armor | 120 | Armor Model API, Runes, Structure Pool API, Spell Power | Third spell system next to Ars and Iron's (decided: each gets a niche); top tiers need netherite, upgrade crystals and an Armory RPGs item |
| Influx | Spell Engine, Paladins & Priests, Bard, More RPG Library, Genetics: Resequenced, Mutant Monsters, cosmetic armor | 264 | Armor Model API, Runes, Ranged Weapon API, Structure Pool API, Spell Power, Player Animator, AaronLib, Puzzles Lib | Genetics adds FE machines (Powah runs them); Mutant Monsters adds End-flavored drops; the egg and spawner recipes still need writing |
| Liminal | everything, plus 4 optional class add-ons | about 760 with all candidates | all of the above | Witcher alone is 192 items and adds ores |

Things to watch when they are added:
1. **Villagers and structures.** Wizards, Archers, Rogues, Paladins and Bard add villager workstations and structure pools; this matters in Verdant (villages exist) and Liminal, not in the void or ship packs.
2. **Recipe clutter.** About 54 to 760 items per pack in the recipe viewer; the gear-role pass is still the way to keep that readable.
3. **Netherite and crystals.** Each class mod's top tier needs netherite, upgrade crystals and an Armory RPGs item; the player route for those is in `required-resources.md`.
4. **Spell Engine is one more spell system** in Elysian; the niches decided in `elysian-review.md` still apply.
5. **Pin consistency.** Elysian and Liminal already carry Player Animator and GeckoLib; Verdant and Influx do not carry Player Animator.

## Verdant defense mod

Decided: Mekanism Turrets & Fences is Verdant's automated-defense mod (`verdant-defense-options.md`): `packwiz modrinth add mekanism-turrets` (Modrinth slug `mekanism-turrets`; CurseForge name "Mekanism Turrets & Fences"). It needs Mekanism (present) and GeckoLib (present in Verdant), so no new library.


## Script

`scripts/add-decided-mods.sh <pack-repo-dir> <modrinth|curseforge> <verdant|elysian|influx|liminal>` loops over the adds above for one pack, then runs `packwiz refresh`. Archers and Rogues & Warriors are CurseForge slugs, so run those with the `curseforge` source.
