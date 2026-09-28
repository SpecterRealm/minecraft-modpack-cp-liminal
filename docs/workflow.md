# Dev workflow — Colony Protocol: Liminal

## Prerequisites

- [Packwiz](https://packwiz.infra.link/) on `PATH` (`go install github.com/packwiz/packwiz@latest`)
- Java 21, Prism Launcher
- Prism instance **`CP-Liminal-Dev`** (or set `PRISM_INSTANCE`)

## Prism smoke (one terminal)

**One manual step Make cannot do:** create an empty Prism instance named `CP-Liminal-Dev` (Minecraft **1.21.1** + NeoForge matching `pack.toml`). Close Prism before `setup-dev`.

```bash
cd /Users/michaelheaton/Projects/specterrealm/esport/minecraft-modpack-cp-liminal
make setup-dev          # once — RAM, window, installer jars, packwiz PreLaunch
make serve-bg           # primary daily target (alias: make up)
# Launch CP-Liminal-Dev in Prism
make serve-stop         # when done (aliases: make down / make stop)
```

`make setup-dev` writes the packwiz PreLaunch command — you do **not** paste it into Prism Settings by hand.

Optional cleanup after pack removals (packwiz does not delete leftovers):

```bash
make prune-instance-orphans   # known-bad paths (e.g. kubejs README orphans)
make prune-dev-mods           # stale mod JARs not in mods/*.pw.toml
```

`make help` lists this smoke path first.

## First-time extras

```bash
make install-hooks   # optional: auto-refresh index on commit
```

Shared stack is soft-pinned under `mods/`. Add pillar mods with `packwiz` when ready; `make refresh` after each batch (also runs inside `serve-bg`).

## Daily loop

```bash
make serve-bg       # backgrounds packwiz; log → .serve.log
# Launch CP-Liminal-Dev in Prism
make logs           # optional second terminal
make serve-stop
```

Or on macOS with Prism at the default path: `make dev` (configure + serve-bg + launch).

Foreground serve (blocks the terminal): `make serve`.

## After edits

- New tracked files → `make refresh` (or just `make serve-bg`)
- In-game quest edits → pull into `config/ftbquests/` (quest worker / `quest-pull` when wired)
- Config drift → `make config-pull` / `make config-diff`

## Export

```bash
make export-cf
make validate-export
```

See [curseforge-export.md](curseforge-export.md). Modrinth export may fail if a mod requires manual CF download.

## Design

Project store: docs/pack-architecture.md §Liminal · pack-progression-arcs.md §L · series-todos.md (port teaching packs; cross-pack bridges default here).
