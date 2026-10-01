# Verdant: partial-fit review (first pass)

Verdant's theme: **learn to grow what you cannot mine**, played calm like Factorio on peaceful mode ("teach how to fish before you are shipwrecked"). Real overworld (Terralith), ore worldgen off, Ex Deorum sieving for metals, Create then Mekanism then AE2, capstone is a megabuild with automated defenses and a finished quest book (the quest book waits until mods are locked). Archers is the chosen class; a cosmetic armor layer is in every pack.

Same method and caveat as `elysian-review.md`: leanings to argue from, not verdicts. Item counts from `scan/`; usage from Verdant's quests and KubeJS scripts. The earlier "9 partial" count was missing two poor fits and two newer mods, so 11 rows are below.

## Systems check first

Verdant has many power sources: Create alternator, Mekanism generators, Powah, Extreme Reactors, Better Fusion Reactor, plus Flux Networks to move power. They are all **FE**, so by the "count systems, not mods" rule they are one system with tiers, not separate systems. The question for each is whether it is a distinct tier or just another way to do the same thing.

## Mod by mod

| Mod | Items | Used in Verdant | Leaning | Why |
|---|---|---|---|---|
| Extreme Reactors | 146 | Quest chapter "Scale": reactor and turbine controllers, wrench | Keep if yellorium gets a route; else question | It is the big-multiblock power tier and has real content and quests. The earlier concern ("fuel needs ore; no sieve recipe") has a known fix pattern: an Ex Deorum sieve recipe through the KubeJS Ex Deorum add-on, like Verdant's blazing path. Not built. Also in Influx and Liminal. |
| Better Fusion Reactor for Mekanism | 14 | One **optional** quest in the Scale chapter (nothing depended on it); doc mentions | Lean cut | Harder fusion reactor, late, ore-dependent, overlaps Mekanism's own fusion and fission. (Corrected: the first draft said it had no quest reference; it had this optional one.) |
| Building Gadgets | 9 | A KubeJS recipe (`gadget_computing_recipes.js`) already changes the building gadget to need computing parts | Keep, stage-6 niche | FE-powered copy and paste suits the **megabuild** capstone. Overlaps Building Wands, so give them different jobs: Wands early and manual, Gadgets late and powered. |
| Charging Gadgets | 1 | No references | Lean cut | One item (a charging station). Elysian already removed it; Flux Networks charges items. Matches the "not one of 27 items" rule. |
| Mekanism Tools | many | No quests or scripts (the MekaSuit gate script is for core Mekanism) | Lean cut | Mekanism Tools mostly repeats what Silent Gear already does (paxels, tiered sets). The MekaSuit lives in core Mekanism, so cutting this jar does not remove it. Check that no recipe or quest needs a Mekanism Tools item before removal. |
| Mekanism Unleashed | 0 | No references | Question | A config-style change (higher upgrade limits, more operations per tick). If Mekanism's own config exposes the same knobs, it can be replaced by a config edit. Not verified. |
| More Thermal Evaporation | 37 | Scale quest uses its controller; one script fixes recipes | Keep for now | In use. It adds sizes, not a new system; revisit if brine volume is not a bottleneck. |
| Mob Grinding Utils | 49 | Heavily gated by `mob_grinding_utils_gates.js`; Blazing Path uses its magma cube farm for sustained blaze powder | Keep | Earlier note "overlaps Hostile Neural Networks" does not apply in Verdant (no HNN here). The Nether bootstrap depends on it. |
| Tough As Nails | 51 | Thermoregulator quest, Field Manual armor insulation page, early leaf armor, one script | Keep, with a flag | Thirst and temperature are survival pressure, not combat, and are deeply wired into early Verdant. The "calm teacher" idea applies to mobs, not to hunger and heat. Decide whether you want that pressure; it is the first thing a player meets. |
| Farming for Blockheads | 12 | No references | Question | Gives Market, Chicken Nest and Feeding Trough. Elysian needs animal husbandry in a void; Verdant has animals and villages in the world. Likely not needed here. |
| Dummmmmmy | 1 | No references | Question | One item, a target dummy. Useful for the gear-role pass, but a single item. |

## Where this leaves Verdant

- **Lean cut**: Better Fusion Reactor, Charging Gadgets, Mekanism Tools.
- **Keep**: Mob Grinding Utils, More Thermal Evaporation, Building Gadgets (as the late building tool), Tough As Nails (flag).
- **Conditional**: Extreme Reactors (needs a yellorium route), Mekanism Unleashed (config replacement?).
- **Open**: Farming for Blockheads, Dummmmmmy.
- **Cleanup that follows a cut**: remove any KubeJS or quest references first. Extreme Reactors and Building Gadgets have them; Better Fusion Reactor had one optional quest; Mekanism Tools and Charging Gadgets had none found.

Nothing is removed. The quest book is not touched until the mods are locked.

## Decisions (maintainer)

- **Removed from Verdant**: Better Fusion Reactor (its optional quest and doc rows too) and Mekanism Tools, in MichaelHeaton/minecraft-modpack-cp-verdant#339. Maintainer later decided to remove both from **all packs**; Liminal was the only other pack with them (done in the Liminal pack files).
- **Early-leaf recipe approved**: 2 saplings and a stick make 4 oak leaves, replacing Wooden Shears (ticket #331); still needs a playtest.
- **Charging Gadgets**: kept for now (maintainer). Original question below. Question raised: what happens to Building Gadgets without it. Findings: the Charging Station burns any fuel item into FE and charges a gadget in its slot (works before the pack has any power system). Building Gadgets hold 500,000 FE and cost 50 FE per block placed (100 per exchange), and Verdant's recipe already needs an AE2 calculation processor, so by then the player has FE sources. Removal would not change the gadget recipe, only how it is charged; another charging route (an energy cube slot or similar) should be confirmed in game before relying on it.

## Next

1. Maintainer call on the leanings above.
2. Then Influx's partial fits.
3. Then a cross-pack check of mods that stay in Liminal's union.
