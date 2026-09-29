# The Road to Liminal

**Design method: Liminal first.** The series is designed backwards. Liminal is the end state; Verdant, Elysian, and Influx are scoped so that each one builds a piece of the road to it. When two packs disagree, or a pack drifts off the road, the fix is decided by asking *what does Liminal need?* — then the earlier pack is adjusted, not Liminal.

> Series index: [`README.md`](README.md) · Story: [`story.md`](story.md) · Roles and mods: [`pack-architecture.md`](pack-architecture.md)

## The end state (what Liminal delivers)

- **The philosophy.** *Magic is just technology with a better marketing department.* It lives in Liminal (the Unified Theory chapter) and nowhere else in full. Other packs only hint at it. *(The term "TechnoMage" is retired — it is a trademark risk. Use "Unified Theory" or the philosophy line.)*
- **The Veil, explained.** What it actually is and why it existed — see [The Veil — Reveal Ladder](story.md#the-veil--reveal-ladder).
- **The three literacies reunited.** Mechanical (Verdant), magic (Elysian), lab (Influx) run as parallel paths and are bridged. A player who did the earlier packs recognizes every system; a player arriving cold learns from a progressive Field Manual.
- **A lived, hostile world.** A pod carries the player down and crash-lands; there is no way back to the ship. The biosphere pushes back (Resistance). The player settles (Colonial Settle) — Liminal owns colony features.
- **The review closes.** *"You are ready"* — ready for what is not stated — then silence. The Entity and the destination question stay open on purpose.

## The road: what each pack does for Liminal

| Pack | Setting | Builds the literacy for | Sets up for Liminal | Must **not** reveal |
|---|---|---|---|---|
| **Verdant** | Virtual (simulation) | Mechanical Path — engineering: sieving, automation, storage, power, networks | The word "Veil" (only the word); the player as an engineer | Anything about magic being technology |
| **Elysian** | Virtual (simulation) | Magic Path — obtaining with spells, essence, and spirit labor; *using* the Veil | The practice of projecting mystery and power; magic on its own terms | What is underneath the practice; that it is technology |
| **Influx** | Aboard the *Longwatch*, in flight (real) | Lab Path — closed loops, conversion, breeding, compact automation (AE2), power scale | The ship as the *Longwatch*; the observation that different vocabularies give the same output | That the overlap is deliberate |
| **Liminal** | The planet — pod crash-landing (real) | All three, reunited | — | Delivers the reveal |

**Hinting rule.** "Hint" means the player can notice a pattern; it never means a character or document states the thesis. If a line could be quoted as "so magic is just technology," it belongs in Liminal.

## Scoping test for anything in packs 1–3

Before adding or keeping a mod, quest, or story beat in Verdant, Elysian, or Influx, ask:

1. Does it build a literacy Liminal's path chapter assumes?
2. Does it keep to that pack's step of the reveal (nothing ahead of the ladder)?
3. Is it something Liminal would be worse without?
4. If it is a mod that lives in another pack, is there a stated reason it is here — and is it doing a job no other mod in this pack already does?

If it fails, cut it or move it. Multiple routes to the same resource are fine; exact duplicates are trimmed (see [`mod-audit.md`](mod-audit.md)). If it fits the theme but not the road, discuss it before it ships.

## Congruency log

Conflicts found between packs and how the end state resolved them.

| Conflict | Resolution (serves Liminal) |
|---|---|
| Veil was explained openly in Part One, then "revealed" as a twist in the finale | Reveal ladder: Verdant the word, Elysian the practice, Influx observations, Liminal the truth |
| Cohort name: canon said `CP-Verdant-S1` throughout; Elysian/Influx quests said "Cohort CP-Elysian/Influx" | The **cohort** is always `CP-Verdant-S1` (Liminal's ending line uses it). Each pack is a **module**: "Module 2 · CP Elysian", etc. Quest text updated. |
| Elysian's contingency ("existing civilization") had no civilization in a void pack | Reframed as *being met*: the void is the rehearsal stage; the exercise is projecting mystery and power. |
| Influx's ship vs. the *Longwatch* was undefined | Influx's ship **is** the *Longwatch*. The navigation-directive fragment lands in Influx, and the ship that confines you is the ship that lands you at Liminal. |
| Quest stub said "leave the ending open" while the finale delivers the reveal | The philosophy lands fully in Liminal; what stays open is the Entity and "ready for what." |
| Too many program names (Colonial Program, Colony Protocol, Cohort Protocol) | Colony Protocol = the overarching program all ships were sent under (and the series name); Cohort Protocol = the training modules; CASPAR = the AI. "Colonial Program" is retired. |
| Every pack was framed as the simulation | Modules 1–2 are virtual; module 3 is aboard the real ship (final practical); module 4 is deployment — a pod crash-landing with no return. |
| "TechnoMage" is a likely trademark | Retired; the chapter is "Unified Theory." Internal file names and placeholder advancement IDs renamed too. |
| Translocators was removed from Elysian and Liminal | Kept for Liminal (non-powered, magic-flavored transfer); out of Elysian for now since Starbuncles and Ender Storage cover it. |
| Colony features had no owner | Liminal owns them (Verdant has villagers only) |

## Still open

- CASPAR's role once the frame changes (module 3 aboard the ship, module 4 on the planet) and what the player starts with after the crash landing.
- Colony mod for Colonial Settle (MineColonies is a candidate).
- Influx: power sources for Azurum Miner (and whether Mekanism's Digital Miner is a better fit); farming overlap; which AE2 addons. See [`mod-audit.md`](mod-audit.md).
- Liminal quest text beyond the stubs; the Field Manual voice for players arriving cold.
- Backfilling CASPAR voice and leak beats into Elysian, Influx, and Liminal quest text, guided by each pack's `docs/story.md`.
