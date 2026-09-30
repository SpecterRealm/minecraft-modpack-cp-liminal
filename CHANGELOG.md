# Changelog

## [Unreleased]

### Mod stack

- **Removed:** KubeJS Mekanism Extends. It only extends Mekanism add-ons (Evolved Mekanism, More Machine, Mekanism Sun), and none are in the pack, so it did nothing.
- **Changed:** Essential Mod is now client-only (`side = "client"`), so servers do not install it while players' clients still get it from the pack (friends list, cosmetics, world hosting).
- **Restored:** Productive Farming (removed in error as a "duplicate" of AgriCraft; also restored in Influx). Keeping both crop mods is tracked in Influx #31.

### Docs

- Full mod audit started: added `scripts/series-mod-inventory.py` and the generated `docs/series/mod-inventory.md` (every mod by which packs ship it), plus first-pass observations in `mod-audit.md`.
- Mod audit: EMC stated as the destination (Star Trek-style replicator); crops and trees decisions recorded; tickets linked (Influx #28, #29).
- Naming: Colony Protocol is the overarching program, Cohort Protocol is the training modules, CASPAR is the AI ("Colonial Program" retired). Modules 1–2 are virtual, module 3 is aboard the real ship, module 4 is a pod crash-landing with no return. "TechnoMage" retired (trademark risk) in favor of "Unified Theory" — chapter renamed. Translocators stays in Liminal and Elysian. Liminal deliberately leaves open whether you are really on the planet or still in training. Added `docs/series/mod-audit.md` and the "every mod needs a reason" rule.
- The Veil is now a three-step reveal (Verdant: the word; Elysian: how to use it; Influx: observations; Liminal: what it is). Colony/settlement features assigned to Liminal. Added `docs/story.md` and updated mod counts (207).
- Vigil / LTM (`minecraft-modpack-ltm`) is cancelled. Liminal is now the series finale and absorbs the revelation, the closing of the behavioral-review thread, and the world-history hooks. Removed Vigil from the series hub and story canon.
- Liminal is now the series source of truth: added `docs/series/` (hub, story canon, pack architecture, archived planning notes).
- Fixed stale mod counts (Liminal is 208 = Verdant ∪ Elysian ∪ Influx + Liminal-only) and removed pointers to design docs that live outside the repos.
- Added `docs/series/road-to-liminal.md`: the series is now designed Liminal-first. Story fixes from it: cohort is always `CP-Verdant-S1` (each pack is a module), Elysian's contingency reframed as being met, Influx's ship is the *Longwatch*, TechnoMage philosophy line added, TechnoMage quest stub reconciled.

## [0.1.0]

- Initial packwiz scaffold (NeoForge 1.21.1)
- Soft-pin shared QoL / quest / storage / EMI stack from Verdant pins
- Empty FTB Quests tree + KubeJS skeleton (content TBD)
