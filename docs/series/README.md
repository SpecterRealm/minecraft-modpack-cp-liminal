# Colony Protocol — Series Hub

> **Liminal is the source of truth for the series.** Anything that spans more than one pack — story, pack roles, cross-pack design rules, mod ownership — lives here, once.
> The other pack repos (Verdant, Elysian, Influx) document **only what they own** and link back to this folder for everything else.

Colony Protocol is a four-pack training series set aboard the *ACS Longwatch*. **Liminal is the finale.** Each pack is a *Cohort Protocol module*: a different arrival scenario, taught by a different way of getting resources.

All packs target **Minecraft 1.21.1 · NeoForge 21.1.228**, are managed with **packwiz**, and share one tooling template (see [Tooling](#tooling)).

## The packs

| # | Pack | Repo | World | How you get resources | Contingency trained | Status |
|---|------|------|-------|-----------------------|---------------------|--------|
| 1 | **Verdant** | [MichaelHeaton/…-cp-verdant](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant) | Full overworld (Terralith), no ore veins (virtual) | **Sieving** — Ex Deorum; learn to grow what you cannot mine | A world with no convenient ore | Release candidate |
| 2 | **Elysian** | [SpecterRealm/…-cp-elysian](https://github.com/SpecterRealm/minecraft-modpack-cp-elysian) | Void / skyblock (virtual) | **Magic** — spells, essence crops, spirit labor; learn to shape what you cannot craft | Being met — the Veil in use | Scaffold + early quests |
| 3 | **Influx** | [SpecterRealm/…-cp-influx](https://github.com/SpecterRealm/minecraft-modpack-cp-influx) | Aboard the *Longwatch* in flight (real) | **Closed-loop conversion** — use what you have to make everything; space, not materials, is the scarce resource | No landfall — the ship is all there is, in flight | Scaffold + early quests |
| 4 | **Liminal** *(this repo)* | [SpecterRealm/…-cp-liminal](https://github.com/SpecterRealm/minecraft-modpack-cp-liminal) | A lived planet — a pod crash-lands, no way back (real) | **All of the above, reunited** — settle, resist, and cross the threshold | A destination that pushes back | Scaffold; release gated behind Elysian |

**Design method — Liminal first.** The series is designed backwards from its end state; earlier packs are scoped to build the road to Liminal. See [`road-to-liminal.md`](road-to-liminal.md).

**Play order:** Verdant → Elysian → Influx → Liminal is *recommended, never required.* Every pack is completable on its own, and quests teach and reward but never hard-gate.

> **Maintainers only:** V + E + I + L spells **VEIL**. Do not mention it in CurseForge descriptions, READMEs, site copy, or anything player-facing.

## Where things live (DRY map)

| Topic | Home | Other repos do this |
|-------|------|---------------------|
| Mod overlap and reasons | [`mod-audit.md`](mod-audit.md) | Trim exact duplicates; each mod needs a reason. |
| The end state and how each pack builds toward it | [`road-to-liminal.md`](road-to-liminal.md) | Scope changes are decided against it. |
| Story, CASPAR, VCA, fleet, probes, the Entity, signal-color system | [`story.md`](story.md) | Link here. Each pack keeps only its own opening narrative and leak budget. |
| Pack roles, world models, mod ownership, what each pack does *not* do | [`pack-architecture.md`](pack-architecture.md) | Each pack's `docs/pack-identity.md` states its own slice and links here. |
| Mod counts and overlap | [`pack-architecture.md` → Mod overlap](pack-architecture.md#mod-overlap) | Never hard-code a count in prose; link here or run `ls mods/*.pw.toml \| wc -l`. |
| Series sibling table / CurseForge links | This file | Replace copies with a one-line link. |
| Cross-pack bridges (e.g. Ars ↔ Mekanism) | Liminal — `pack-architecture.md` | Not implemented outside Liminal. |
| Pack-specific quest chapters, mod pillars, KubeJS gates, world rules | The owning pack's repo | — |
| Historical design notes (pre-restructure) | [`archive/`](archive/) | — |

**Rule of thumb:** if a fact is true for more than one pack, it goes here. If a pack repo needs it, link — don't copy.

## Tooling

Every repo uses the same Makefile, Prism dev loop, versioning, and CurseForge export rules. The reference implementation is Verdant's [`docs/pack-template.md`](https://github.com/MichaelHeaton/minecraft-modpack-cp-verdant/blob/main/docs/pack-template.md); each repo's own `docs/workflow.md` covers the local specifics. All CP packs serve packwiz on `:8080` — run one at a time.

## Shared services

- **SpecterRealm Core** — shared library mod (`modId: specterrealm`): Patchouli Field Manual shell and cross-pack components. [GitHub](https://github.com/SpecterRealm/specterrealm-core)
- **Field Manual** — Patchouli book rewarded at each pack's Welcome gate; topic IDs live under `specterrealm:field_manual/<pack>/…`.

## CurseForge

| Pack | Project |
|------|---------|
| Verdant | [colony-protocol-verdant](https://www.curseforge.com/minecraft/modpacks/colony-protocol-verdant) |
| Elysian | [colony-protocol-elysian](https://www.curseforge.com/minecraft/modpacks/colony-protocol-elysian) (id `1715473`, preview) |
| Influx | [colony-protocol-influx](https://www.curseforge.com/minecraft/modpacks/colony-protocol-influx) (id `1715476`, preview) |
| Liminal | [colony-protocol-liminal](https://www.curseforge.com/minecraft/modpacks/colony-protocol-liminal) (id `1715485`, preview) |
