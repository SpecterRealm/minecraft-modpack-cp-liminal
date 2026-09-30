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

## 3. Decisions so far (maintainer)

| Pack | Direction chosen | Still to do |
|---|---|---|
| Influx | **Genetics: Resequenced** ("how to make yourself better": scrape mobs for genes, infuse powers) plus **Mutant Monsters** (mutant mobs as the combat content). Genes are the cure and the power-up; the mutants are what the experiments produce. | Scan both (Mutant Monsters source: Fuzss/mutant-monsters, branch 1.21.1; Genetics: Resequenced by aaronhowser1, repo not yet located). Check how genes connect to Hostile Neural Networks, Productive Bees and Replication. |
| Verdant | **Megabuild with automated defenses**, played like Factorio on peaceful mode: time and space to learn how things work, light pressure. Defenses are a skill being taught, not a survival test. | Define the target as a production and uptime goal, with at most a gentle defense check. No new mod yet. |
| Elysian | Gateways to Eternity (already in pack). | The arena should cost things the player automated. |

### Armor is also for looks

Part of why many armor mods were collected is how the player looks in them, which is why the RPG class mods (rogue, wizard, paladin, archer) appeal. So the "every item has a job" rule has two kinds of job: a **gameplay niche** and a **look**. Options to keep both without 27 competing tiers:

1. **Cosmetic layer**: a cosmetic-armor-slot mod (for example Cosmetic Armor Reworked, which has NeoForge 1.21.1 builds) lets any set be worn for looks while the tiered set provides stats. Then look variety costs no balance.
2. **Class sets as the niche**: the RPG Series (Wizards, Archers, Rogues & Warriors, Paladins & Priests; all NeoForge 1.21.1, all require Spell Engine) gives each class armor a role (spell power, ranged, evasion, frontline, healing). The job is the class.
3. Both: one stat family per niche per tier, class sets as the niche sets, cosmetic layer for everything else.

Not yet scanned. These are discovery leads, not additions.

### Pack roles before Liminal (maintainer, latest)

- **Verdant is the calm teacher.** Think Factorio on peaceful mode: the player learns how to do things with time and space to do them. The aim is that they understand how things work before Liminal. "Teach how to fish before you are shipwrecked."
- **Liminal is the war zone.** It brings the mobs from the other packs plus a few new ones made for Liminal. Verdant therefore needs to teach the *skills* Liminal tests (automate, store, defend), without the threat.
- Consequence for the capstone: measure Verdant by whether the factory runs unattended, not by whether the player survives a wave. Automated defenses are taught as a build (a turret line, a mob farm) and get their real test in Liminal.

### Armor decisions

- The RPG Series (Wizards, Archers, Rogues & Warriors, Paladins & Priests; all need Spell Engine) is the class-set mod family meant.
- Use **both** class sets and a cosmetic layer, but they do not have to be in every pack. Rollout chosen:

| Pack | Class sets (RPG Series) | Cosmetic layer |
|---|---|---|
| Verdant | **Archers** (ranged; fits turret-and-defense teaching) | **yes** (appearance from the first pack) |
| Elysian | **start here**: a first few classes | carries over |
| Influx | a few more | carries over |
| Liminal | all of them | carries over |

Class split (maintainer): **Elysian gets the combat classes** (Wizards, Rogues & Warriors); **Influx gets the utility classes** (Paladins & Priests: frontline, healing, shielding). **Verdant gets Archers** (maintainer). Liminal gets all.

### Verdant's capstone is the finished quest book

"Runs unattended" is measured by the quest book: every system a player will need or want later has a quest, so completing the book means they understand how each thing works. The stage matrix tells us which systems must be covered.

**Timing: the quest book waits until the mods are locked.** Building quests now would repeat the rework the pack has today, because every mod decision changes what needs a quest. Until go/no-go is settled per mod, do not audit or build Verdant quests; `docs/machines.md` and `/tier-quest` stay as they are.

## 4. Scan results for the chosen mods (first read, source at the 1.21 branches)

Scanned with `series-mod-scan.py` (entries in `scan/`, repos in `sources.json`, all flagged `candidate`). Recipes read from each repo's generated data.

| Mod | Items | What it adds | Built-in support | Fit issue found |
|---|---|---|---|---|
| Genetics: Resequenced | 35 | Scrape mobs, extract DNA, plasmids and syringes; incubator and cell analyzer machines; coal generator | Modonomicon and Patchouli guide data | **Its own FE machines and Coal Generator**: one more power consumer and a small generator inside the mod. Needs a check against Influx's power (is it fed by existing FE or isolated?). |
| Mutant Monsters | 64 | Mutant creeper, enderman, skeleton, zombie, snow golem; Hulk Hammer; Mutant Skeleton armor | none | Enderman and End-flavored drops (Endersoul) sit outside the no-End rule. Skeleton armor is a mob-drop armor set (needs a gear role). |
| Spell Engine | 6 | Library: spells, spell scrolls, Spell Binding Table | Curios, EMI, Cloth Config, Player Animator | Required by all four class mods. |
| Wizards | 53 | Arcane/Fire/Frost robes, staffs, wands, Wizard Merchant | Lithostitched | Recipes need **netherite, ender pearls, blaze powder, prismarine, lapis**. |
| Archers | 48 | Bows, crossbows, spears, quivers, ranger sets, Archery Artisan | Curios | Recipes mostly iron, leather, string; upper tier needs netherite. |
| Rogues & Warriors | 61 | Daggers, sickles, glaives, double axes, assassin and berserker sets | Lithostitched | Iron and gold base; upper tier needs netherite. |
| Paladins & Priests | 74 | Claymores, maces, great hammers, shields, holy wands and staffs, crusader set | Lithostitched | Iron, gold, diamond; **ghast tears** and netherite for upper tiers. |

### What this means

- **Base tiers fit the pack**: iron, gold, leather, string and wool are all reachable by sieving and farming. Verdant's Archers and the lower classes need no change.
- **Top tiers collide with "no Nether, no End"** in packs 1 to 3. Every class mod has a netherite tier, and Wizards and Paladins also use ender pearls, blaze powder and ghast tears. Options to decide later: hide the netherite tier, or recipe-swap it with KubeJS onto a pack-native material (for example a Silent Gear or Mekanism alloy). Not decided here.
- **Cosmetic layer**: the armor sets work as looks for any tier once a cosmetic mod is in.
- **Spell Engine** is the shared dependency, so the class mods cost one library plus content.

The seven mods now have profiles (`profiles.json`, status candidate) and review files; all items are marked review:checked from a first read.

Still to do: scan the cosmetic armor mod (Cosmetic Armor Reworked, NeoForge 1.21.1 build; the public repo found only has old branches, so it needs a source), review each mod against the review-process steps, and fill `profiles.json` (feel, stage, fit) for the new mods.

### Netherite tiers: the player builds them (maintainer decision)

Direction: keep the netherite tier in the class mods and give the player a way to build it, as skyblock maps commonly do. Read from Ex Deorum's generated sieve recipes (repo `thedarkcolour/ExDeorum`, branch 1.21.1):

| Input the class mods need | Ex Deorum route | Note |
|---|---|---|
| Ancient debris (for netherite scrap, then ingot) | Sieve crushed blackstone with a **netherite mesh**, 10% per pass (binomial p=0.1) | Mesh tier gates it; other meshes also list ancient debris in some recipes |
| Ghast tear | Sieve soul sand | |
| Blaze powder | Sieve crushed netherrack, or dust | |
| Ender pearl | Sieve crushed end stone | |
| Prismarine shard | Sieve sand | |
| Netherite upgrade smithing template | not checked | The smithing template recipe needs checking |

### Resource supply is the real question, per pack (maintainer, latest)

Verdant is skyblock-style by design: Ex Deorum already supplies stone and the nether-style materials, so a netherite tier is not a special problem there. What is needed is a **required-resource list**: for each gear tier, the inputs, and the pack route that delivers each. The weak spots are the other two packs, and the maintainer expects to lean on Ex Deorum more than first intended to close them. That is a gap we are looking for, not a settled change.

Note the conflict to settle: `pack-architecture.md` currently says Elysian has "No sieve loop", and Ex Deorum is in Verdant and Liminal only (not Elysian or Influx).

| Pack | Netherite-tier inputs today (read from `yields/`) | Gaps to check |
|---|---|---|
| Verdant | Ex Deorum sieves (table above) | Confirm the base blocks (blackstone, soul sand, end stone) and the smithing template |
| Elysian | Mystical Agriculture netherite crop (but its seed needs a netherite ingot first) and mob crops for blaze, ghast, enderman (soul jar needed) | First-unit bootstrap for ingots and souls; see the Elysian section |
| Influx | Productive Bees has a netherite comb (centrifuge); ProjectE and Replication can make items from EMC/matter | Confirm ender pearl, ghast tear, blaze powder via EMC or replication; else rely on Ex Deorum |

Next step: build the **required-resource list** per pack (tier, inputs, route, gap), starting from the class mods and Silent Gear, then decide per gap whether Elysian and Influx add Ex Deorum or use their own route.

### Influx: mobs as the resource source (maintainer idea, latest)

Direction to test: Influx gets its nether-style inputs by **training Hostile Neural Networks on mobs**, and its genetics theme moves from "27,000 plants" toward **engineering animals and mobs to get what you need**. That would make Genetics: Resequenced the centre of the pack and could reduce the plant-genetics mods.

What the source shows (Hostile Neural Networks, branch 1.21):
- Data models exist for blaze, ghast, enderman, wither skeleton, guardian, elder guardian, creeper, skeleton, zombified piglin, magma cube, shulker, warden, wither and more. A Loot Fabricator turns a trained model into that mob's drops (so blaze rods, ghast tears, ender pearls come from models).
- Model tiers carry a required-data value per tier (`RequiredData`). Models are trained by feeding data from that mob, in the Simulation Chamber, so the first blaze or ghast has to come from somewhere. I read the tier and data structure but not the exact kill path; confirm in game.
- Generalized Overworld, Nether and Ender predictions exist too.

**The chicken-and-egg**: the player must be carrying a training model and kill a mob of that type before the model records data, so the first blaze or ghast has to come from somewhere (maintainer confirmed: the model needs the kill).

**Maintainer design: make the genetics path the answer.** Instead of a handed-out pocket dimension, the arc is one continuous lesson:

1. **Peaceful mobs first.** Genetics: manipulate cows, pigs, chickens, rabbits (gene, cell, incubator).
2. **Make eggs.** Turn a mob's cell into its spawn egg, so any mob can be spawned, including a blaze, without finding one.
3. **Make spawners** from eggs.
4. **Feed Hostile Neural Networks** from the spawners: train the models, then the Loot Fabricator makes the drops (blaze rods, ghast tears, ender pearls) at scale.

What is already there and what is missing (Genetics: Resequenced source, 1.21-Neoforge):
- **There**: per-mob DNA and cells (`EntityDnaItem` gives a cell for any entity type), cell duplication (`dupe_cell`), GMO incubator recipes (for example blaze to bioluminescence, enderman to teleport, at set chances), and virus, mutation and cell-growth recipes.
- **Not there**: no recipe makes a spawn egg or a spawner from a cell. The mod only uses spawn eggs as information in its guide. So the egg and spawner steps need to be built: a KubeJS recipe (mob cell plus a cost to egg; eggs plus a cost to spawner) is the likely way, and it leaves the genetics mod untouched. Keeping the cost high enough that eggs are a stage-4 milestone, not a day-one shortcut, is a tuning decision.
- **Replacement**: a lost component is never a block, because eggs and cells can be remade from the genetics line.

**AE2's spatial storage** already gives Influx a pocket-dimension effect (maintainer point; AE2 is in Influx). So Compact Machines may be unneeded for the pocket idea. Two things to check: whether a spawner or spawn-egg room can be stored and moved in AE2 spatial storage, and whether Compact Machines adds anything AE2 spatial does not (it stays a candidate only for "build inward" rooms).

Other supply notes:
- **Mystical Agriculture**: has blaze, ghast and enderman mob crops (see the Elysian section below). Already in Elysian; adding it to Influx is an option the maintainer raised.
- **Ex Deorum** (or Ex Nihilo) stays the fallback for Influx if the mob route leaves gaps.

### Elysian: the first-seed problem (Mystical Agriculture, source read)

Correction first: Mystical Agriculture **does** have mob crops. The resource-only list read earlier (`yields/mystical-agriculture.json`) left them out because they are a separate crop type. From `ModCrops.java` (branch 1.21):

| Tier | Mob crops |
|---|---|
| 2 | pig, chicken, cow, sheep, squid, fish, slime, turtle, armadillo |
| 3 | zombie, skeleton, creeper, spider, phantom, rabbit (also blizz, blitz, basalz) |
| 4 | breeze, **blaze, ghast, enderman** |
| 5 | wither skeleton |

How seeds work (recipes read from source):
- Each crop's seed needs its **base ingredient** plus essence. Resource crops need the real material: the **iron seed needs an iron ingot**, the **netherite seed needs a netherite ingot**, coal needs coal. So a crop cannot make the first unit of its own material (the literal chicken and egg).
- Tier 1 crops are cheap: stone, dirt, wood (any log), ice, deepslate. Tier 2 nether, nature, dye, coral and honey use **agglomeratio** items crafted from ordinary materials. The nether agglomeratio recipe is netherrack, soul sand, nether bricks and nether wart, so even the nether crop needs those Nether items first.
- **Mob crops need a filled Soul Jar** (recipes: soul jar, soul extractor, soul siphoner enchant, passive and hostile soulium daggers). So a mob's soul must be captured by killing that mob once, which brings back the blaze, ghast and enderman problem in Elysian.

What Elysian still needs to answer (its scaffold docs list the spine as Ars void bootstrap, MA grow and Occultism labor; the detail is not written):
1. **First iron** and other starter ingots for resource seeds: which mod hands the player the first unit in a void start (Occultism, Theurgy, Ars, a quest reward, KubeJS)?
2. **First blaze, ghast and enderman soul** for their crops: a mob spawner in the world, a KubeJS recipe, or a quest reward, like Influx's egg route.
3. **Netherrack, soul sand, nether bricks and nether wart** for the nether agglomeratio.

Maintainer's likely answer: **add Ex Deorum to Elysian**, and remove some of its recipes so it only bootstraps the first items and pushes the player toward the magical crops. That overturns the current "no sieve loop" line in `pack-architecture.md`, so it needs a deliberate edit there if chosen. AgriCraft is an Influx mod, not Elysian's; it is not part of this question.

### Principle (maintainer): key off the foundation mods

Do not lock a pack to one mod too early. Decide where each pack is going, pick the mods that are its **foundation**, then add mods only to fill the holes and gaps around them. For Influx, candidate foundation: Hostile Neural Networks, Genetics: Resequenced, Replication, ProjectE, with Compact Machines for space. Mods that only serve the old plant-genetics direction (AgriCraft, Productive Trees, Productive Farming) are then reviewed again, not cut in advance.

### Liminal's new mobs: candidates found

Liminal needs mobs made for it (still undecided). Two candidates supplied by the maintainer, both scanned:
- **Mowzie's Mobs** (`BobMowzie/MowziesMobs-Public`, 153 items): bosses (Ferrous Wroughtnaut, Frostmaw, Umvuthi, Naga, Sculptor), GeckoLib required. Its gear has real jobs (each mask gives an ability; Earthrend Gauntlet and the Axe of a Thousand Metals have special attacks), which fits the every-item-has-a-job rule.
- **Deeper and Darker** (`KyaniteMods/DeeperAndDarker`, 278 items): a Deep Dark dimension with blocks, woods and gear. It adds a dimension, so it conflicts with "no extra dimensions" in packs 1 to 3; Liminal only.

Neither is decided. Mutant Monsters stays Influx's outbreak content.

## Open questions

1. Influx: Genetics: Resequenced plus Mutant Monsters chosen. Confirm after scanning that they fit the pack's power and breeding systems.
2. Archers in Verdant brings Spell Engine into the first pack. Confirm that is wanted, since Elysian's Wizards need it anyway.
3. Elysian and Influx: add Ex Deorum (or part of it), or close the netherite-tier input gaps with their own mods? Needs the required-resource list first.
4. Elysian: first iron, first mob souls and Nether items for the agglomeratio: Ex Deorum with trimmed recipes, or other routes?
5. Influx: build the egg and spawner recipes (cost, stage) on top of Genetics: Resequenced; confirm AE2 spatial storage can hold a spawner room and whether Compact Machines adds anything.
6. Liminal's new mobs are not decided yet (raised in the last chat). Verdant, Elysian and Influx teach the counters once they are.
7. Gear: do the roles above cover what you want, or are there jobs to add?
