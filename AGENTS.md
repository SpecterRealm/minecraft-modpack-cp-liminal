# Colony Protocol: Liminal — Agent Instructions

Planetfall kitchen-sink inherit — reunite V/E/I systems + combat / colonial settle on a lived world.

**Loader:** NeoForge 1.21.1 (match Verdant). **Not** a copy of Verdant quests or world model.

## Canonical paths

| Purpose | Path |
|---------|------|
| Pack repo | repo root |
| Prism | `~/Library/Application Support/PrismLauncher/instances/CP-Liminal-Dev/minecraft/` |
| Quests | `config/ftbquests/` (**quest worker owns SNBT** — scaffolding PRs leave empty) |
| KubeJS | `kubejs/` |
| Mods | `mods/*.pw.toml` |

## Dev loop

1. Edit → `make refresh` → `make serve-bg` → Launch `CP-Liminal-Dev` in Prism (PreLaunch pulls `http://localhost:8080/pack.toml`)
2. Stop with `make serve-stop` (aliases: `down`, `stop`)
3. `make help` — smoke path listed first; also exports / config pull
4. Do **not** invent final pillar modlists — soft pins + TODOs only
5. Quests teach; rewards = QoL + Field Manual pages — **never** progression gates

First-time (Prism closed): `make setup-dev` (jars + PreLaunch + RAM/window). Optional: `make prune-instance-orphans` after pack removals.

## Design pointers

Project store: docs/pack-architecture.md §Liminal · pack-progression-arcs.md §L · series-todos.md (port teaching packs; cross-pack bridges default here).

## GitHub

- Repo: `specterrealm/minecraft-modpack-cp-liminal`
- Do not close code issues until PR merged to `main`
- Do not bump `pack.toml` version in feature PRs (CI blocks)

## What not to copy from Verdant

- Verdant quest chapters / lore SNBT
- Verdant-only pillars (Ex Deorum, Create, Mekanism as V teaching path)
- `pack-content/cpverdant` / `cpverdant:` namespaces — use SpecterRealm Core
