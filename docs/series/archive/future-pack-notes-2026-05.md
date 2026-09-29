# Future Pack Notes — archived planning (2026-05)

> **Archived. Not current.** These notes predate the pack restructure and use the old lineup (P2 "Magic Pack", P3 "Convergence" skyblock/genetics, P4 "Hostile Contact"). The current roles are in [`../pack-architecture.md`](../pack-architecture.md) and the current story is in [`../story.md`](../story.md).
> Mapping: old P2 → **Elysian** · old P3 → split between **Influx** (ship, closed loops, genetics) and **Liminal** (reunite tech + magic) · old P4 → **Liminal** (settle, resist) · LTM → **Vigil**.
> Kept for the mod-candidate research and design rationale only.

# Future Pack Notes

Ideas and mods flagged during CP: Verdant development for use in later packs.

---

> **TLDR**
> - **The whole series is a slow reveal:** magic is just technology with better branding
> - **Packs + LTM (series is open-ended):** P1 = no ore veins, P2 = existing civilization, P3 = skyblock void, P4 = hostile native life; more contingency modules may be added; LTM grows with each release
> - **Escalating contingency:** each pack trains for a harder arrival scenario; P3 is worst-case
> - **Ender Pearls are the throughline** — their meaning evolves in every pack
> - **Pack 2's design gap:** no existing modpack gives magic the same quest depth as tech — this is the opportunity
> - **Pack 3 is the rehearsal** — skyblock forces both tech and magic skillsets; trains players for LTM colony management
> - **LTM is the sum of all packs** — players who did the packs recognize everything; players who didn't have no frame for it

---

## 🧙 Series Narrative — The TechnoMage Arc

**The thesis:** Magic is just technology you don't understand yet.

Inspired by the TechnoMages of Babylon 5 — humans who wielded technology so advanced, so precisely cultivated to resemble the impossible, that even they began to lose track of where the engineering ended and the mystique began. Clarke's Third Law made playable across the CP series:

> *"Any sufficiently advanced technology is indistinguishable from magic."*

**The CP series is built around a slow reveal.** Players who start in Pack 1 are engineers. Players who start in Pack 2 think they are mages. By the time they reach the LTM pack, the truth comes out — and it reframes everything they did in every earlier pack.

---

### 🗺️ The Arc

**Pack 1 — CP: Verdant (Tech)**

**Pure engineering.** Ore becomes ingot becomes machine becomes network. The world is mechanical, rational, predictable.

Players learn to think like engineers: inputs, outputs, throughput, automation. The universe operates on rules, and the rules can be mastered.

---

**Pack 2 — (Magic Pack)**

**Players arrive in a world where something else is happening.** Flowers generate power. Stars channel force into crystals. Blood powers circles drawn on stone.

The systems are strange but suspiciously structured — rituals have precise geometric requirements. Spells follow grammatical rules. Mana flows through predictable channels. It *behaves* like engineering. But the aesthetic is entirely different. Players learn to think like mages: intention, alignment, attunement, sacrifice.

*What they don't know yet:* Botania flowers are phytoremediation arrays converting ambient RF through engineered petal compounds. Ars Nouveau glyphs are a gesture-recognition programming language running on distributed spellcasting drones. Blood Magic ritual circles are bioelectric harvesting arrays. Astral Sorcery lenses focus stellar radiation into coherent energy. The "ancient runes" are machine code. **The TechnoMages wrote a very good user manual and then burned the source code.**

---

**Pack 3 — Convergence (Farming + Genetics)**

**Tech and magic players share a world for the first time.** Working together, they start noticing things.

The crop mutations that look exactly like Mendelian genetics. The mana flowers that respond to light intensity like solar panels. The ritual circles that, rotated 45 degrees, look like circuit diagrams. The Genetic Synthesizer and the Ars Nouveau breeding spells arrive at the same output through completely different-looking inputs.

Quest text in Pack 3 should start dropping the hints — not stating the truth, but making the observation. "Interesting — both approaches arrive at the same output. Different language, same math."

---

**LTM — The Revelation**

**The final pack begins the same as the others, then a quest chain unlocks.** A Patchouli book appears in a chest: *"A Technical History of the Arcane Arts."* It's a dry academic text. It cites sources. It has footnotes. It explains, with diagrams, what every magic system in Pack 2 actually was.

The chapter structure of the LTM pack's late game is the unified theory: showing that every tech system and every magic system is an instance of the same underlying physics, described in different vocabularies by people who never spoke to each other. The AE2 network and the Blood Magic sigil network are both graph-based distributed computation systems with node priority routing. The ME Controller and the Ars Nouveau Archwood tree are both power distribution hubs with channel/mana budgets.

**Players who finished Pack 1 recognize the technology in what they thought was magic. Players who finished Pack 2 recognize the magic in what they thought was just engineering.** The convergence *was always the point.*

---

### 🎛️ Design Implications for Each Pack

**Pack 2 mod selection criteria (in addition to fun):**
- Choose magic mods whose systems have plausible technology explanations
- Avoid mods that are purely cosmetic ritual with no structured mechanic
- Prioritize mods where the progression *feels* like mastery (not luck)
- Botania, Ars Nouveau, Blood Magic, Astral Sorcery all qualify: their systems have precise, learnable rules that read differently depending on your vocabulary

> 💡 **Design rule:** If a magic mod's mechanics can't be explained with a straight face as "advanced technology," it probably doesn't belong in this series.

**Pack 3 quest writing criteria:**
- Convergence quests explicitly note when tech and magic solutions match
- "Both paths produce the same result. The method is different. The output is identical. File that observation away."
- Never state the thesis directly — let players arrive at it

**LTM quest writing criteria:**
- The revelation chapter should feel earned, not sudden
- The Patchouli book should be in-universe academic writing, not a fourth-wall break — written as if the discovery was made by scholars inside the game world, not by the pack developer
- Players who did both Pack 1 and Pack 2 should have an "of course" moment; players who only did one should have a "wait, what" moment

---

**Ender Storage note:** Moved from Pack 1 to Pack 2.

**In Pack 1 it reads as inexplicable magical teleportation** — the "Ender" name, the color-coded frequency system that works across dimensions without cables. In Pack 2 it is presented as standard magical infrastructure.

In the LTM revelation, the Ender Chest is revealed to be a quantum-entangled storage matrix with a frequency-keyed resonance lock. It was always tech. The name was marketing.

---

**Ender Pearl arc (cross-pack narrative thread):**

**Ender Pearls appear as crafting components across virtually every mod that involves spatial manipulation** — AE2 Quantum Rings, Mekanism Teleporter parts, and many others. This is the TechnoMage arc's most persistent background thread.

- **Pack 1 (CP: Verdant):** The Patchouli "Field Notes" entry on Ender Pearls makes the observation without explanation. Detached, clinical. Notes the pattern. Notes that the crystalline internal structure doesn't look biological. "The researcher who wrote this section did not file a follow-up." No conclusion offered.

- **Pack 2 (Magic Pack):** Ender Pearls are presented as dimensional foci — "the crystallized attunement of a creature that exists between worlds." The magic vocabulary fully frames them as mystical components.

- **Pack 3 (Convergence):** Quest text begins noticing the overlap. A Patchouli observation that the pearl's response to dimensional energy is consistent across both the tech and magic uses. "The thing being leveraged is the same thing. The vocabulary is different. The physics is identical."

- **LTM (Revelation):** The "Technical History of the Arcane Arts" chapter on Ender Pearls. The Enderman is a naturally occurring quantum tunneling organism — its teleportation is biological, not supernatural. The pearl is the physical substrate of that ability: a crystallized coherent quantum state matrix that stores dimensional coordinates. When thrown, it completes a short-range spatial fold using residual coordinate memory. Every mod that uses pearls in "dimensional" crafts is leveraging the same underlying mechanism. **The Endermen are not mystical. They are, in a meaningful sense, the only naturally evolved engineers this world ever produced.**

---

## ✨ Pack 2: Magic-Based Quest Pack

**Design Philosophy:** "Learn to shape what you cannot craft."

Where CP: Verdant forces the player through tech automation, Pack 2 forces mastery of magic systems — transmutation, ritual, enchanting, blood, and botany — before any industrial shortcut is available. Tech mods present but gated behind magic milestones.

**Informed by CP: Verdant research findings (May 2026):**
- **Magic mods are the single most chronically under-documented category** across all major modpacks. A pack that gives magic mods the same quest depth as tech mods will stand out.
- Research found zero examples of a pack that treats magic progression with the same chapter-level structure that CP: Verdant uses for tech. **This is the gap to fill.**
- Blightfall (HQM, 2014) remains the gold standard for narrative quest design and was specifically magic/exploration adjacent. No pack has replicated it in a tech-magic hybrid.
- The "quest as encyclopedia" pattern (GTNH) is especially valuable here: magic mod recipes and rituals are the content players most frequently alt-tab to look up.

---

**Phase concept (draft):**

| Phase | Theme | Example Mods |
|-------|-------|--------------|
| 1 - Discover | First sparks — alchemy, basic rituals | Botania, Ars Nouveau basics |
| 2 - Bind | Blood contracts, soul magic, sacrifice loops | Blood Magic, Malum |
| 3 - Transmute | EMC economy, equivalent exchange | ProjectE, AppliedE |
| 4 - Ascend | Ritual automation, mana machines | Botania automating via Create or IF |
| 5 - Command | Unified magic control, narrative ending | CC:Tweaked magic dashboard, Ars + AE2 |

---

**Core design rules for Pack 2:**
- No ore worldgen (same as CP: Verdant) — resources come from transmutation and rituals
- Tech mods (Create, Mekanism) available but gated behind late-Phase 3 magic milestones
- Every magic system gets its own chapter with the same quest depth as CP: Verdant's tech chapters
- **Reward philosophy: rewards should be *materials for the next ritual*, not XP** (lesson learned from CP: Verdant research — XP-only rewards are universally disliked)

> ⚠️ **Note:** XP-only rewards are universally disliked in modpack research. Never use them as the primary reward in a chapter.

---

**Mod candidates:**

| Mod | CurseForge | Notes |
|---|---|---|
| ProjectE | https://www.curseforge.com/minecraft/mc-mods/projecte | Equivalent Exchange / transmutation — core magic progression loop |
| AppliedE | https://www.curseforge.com/minecraft/mc-mods/appliede | ProjectE + AE2 integration — autocrafting with EMC |
| Botania | https://www.curseforge.com/minecraft/mc-mods/botania | Flower-based mana system; automation-friendly; strong quest narrative potential |
| Ars Nouveau | https://www.curseforge.com/minecraft/mc-mods/ars-nouveau | Spell crafting system; glyph progression maps cleanly to quest chapters |
| Blood Magic | https://www.curseforge.com/minecraft/mc-mods/blood-magic | Ritual/sacrifice loop; Blightfall-style reputation economy possible |
| Malum | https://www.curseforge.com/minecraft/mc-mods/malum | Dark/soul magic; aesthetic cohesion with Blood Magic |
| Apotheosis | https://www.curseforge.com/minecraft/mc-mods/apotheosis | Moved from CP:V — Chronicle of Shadows + gem socketing fits Phase 1-2 here |
| Waystones | https://www.curseforge.com/minecraft/mc-mods/waystones | Moved from CP:V — stone monuments with arcane inscription are natural magic infrastructure; LTM reveals as quantum-entangled teleportation terminals |
| Ender Storage | https://www.curseforge.com/minecraft/mc-mods/ender-storage-1-8 | Moved from CP:V — "Ender" dimensional storage fits as standard magical infrastructure; LTM: quantum-entangled storage matrix with frequency-keyed resonance lock |
| Occultism | https://www.curseforge.com/minecraft/mc-mods/occultism | Demon summoning/storage; ritual-first progression |
| Astral Sorcery | https://www.curseforge.com/minecraft/mc-mods/astral-sorcery | Starlight rituals; strong "discovery" phase candidate |
| Iron's Spells | https://www.curseforge.com/minecraft/mc-mods/irons-spells-n-spellbooks | Combat magic; gives the player something to *do* with magic power |
| Patchouli | https://www.curseforge.com/minecraft/mc-mods/patchouli | In-game guidebook mod; critical for magic packs — pairs with quest encyclopedia pattern |

---

**In-game documentation strategy:**

Most magic mods ship with Patchouli guidebooks (Botania's Lexica Botania, Ars Nouveau's Worn Notebook, etc.). **Pack 2 should:**

1. Surface these books as quest rewards at the start of each magic chapter
2. Use FTB Quests item fields to link key crafting targets inside quest descriptions
3. Consider a custom Patchouli "Pack Guide" that covers cross-mod interactions the individual mod books don't explain (same gap GTNH's quest book fills)

---

## 🌱 Pack 3: The Convergence Pack — Skyblock, Synthesis, and Creation
🔍 *Updated: P3 is now a skyblock pack (void start). Design philosophy, phase table, and design rules all rewritten to reflect synthesizing soil/ore/creatures/villagers from nothing.* Delete when reviewed.

**Design Philosophy:** "Learn to build from nothing, together."

**Pack 3 is the skyblock pack.** The void. No world to land on. The worst-case contingency scenario — what do you do when the destination doesn't exist in any usable form?

Where Pack 1 trained players for a world without convenient ore, and Pack 2 trained players for encountering an existing civilization, **Pack 3 trains for the scenario where there is no planet at all.** You start with void and an island of dirt. Everything must be synthesized — the soil, the creatures, the ore, eventually the people. This is the terraforming module.

It is also the convergence. Pack 3 is where players of Pack 1 (tech) and Pack 2 (magic) meet on common ground for the first time. **Both skillsets are required.** You cannot terraform from void using only engineering. You cannot do it using only magic. The farming, genetics, and biology content that defines Pack 3's mid-to-late game is what you're building *toward* — establishing life where there was none.

This is intentional preparation for the LTM, where tech and magic players share the same world. Pack 3 is where they practice that collaboration under pressure.

> 💡 **Design rule:** Pack 3 is the rehearsal. Every design decision should be asking: "Does this prepare players for the LTM?" The skyblock start is not a difficulty spike — it is the contingency scenario the whole arc has been building toward.

> ⚠️ **Key difference from a standard skyblock:** This is not "get an island, expand it." The *goal* is biological and civilizational synthesis — you are not just surviving, you are manufacturing the conditions for a colony. Create ore (not just find it). Summon and breed creatures with useful traits. Eventually synthesize villagers. The late-game problem is not resource generation — it is creating a world that can *sustain itself*.

---

**Informed by CP: Verdant mod review (May 2026):**
- Serene Seasons, Butchery, and AgriCraft were removed from CP: Verdant as off-theme
- **They are not cut — they are reserved as Pack 3 farming-layer content**
- Genetic Animals is the Pack 3 animal anchor (Mendelian genetics — same design language as AgriCraft's crop genetics)
- The tech and magic mods present are *reduced* versions of Packs 1 and 2 — enough to exercise learned skills, not enough to re-teach them from scratch

---

**The Two Paths (both lead to the same late-game problems):**

*Tech Path* — players who completed Pack 1:
- Create automates planting, harvesting, processing
- AE2 stores and routes genetic samples and harvested materials
- Mekanism processes animal byproducts industrially
- Industrial Foregoing Mob Duplicator scales the best genetic specimens

*Magic Path* — players who completed Pack 2:
- Botania's Agricarnation speeds crop growth with mana
- Ars Nouveau spells modify soil fertility and mutation rates
- Mystical Agriculture (reintroduced here in its proper context) provides the magical seed tier system as a complement to AgriCraft's science
- Blood Magic rituals accelerate animal trait expression

*Convergence problems* — where both paths must contribute:
- "The best genetic specimens need both magical enhancement AND industrial duplication"
- "Seasonal crop timing requires Create automation AND mana-powered growth acceleration"
- "Maximum yield requires AgriCraft stat maxing AND Botania soil enrichment"

---

**Phase concept (draft):**

| Phase | Theme | Tech Tools | Magic Tools |
|-------|-------|------------|-------------|
| 1 - Void | Start from nothing; make soil, make stone, make light | Ex Deorum skyblock recipes, basic sieving | Botania mana from flowers; earliest spells |
| 2 - Life | First crops; first creatures; establish a biome | AgriCraft crossbreeding; IF early mob processing | Ars Nouveau growth/spawn spells; MA starter seeds |
| 3 - Genetics | Selective breeding of crops and animals | Genetic Animals, IF Mob Duplicator | Blood Magic livestock rituals; magical trait acceleration |
| 4 - Civilization | Synthesize a villager population; build a functioning colony | Industrial processes for population bootstrapping | Ars Nouveau + Blood Magic ritual summoning |
| 5 - Convergence | Both paths required; the void becomes a world | Full automation + full magic running together; the planet sustains itself | |

---

**Mod candidates:**

*New in Pack 3 (farming/biology layer):*

| Mod | CurseForge | Notes |
|---|---|---|
| AgriCraft | https://www.curseforge.com/minecraft/mc-mods/agricraft | Core crop genetics anchor |
| Genetic Animals | https://www.curseforge.com/minecraft/mc-mods/genetic-animals | Core animal genetics anchor; 1.20.1 Forge confirmed |
| Serene Seasons | https://www.curseforge.com/minecraft/mc-mods/serene-seasons | Seasonal pressure; centerpiece here |
| Butchery + Alex's Mobs Addon | https://www.curseforge.com/minecraft/mc-mods/butchery | Full livestock processing loop |
| CropCraft (Crop and Craft) | https://www.curseforge.com/minecraft/mc-mods/crop-and-craft | RF-powered Genetic Synthesizer; verify 1.20.1 Forge |
| Thoroughbred | https://www.curseforge.com/minecraft/mc-mods/thoroughbred | Horse selective breeding; niche, optional |
| Productive Farming | https://www.curseforge.com/minecraft/mc-mods/productivefarming | 160 crops with traits; 1.21.1 only as of May 2026 — watch for port |

> ⚠️ **Note:** Productive Farming is 1.21.1 only as of May 2026. Check back before Pack 3 development starts.

*Carried from Pack 1 (tech layer — reduced scope):*
- Create (harvest automation, logistics)
- AE2 (genetic sample storage, output routing)
- Industrial Foregoing (Mob Duplicator for genetic scaling)
- Farmer's Delight (full food chain now — more recipes unlocked)
- Farming for Blockheads, Botany Pots, RightClickHarvest

*Carried from Pack 2 (magic layer — reduced scope):*
- Botania (Agricarnation, soil enrichment runes, mana pool for growth)
- Ars Nouveau (growth and fertility spells)
- Mystical Agriculture (reintroduced — now in its magic context)
- Blood Magic (animal ritual mechanics)

---

**Core design rules for Pack 3:**
- **Skyblock start** — no natural world, no ore worldgen. Ore is synthesized (Ex Nihilo sieving, Mystical Agriculture ore seeds, Blood Magic transmutation)
- **Both tech AND magic are present but neither is taught from scratch** — Pack 3 assumes players bring one skillset and need to acquire working knowledge of the other
- Quest chapters have two parallel tracks for most phases (tech approach / magic approach) converging at Synthesis quests that require both
- The late-game goal is civilizational, not just resource-based: building a colony that functions without the player manually running it
- This is the direct training run for the LTM pack's dual-path chapter structure

---

## 🏰 LTM (Long-Term Multiplayer) Pack
🔍 *Updated: full LTM section written — colony mechanics (MineColonies candidates), between-module experience design, P4 hostile-landing/ruins concept, player-context asymmetry.* Delete when reviewed.

**The LTM is not another module. It is the ship.**

In the lore, players return to the LTM between every training module. It is the social and ambient layer — the simulation "common area" where crew members exist between assignments. In practice, it is a persistent multiplayer server that runs alongside and between all packs in the series.

**The LTM is also the sum of all packs.** Every mechanic from every released pack exists in the LTM world simultaneously — and grows as new packs ship. A player who drops in with no pack experience will encounter systems they don't have context for — colony management, magic infrastructure, genetic breeding programs — and they will simply not know why those things are there. A player who has worked through the series will recognize every thread. **The experience is not the same for both players, and that is intentional.**

---

### 🗺️ World Design

The LTM world is not clean. It is a world with history — the kind of history that implies previous occupants. Think abandoned infrastructure, partially functional systems, city ruins with things still running inside them. The world resists easy interpretation: is this what a previous ship left behind? Is this what Kethara looks like? Did something else build this?

> 💡 This is the narrative hook for the apocalyptic layer. The ruins exist. The lore does not immediately explain them. Players who paid attention to the P3 red leaks — specifically the "confirmed" coordinates that don't point to Kethara — will have a theory. Players who didn't will just be exploring ruins.

---

### 🏘️ Colony Mechanics

The LTM needs a **colony/settlement building layer** — a mod or mod combination that allows players to establish functional NPC colonies that operate semi-autonomously. Candidates:

| Mod | CurseForge | Notes |
|---|---|---|
| MineColonies | https://www.curseforge.com/minecraft/mc-mods/minecolonies | Full colony management — citizens, buildings, supply chains, research tree; 1.20.1 Forge confirmed |
| Structurize | https://www.curseforge.com/minecraft/mc-mods/structurize | MineColonies companion — building placement and blueprint system |
| Domum Ornamentum | https://www.curseforge.com/minecraft/mc-mods/domum-ornamentum | MineColonies companion — decorative block generation for colony buildings |

> ⚠️ **Note:** MineColonies is a significant system on its own. P3's "synthesize a villager population" quest chapter is explicitly designed to give players working knowledge of NPC management before the LTM drops full colony mechanics on them.

---

### 🛠️ Server Utility Mods

Mods that make sense for a persistent multiplayer server but not for the singleplayer training packs.

| Mod | CurseForge | Notes |
|---|---|---|
| FTB Essentials | https://www.curseforge.com/minecraft/mc-mods/ftb-essentials | `/home`, `/back`, `/tpa`, `/rtp`, `/spawn` — standard server QoL commands; not appropriate for P1-P4 survival training but right for the persistent LTM ship |

---

### 📡 The Between-Module Experience

After completing each pack, players are narratively returned to the LTM. The return isn't a hard transition — it's an event. A quest chain fires, CASPAR delivers a module-end debrief, and the player is cleared to access the LTM server.

**Players who haven't done a pack** will encounter those mechanics in the LTM but without CASPAR's framing. The systems work. The context isn't there. This is a feature.

**Players who have worked through the series** have a different LTM experience than players who have done nothing. The same physical space, different depth of interpretation. This is the payoff for the behavioral review thread that runs through every pack.

---

### 🌆 P4 — Hostile Contact (title TBD)

**Still a simulation.** CASPAR is present. The training frame holds. The colonists never actually land — P4 is an additional Colonial Program module added because probe data made it necessary.

**Why it exists in-universe:** P1, P2, and P3 are the original planned curriculum. P4 was not. A probe returned with data showing a biosphere classification the original training sequence didn't cover. CASPAR added the module under VCA Directive 7-C — standard adaptive curriculum protocols. The crew is told this is routine. Players who tracked the probe dispatch log from P2 onward will know which probe triggered it.

**The contingency scenario:** What if the destination has established native life — and it is actively hostile? Players arrive at a world that is fully formed, fully occupied, and treats colonists as a threat. This is the combat/survival module. Every skill from prior packs is assumed. The difficulty is not "figure out how the systems work" — the difficulty is deploying those systems under sustained pressure from a biosphere that pushes back.

**Why it fits the arc:**
- P1: The ground won't help you — extract resources the hard way
- P2: Someone's already there — navigate an existing civilization
- P3: There's nothing — build a world from void
- P4: What's there opposes you — survive and establish a foothold against active resistance

**Mod direction:** Harder mob packs, biome-specific hostile life, combat progression systems. Players bring their full tech toolkit (all prior packs assumed) and apply it defensively and offensively for the first time.

**Lore thread:** The "confirmed" coordinates from P3 red leaks connect here — the entity research fragments describe a biosphere that has changed in ways consistent with what P4 players encounter. Players who tracked the leaks recognize what they're in. Players who didn't just experience it as a hard survival challenge.

> 💡 **The P4 behavioral review ending:** *"Colonial Program module sequence complete. Cohort CP-Verdant-S1 behavioral profile finalized. You are ready."* Ready for what is not stated. That line is the last thing CASPAR says.

---

### Design Implications

**Packs vs. LTM — scope relationship:**
- Packs are focused, smaller, fewer mods — purpose-built to teach one contingency scenario cleanly
- LTM contains everything from all packs simultaneously — it is the full ship simulation
- Each pack release triggers a LTM update: that module's systems become available in the persistent world
- Players who do the packs first arrive in the LTM with skills that are visibly superior to players who didn't
- Players who jump straight into LTM can survive and engage — but the packs are the real tutorial

**LTM quest writing:**
- Never explain mechanics that players should have learned in a prior pack
- Write flavor text that assumes knowledge — players who have it feel rewarded; players who don't feel motivated to go back
- The LTM is where players realize what the packs were preparing them for

**Colony mechanics as the multiplayer backbone:**
- Players divide labor by skill: resource processing (P1), magical infrastructure (P2), genetics and colony management (P3), combat/defense (P4)
- No single skill set is sufficient alone — the LTM is designed so that experienced players in each discipline need each other
- None of it requires playing the prior packs, but pack players will be demonstrably better at their role

**The behavioral review thread pays off in LTM:** players whose cohort was "flagged for extended review" find out, eventually, what the review was for. The answer is not sinister. It is, in retrospect, inevitable.

---
