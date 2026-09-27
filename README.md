# Colony Protocol: Liminal

**Planetfall** kitchen-sink inherit — reunite Verdant, Elysian, and Influx systems on a lived world. Settle, resist, and cross the threshold.

**Loader:** NeoForge **1.21.1** (packwiz)  
**Series order:** Pack **4** of Colony Protocol — Verdant → Elysian → Influx → **Liminal** (recommended last; not required)  
**Status:** Scaffold / coming soon — shared QoL soft-pinned; public release gated after ≥ Elysian is out.

**CurseForge:** _Coming soon — project URL TBD_  
*(Separate CF project from Verdant. Pack display name is **Liminal** — not “Convergence Void.”)*

## What this is

Not another classroom void. Not the ship (that’s Influx). **Planetfall / lived world:** mechanical sieve literacy, magic obtain, and ship-lab genetics/digital reunite under colonial settle pressure and hostile resistance.

Bring whichever path you learned — or arrive cold and learn from a progressive Field Manual (not a day-one dump). Parallel chapter paths OK. Cross-pack bridges default here. Quests still never hard-gate.

## Install tip (players)

1. Install [Prism Launcher](https://prismlauncher.org/) (or the CurseForge app).
2. Add an instance from this pack’s CurseForge page / downloaded zip when published.
3. Allocate ~6–8 GB RAM (more with shaders).
4. Launch with the NeoForge profile the pack ships.

## Dev quick start (Prism)

1. Create Prism instance `CP-Liminal-Dev` → Minecraft **1.21.1** + NeoForge matching `pack.toml`.
2. `make serve` from this repo (or `packwiz serve`).
3. Instance pre-launch:

   ```text
   "$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" --bootstrap-no-update http://localhost:8080/pack.toml
   ```

4. `make setup-dev` once (Prism closed), then launch.

See [docs/workflow.md](docs/workflow.md).

## Series siblings

| Pack | Role | Repo |
|------|------|------|
| [Verdant](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant) | Pack 1 — overworld, no ore veins, sieve loop | Live CF: [colony-protocol-verdant](https://www.curseforge.com/minecraft/modpacks/colony-protocol-verdant) |
| [Elysian](https://github.com/SpecterRealm/minecraft-modpack-cp-elysian) | Pack 2 — void magic | — |
| [Influx](https://github.com/SpecterRealm/minecraft-modpack-cp-influx) | Pack 3 — ship lab / genetics | — |
| **Liminal** (this repo) | Pack 4 — planetfall reunite | — |

Shared library: [SpecterRealm Core](https://github.com/SpecterRealm/specterrealm-core) · CF [SpecterRealm Core](https://www.curseforge.com/minecraft/mc-mods/specterrealm-core)

## What's ready vs stubbed

| Area | Status |
|------|--------|
| packwiz + Makefile + CI | Ready |
| Shared stack (`mods/*.pw.toml`) | Soft-pinned — smoke-test pending |
| `config/ftbquests/` | Early/Mid spine + Late stubs |
| KubeJS | Skeleton + TODOs |
| Pack pillar mods | Soft candidates — inherit from teaching packs when ports land |
| FancyMenu / Field Manual content | Mod pinned; assets TBD |

## Design pointers

Project store: `docs/pack-architecture.md` §Liminal · `pack-progression-arcs.md` §L · `series-todos.md` (port teaching packs; cross-pack bridges default here).

Tooling reference: [Verdant pack-template](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant/blob/main/docs/pack-template.md).
