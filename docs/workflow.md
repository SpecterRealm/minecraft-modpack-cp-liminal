# Dev workflow — Colony Protocol: Liminal

## Prerequisites

- [Packwiz](https://packwiz.infra.link/) on `PATH` (`go install github.com/packwiz/packwiz@latest`)
- Java 21, Prism Launcher
- Prism instance **`CP-Liminal-Dev`** (or set `PRISM_INSTANCE`)

## First-time setup

1. Clone this repo.
2. Create a **NeoForge 1.21.1** instance in Prism named `CP-Liminal-Dev` (empty mods folder OK).
3. Set instance pre-launch (after `make serve` is running):

   ```text
   "$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" --bootstrap-no-update http://localhost:8080/pack.toml
   ```

4. From repo root:

   ```bash
   make install-hooks   # optional: auto-refresh index on commit
   make setup-dev       # Prism must be closed
   ```

5. Shared stack is already soft-pinned under `mods/`. Add pillar mods with `packwiz` when ready; `make refresh` after each batch.

## Daily loop

```bash
make serve          # terminal 1 — http://localhost:8080
# Launch CP-Liminal-Dev in Prism (pre-launch pulls pack)
make logs           # terminal 2 — optional
```

Or: `make dev` on macOS with Prism at the default path.

## After edits

- New tracked files → `make refresh`
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
