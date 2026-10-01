# Elysian: partial-fit review (first pass)

Elysian's theme: **shape what you cannot craft**. Void start; magic obtains what you cannot mine (spells, essence crops, spirit labor); no FE power system; capstone is Gateways to Eternity (a portal opens, mobs come through, you fight). Combat classes chosen for Elysian: Wizards and Rogues & Warriors (`capstones-and-gear.md`).

Method: for each mod rated partial or poor, ask (a) does it fill a named gap, (b) does it add enough content, (c) does it add a system the pack already has an answer for. These are **leanings to argue from, not verdicts**; every one is open to the maintainer's call. Item counts come from `scan/`.

## First, a systems count the Wizards decision raises

Elysian already has several spell and magic systems:

| System | Mods (items) | Job today |
|---|---|---|
| Ars Nouveau (Source) | Ars Nouveau + Elemental (160), Elemancy (105), Zero (113), Additions (65), Controle (8), Not Enough Glyphs (14) | Glyph spellcasting and Source automation |
| Iron's Spells | Iron's Spells 'n Spellbooks (341), Iron's Jewelry (13) | Combat spells, scrolls, spellbooks |
| Spell Engine (new) | Wizards (53), plus Spell Engine library | Class staffs, wands, robes |
| Occultism and Theurgy | spirits, ritual, alchemy | Labor, materials |
| Mystical Agriculture | essence crops | Resources |

Three spellcasting systems (Ars, Iron's, Spell Engine) and at least four staff families (Ars Zero staffs, Iron's staffs, Wizards' Arcane/Fire/Frost staffs, Ars Elemental foci) is exactly the "27 ways to do one thing" the series avoids in packs 1 to 3. This is the main thing to settle before judging the individual Ars add-ons. Options: (1) give each a niche (Ars = utility and Source, Iron's = combat spells, Spell Engine = class kit and looks), (2) drop Wizards from Elysian and keep only Rogues & Warriors there, moving Wizards to Liminal, (3) drop the Iron's line. Not decided.

## Mod by mod

| Mod | Items | Leaning | Why |
|---|---|---|---|
| Apotheosis | 66 | Keep, tied to Gateways | Affixed gear, gems and boss loot are what Gateways pays out; it is how the capstone rewards the factory. The earlier "needs dimensions" worry is about Apotheosis bosses, not Gateways. Check which of its systems we actually want. |
| Apothic Enchanting | 52 | Keep with Apotheosis | Depends on it; adds the enchanting shelves (a progression of its own). |
| Apothic Spawners | 1 | Revisit | One item (a spawner tweak). Only earns its place if Elysian uses spawners. Decide with the first-mob-soul question (see `required-resources.md`). |
| Gateways to Eternity | 2 | Keep (capstone) | Two items, but the whole capstone. Needs a cost the player automated. |
| Ars Elemental | 160 | Keep as the Ars depth | Already provides turrets, relays and elemental schools; large and used. |
| Ars Elemancy | 105 | Question | Armor and foci for Elemental. Another armor family; passes the every-item-has-a-job test only if its armor has a niche or a look we want. |
| Ars Zero | 113 | Question | New cast devices and glyphs, mostly staffs and circlets. Direct overlap with Iron's and Wizards staffs. |
| Ars Additions | 65 | Keep, low cost | Mostly decoration (sourcestone, archwood lanterns) plus tweaks: a stage-6 expression sink, matching the decoration point from earlier. |
| Ars Controle | 8 | Question | Eight utility items (relays, remotes). Small; is it a named gap or "one of 27 items"? |
| Not Enough Glyphs | 14 | Question | Extra glyphs and foci for Ars. Small addition to a mod we already have deeply. |
| Iron's Jewelry | 13 | Keep if Iron's stays | Accessory layer for Iron's Spells; also needs Iron's Lib, whose source repo is still missing. Gems it uses (ruby, sapphire and so on) need a route. |
| Farming for Blockheads | 12 | Keep, check | Gives a Market, Chicken Nest and Feeding Trough: the animal husbandry that leather, wool and string need in a void start, and that Mystical Agriculture's mob crops (pig, cow, sheep) tie to. Fills a real gap if animals are otherwise absent. |
| Tough As Nails | 51 | Question | Thirst and temperature are a survival-pressure system, with the survival data pack in Verdant, Elysian and Liminal. Fits stage 0 (shelter, food) but conflicts with the "calm teacher" Verdant idea. Decide per pack. |
| Wooden Shears | 1 | Replace | One item; matches the "not one of 27 items" rule. A KubeJS recipe or tag change could give the same early shears with no jar. In all four packs, and Verdant issue #331 is open. |
| Mystical Automation | 7 | Lean cut | FE machines in a pack with no power system. Elysian's automation is covered by Botany Pots hoppers, Occultism spirits, Theurgy logistics and Sophisticated upgrades (see `cleanup-findings.md`). Revisit only if Elysian adopts a power answer. |

## Where this leaves Elysian

- **Settle first**: the spell-system count (three systems, four staff families). Everything under the Ars add-ons depends on it.
- **Fairly clear**: Gateways, Apotheosis, Apothic Enchanting, Ars Elemental, Ars Additions, Iron's Jewelry (if Iron's stays) and Farming for Blockheads stay for now. Wooden Shears and Mystical Automation lean out.
- **Open**: Apothic Spawners, Ars Elemancy, Ars Zero, Ars Controle, Not Enough Glyphs, Tough As Nails.

## Decisions (maintainer)

- **Removed from Elysian**: Wooden Shears, Mystical Automation, Apothic Spawners, Ars Elemancy, Ars Controle, Not Enough Glyphs. Done in the Elysian repo (SpecterRealm/minecraft-modpack-cp-elysian#38). Wooden Shears is also in Verdant, Influx and Liminal; only Elysian was decided, so the others stay until each pack is reviewed.
- **Wizards stays in Elysian.** Option 1 from the spell-system count: each system gets a niche (Ars for utility and Source, Iron's for combat spells, Spell Engine for the class kit and looks). The staff overlap (Ars Zero, Iron's, Wizards, Elemental foci) still needs a gear-role pass; Ars Zero stays open.
- **Still open**: Ars Zero, Tough As Nails (calm Verdant question), and the unchanged keeps.
- **Liminal** keeps the union for now; these six mods are still in Liminal and need their own reason there or removal later.

## Next

1. Maintainer call on the spell-system count.
2. Then re-rate the open mods; update `profiles.json` (status moves from `pending` only once decided).
3. Repeat for Verdant's 9 partial and Influx's 4.
