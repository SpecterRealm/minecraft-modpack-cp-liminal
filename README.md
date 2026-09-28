# Colony Protocol: Liminal

**Planetfall** kitchen-sink inherit — reunite Verdant, Elysian, and Influx systems on a lived world. Settle, resist, and cross the threshold.

**Loader:** NeoForge **1.21.1** (packwiz)  
**Series order:** Pack **4** of Colony Protocol — Verdant → Elysian → Influx → **Liminal** (recommended last; not required)  
**Status:** Scaffold / coming soon — **V ∪ E ∪ I** mod union pinned (**133**); public release gated after ≥ Elysian is out.

**CurseForge:** [colony-protocol-liminal](https://www.curseforge.com/minecraft/modpacks/colony-protocol-liminal) (id `1715485`) — public preview / Coming Soon (no zip yet)  
*(Separate CF project from Verdant. Pack display name is **Liminal** — not “Convergence Void.”)*

## What this is

Not another classroom void. Not the ship (that’s Influx). **Planetfall / lived world:** mechanical sieve literacy, magic obtain, and ship-lab genetics/digital reunite under colonial settle pressure and hostile resistance.

Bring whichever path you learned — or arrive cold and learn from a progressive Field Manual (not a day-one dump). Parallel chapter paths OK. Cross-pack bridges default here. Quests still never hard-gate.

## Install tip (players)

1. Install [Prism Launcher](https://prismlauncher.org/) (or the CurseForge app).
2. Add an instance from this pack’s CurseForge page / downloaded zip when published.
3. Allocate ~6–8 GB RAM (more with shaders).
4. Launch with the NeoForge profile the pack ships.

## Prism smoke (one terminal)

**One manual step Make cannot do:** create an empty Prism instance named **`CP-Liminal-Dev`** with Minecraft **1.21.1** + NeoForge matching `pack.toml`. Close Prism before step 2.

```bash
cd /Users/michaelheaton/Projects/specterrealm/esport/minecraft-modpack-cp-liminal
make setup-dev          # RAM, window, installer jars, packwiz PreLaunch
make serve-bg           # primary — backgrounds packwiz on :8080
# Launch CP-Liminal-Dev in Prism
make serve-stop         # when done (aliases: make down / make stop)
```

**Port:** all CP packs use `:8080`. Switch packs with `make serve-stop` here, then `make serve-bg` in the other repo (one serve at a time).

Optional after pack removals (packwiz does not delete leftovers): `make prune-instance-orphans` and/or `make prune-dev-mods`.

See [docs/workflow.md](docs/workflow.md).

## Series siblings

| Pack | Role | CF |
|------|------|-----|
| [Verdant](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant) | Pack 1 — overworld, no ore veins, sieve loop | [colony-protocol-verdant](https://www.curseforge.com/minecraft/modpacks/colony-protocol-verdant) |
| [Elysian](https://github.com/SpecterRealm/minecraft-modpack-cp-elysian) | Pack 2 — void magic | [colony-protocol-elysian](https://www.curseforge.com/minecraft/modpacks/colony-protocol-elysian) (preview) |
| [Influx](https://github.com/SpecterRealm/minecraft-modpack-cp-influx) | Pack 3 — ship lab / genetics | [colony-protocol-influx](https://www.curseforge.com/minecraft/modpacks/colony-protocol-influx) (preview) |
| **Liminal** (this repo) | Pack 4 — planetfall reunite | [colony-protocol-liminal](https://www.curseforge.com/minecraft/modpacks/colony-protocol-liminal) (preview) |

Shared library: [SpecterRealm Core](https://github.com/SpecterRealm/specterrealm-core) · CF [SpecterRealm Core](https://www.curseforge.com/minecraft/mc-mods/specterrealm-core)

## What's ready vs stubbed

| Area | Status |
|------|--------|
| packwiz + Makefile + CI | Ready |
| Shared + reunite stack (`mods/*.pw.toml`) | **133** = V∪E∪I — Prism smoke pending |
| `config/ftbquests/` | Early/Mid spine + Late stubs |
| KubeJS | Skeleton + TODOs |
| FancyMenu / Field Manual content | Backgrounds shipped (#12); full Bridge chrome TBD |

## Design pointers

Project store: `docs/pack-architecture.md` §Liminal · `pack-progression-arcs.md` §L · `series-todos.md` (port teaching packs; cross-pack bridges default here).

Tooling reference: [Verdant pack-template](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant/blob/main/docs/pack-template.md).
