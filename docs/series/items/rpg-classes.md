# RPG class mods: what is chosen, what is being reviewed

Spell Engine is the shared base. Class rollout chosen so far (`capstones-and-gear.md`): **Verdant** Archers, **Elysian** combat classes (Wizards, Rogues & Warriors), **Influx** utility classes (Paladins & Priests), **Liminal** all. A cosmetic armor layer is in every pack. Nothing below is added; this is a first read.

## Chosen mods (scanned earlier)

Spell Engine (library), Wizards (53 items), Archers (48), Rogues & Warriors (61), Paladins & Priests (74).

## Candidates supplied by the maintainer (scanned, source at the 1.21.1 branches)

| Mod | Repo | Items | Class job | Notable |
|---|---|---|---|---|
| Berserker | `ProfessorFichte/Berserker-RPG-Class` | 33 | Melee: raid axes, Northling armor; "Rage" (less health, more damage) | Netherite tier; top-tier recipes use upgrade crystals and an Armory RPGs item |
| Bard | `ProfessorFichte/Bards` | 68 | Support: lyres, lutes, rapiers, harp crossbows, Luthier villager | Needs Structure Pool API and Ranged Weapon API as well |
| Forcemaster | `ProfessorFichte/Forcemaster` | 34 | Martial artist: knuckles and suits, plus spells | Netherite tier, amethyst shards |
| Witcher | `ProfessorFichte/Witcher-RPG-Class` | 192 | Full kit: silver and steel swords, glyph signs, medallions, traps, diagrams | **Adds its own ores** (silver, dark iron, meteorite) and metals (steel, dimeritium); 17 diagram tiers per gear piece |
| Elemental Wizards | `ProfessorFichte/Elemental-Wizards-RPG-Class` | 75 | Earth, water, air robes and spells | Extends Wizards (needs it); netherite and warden-crystal tiers |
| More RPG Library | `ProfessorFichte/More-RPG-Library` | 17 | Shared library: runes, bear and wolf fur, hardened leather, "Lost Crystals" | Required by every add-on above |
| AzureLib Armor | `AzureDoom/AzureLib-Armor` | library | Armor model rendering | **Repo archived April 2026** (read-only); required by the add-ons |

## What they cost in dependencies

Each add-on needs Spell Engine, More RPG Library, AzureLib Armor and (Bard) Structure Pool API and Ranged Weapon API. So one more class costs little after the first, but the first costs a **library chain**: More RPG Library, AzureLib Armor, and the extra APIs. AzureLib Armor being archived is a maintenance risk.

## Fit, and what needs deciding

- **Base tiers** are iron, gold, leather, string, chain, amethyst and wool: all reachable by the packs' own routes (see `required-resources.md`).
- **Top tiers** follow the pattern already found: netherite, plus **upgrade crystals** (More RPG Library "Lost Crystals", likely loot or boss drops) and an **Armory RPGs** item (`armory_rpgs:epic_armor_upgrade`, a separate mod the add-on only references as optional; not read in detail). Without those, the top tier of each add-on may not be craftable; the real source of the Lost Crystals needs a read.
- **Witcher is a mod pack inside a mod**: ores, a metal chain and 17 diagram tiers. That conflicts with the no-ore rule in packs 1 to 3 and with "one family per niche per tier". It fits **Liminal** only, if at all.
- **Berserker, Forcemaster and Elemental Wizards** are combat classes: they match the Elysian role, but add more spell and armor families to a pack that already has three spell systems (`elysian-review.md`). Elemental Wizards overlaps Wizards directly.
- **Bard** is a support class and fits the Influx utility role next to Paladins & Priests.
- **Gear roles**: with these, the pack has many armor and weapon families. The gear-role pass in `capstones-and-gear.md` has to happen before adding more than one or two.

Suggested starting point (a leaning, not a decision): Elysian keeps Wizards plus Rogues & Warriors for now; consider **one** of Berserker or Forcemaster as a third combat class only after the gear-role pass; Influx adds Bard; Witcher and Elemental Wizards wait for Liminal.

## Liminal add: NoCubes Sea Dwellers

Maintainer suggests it for Liminal. CurseForge lists it as "Realm RPG: Sea Dwellers" (author BlackAuresArt, NeoForge 1.21.1 builds): underwater villages and sea traders. **No public source repo found**, so it cannot be scanned. **Liminal already carries an `underwater-village` structure mod (SuperWarioModTeam, no repo found either)**, so these two would overlap. Decide which to keep once either has a source.

## Open

1. Which class add-ons go to which pack, after the gear-role pass.
2. Read where the Lost Crystals come from and whether Armory RPGs is needed.
3. Find a source repo for NoCubes Sea Dwellers; resolve the overlap with the underwater village.
