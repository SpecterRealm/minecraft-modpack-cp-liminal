# Verdant: automated-defense options (discovery)

The gap (`gap-check.md`): Verdant's capstone is a megabuild with automated defenses, and its mod scans found no turret or sentry (only Mekanism's Laser and Robit and Mob Grinding Utils' Iron Spikes). Verdant is calm, tech-feel (Create, Mekanism, AE2, FE power), has no ore worldgen and no Nether progression, and teaches defense as a skill rather than a threat (Liminal is the war zone).

This is a discovery pass for **named gaps only**: search results plus source reads. Nothing is added. Three options were scanned; the rest are listed from search results.

## Options read from source

| Mod | Source | Items | What it is | Fit for Verdant |
|---|---|---|---|---|
| **Mekanism Turrets & Fences** (`x3rdev/MekanismTurrets`, branch 1.21, NeoForge 1.21.1) | read | 5: Electric Fence, and Basic, Advanced, Elite, Ultimate Laser Turret | FE-powered laser turrets with per-turret target settings; needs GeckoLib (already in Verdant) | **Strong.** The four tiers match Mekanism's own Basic, Advanced, Elite, Ultimate ladder, and the recipes use only Mekanism items (steel, tiered control circuits, alloys, energy tablet, electric bow), so there is no Nether item and no new ore. It is a small mod, but it fills the named gap and nothing else in the pack does |
| Create Big Cannons (community NeoForge 1.21.1 port `Reider745/CreateBigCannons-NeoForge-1.21.1`, branch `create-v6-1.21.1`; official build is on CurseForge) | read (names) | 208 | Multiblock cannons and autocannons built with Create; kinetic loaders and aiming; many cannon materials (cast iron, bronze, steel, nethersteel) | **Weak.** Big, a whole second weapons system, and it is aimed and fired rather than auto-targeting; nethersteel needs Nether. It is a Create toy for the megabuild, not a defense line |
| K-Turrets (`AlexiyOrlov/k-turrets`) | **not scanned**: GitHub has no 1.21 branch (master is 1.20.1); the NeoForge 1.21.1 build is on CurseForge and Modrinth only | 6 turrets + 6 combat drones (per the mod page) | Turrets and drones with targeting configurable per mob type; GPL-3.0 | Possible. Not tech-themed in the Mekanism sense; the drones would be new. Needs a source or the jar read in game |

### Mekanism Turrets: numbers read from its config (all editable)

| Tier | Damage | Cooldown (ticks) | Range (blocks) | Energy stored |
|---|---|---|---|---|
| Basic | 1 | 50 | 15 | 10,000 |
| Advanced | 2 | 40 | 20 | 40,000 |
| Elite | 3 | 30 | 25 | 90,000 |
| Ultimate | 4 | 35 | 30 | 160,000 |

Targets are configurable and the default blacklist is the Ender Dragon and Iron Golems. The damage is low (1 to 4 per shot every 1.5 to 2.5 seconds), which is right for the calm teaching pack and weak against Liminal's bosses; every number is a config value, so Liminal can raise it.

## Listed from search results only (not scanned)

| Mod | Why not a fit |
|---|---|
| Create: Sentry Mechanical Arm | Needs TaCZ guns (a gun mod), which is off-theme |
| TACZ Turrets, Mini Auto Turret (SuperbWarfare) | Gun-mod dependent |
| Defense Turrets, Automated Defence, Create Guardian Beam Defense, Create Base Defense Addon | Not read; small mods, versions unconfirmed. Worth a look only if Mekanism Turrets proves too weak |

## Leaning (not a decision)

**Mekanism Turrets & Fences** is the likeliest answer: five items, one named gap, tier-matched to the Mekanism ladder, FE-powered, no new materials. The megabuild goal becomes "a factory that runs unattended and is guarded by turrets the player built and powers". Concerns:
1. Damage is low; fine in Verdant, tune up in Liminal.
2. Fences and turrets need power, which ties defense to the generator lessons (Mekanism Generators, Powah).
3. It is a small mod, so it passes the "adds enough to be worth adding" test only because the gap is real. If you would rather not add a mod for this, the alternative is a KubeJS-built defense from existing items (Mob Grinding Utils spikes plus a kill chamber), which is less fun and less teachable.

Next: decide, then add it with the other decided mods (`adding-decided-mods.md`).
