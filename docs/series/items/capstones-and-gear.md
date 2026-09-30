# Capstones and gear: what each pack is for, and what each item is for

Two design gaps the catalog surfaced. Both come from maintainer direction, recorded here with the data behind them. Nothing below is a decision to add a mod.

## 1. Every pack needs a "why are you doing all this"

Stage 6 of the progression (see `mod-profiles.md`, stage matrix) is the capstone: content that uses everything the player built. Status:

| Pack | Theme | Stage 6 today | Gap |
|---|---|---|---|
| Elysian | Shape what you cannot craft | Gateways to Eternity (open a portal, mobs come through, fight), Apotheosis gear, Iron's Spells combat, Ars schools | Has one. Needs the arena to cost things the player automated. |
| Verdant | Automate all the things | Building gadgets and wands, the MekaSuit, Silent Gear | **No capstone.** Nothing turns a big factory into a goal. |
| Influx | Look what the mad scientist made today | Silent Gear only | **No capstone.** The genetics, EMC and replication all feed nothing. |

### Influx: "what did we make, and how do we stop it"

The feel asked for is Regrowth-style restoration or a Resident Evil outbreak: the player's experiments (breeding, genetics, replication, EMC) cause something, and the capstone is containing or curing it. Leads found (web search; none scanned yet because source repos were not located):

| Lead | What it is | Why it might fit |
|---|---|---|
| Infected World | Spreading apocalypse: infected biomes, mutated wildlife, twisted villagers (NeoForge 1.21.1) | The outbreak itself |
| Mutationcraft | Parasite mutants; mobs and players killed by them turn; Mutagen Sickness (NeoForge 1.21.1) | Fits "our experiments got out" |
| Genetics: Resequenced | Extract mobs' genes to gain their powers | Fits the mad-scientist and genetics theme; could be the cause or the cure |
| Fungal Infection: Spore | Aggressive fungal spread (NeoForge 1.21.1, alpha) | Spreading-corruption mechanic |
| Contagion | Zombie infection (NeoForge 1.21.1) | Simpler outbreak |
| Mutant Monsters | Mutant boss-style mobs (NeoForge 1.21.1) | Combat content for the outbreak |

The existing Influx mods give the cure a path: Hostile Neural Networks (study mobs), Productive Bees and AgriCraft (genetics), Replication and ProjectE (make the cure). The open design question is whether the outbreak mod is the *threat* (something spreads until you stop it) or the *content* (mutant bosses), and which single mod does it.

### Verdant: "automate all the things"

The capstone should be a goal that only a big automated factory can reach. Leads:

| Lead | Why it might fit | Caveat |
|---|---|---|
| Ad Astra | Space program: rockets need processed fuel, oxygen and machines before the first launch; five planets with their own resources | Adds an oxygen and fuel chain, which is one more system to fit next to Create and Mekanism |
| A production target built on what exists | For example a quest-gated megabuild: an AE2 network, a Create train line, a reactor | No new mod; the goal is a number, not content |
| Gateways to Eternity with automated defenses | Waves that need turret and farm automation | Overlaps Elysian's capstone; tech-side defenses are needed |

MineColonies stays Liminal's (the colony capstone).

## 2. Every item needs a job

Direction: gear scales with progress, and two tools that do the same basic job should each have a reason to exist (Tinkers' Construct: one sword for mob heads, another for bypassing armor). "Why gold armor versus iron?" needs an answer.

### Silent Gear already is that system

From source (branch 1.21.1): 92 materials and 77 traits. Materials carry trait mixes, so niches come from parts, not from a count of swords. Examples of what the data shows:

| Material | Traits | The job |
|---|---|---|
| Iron | flexible, malleable | Durable all-rounder |
| Gold | soft, brilliant, malleable, bending | Enchantable, fragile |
| Diamond | lustrous, brittle, bastion | High stats, low durability |
| Crimson iron | fiery, heat-resistant, hard | Fire and Nether work |
| Flint | jagged, brittle | Cheap early damage |
| Stone | crushing, ancient | Early mining |

Other traits cover silk touch (silky), fortune (fortunate), looting-style luck (lucky), multi-break, magnetic, venom, holy, cursed, void ward, flame ward, and movement (moonwalker, snow walker). Silent Gear Metalworks (decided: all packs) adds the Tinkers-style casting feel.

### The test for any other gear mod

A gear set earns its place only if it does something a Silent Gear build cannot:

| Family | Job no Silent Gear build does | Verdict input |
|---|---|---|
| MekaSuit (core Mekanism) | Powered modular suit: jetpack, scuba, hazmat modules | Keep the niche; it is in core Mekanism, not the Tools jar |
| Mekanism Tools (separate jar, about 36 gear items in Verdant) | Plain tiered sets and paxels | No niche next to Silent Gear and vanilla tiers; cut candidate |
| Advanced AE quantum armor | Upgrade-card suit tied to the AE2 network | Niche only if AE2 stays the pillar |
| Iron's Spells armor, Ars Elemental and Elemancy | Spell power and elemental schools | Niche for magic packs; 165 armor items in Elysian (Elemancy 70, Iron's 55, Elemental 40) means one family per tier |
| AE2 certus and fluix tools | Early AE2-themed tools | No niche; hide |
| Mystical Agriculture gear | Resource-tier sets | Overlaps Silent Gear tiers; decide by tier |
| Draconic, Twilight Forest, ProjectE sets | Endgame tiers | Fine if each owns a late tier |

### What to build next for gear

1. A **gear-role tag** on weapons, armor and tools (for example: all-rounder, armor-piercing, mob-drops, mining-AoE, fire, hazard, spell-power, mobility), set per family and per Silent Gear trait group.
2. A **tier ladder per pack**: which family owns each stage, with one family per niche per tier.
3. Hide the rest, at the item level if the mod stays for other reasons.

## Open questions

1. Influx: is the outbreak the threat (spreads until stopped) or the content (mutant bosses)? Which one mod carries it?
2. Verdant: a space program (Ad Astra), a production-target megabuild, or something else?
3. Gear: do the roles above cover what you want, or are there jobs to add?
