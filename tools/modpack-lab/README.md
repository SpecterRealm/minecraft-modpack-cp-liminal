# modpack-lab

Boots a packwiz modpack on a **headless NeoForge server in Docker** and saves what the server really
loaded: every recipe (after datapacks, KubeJS and load conditions) and the item tags those recipes use.
No Prism, no game client. This is a prototype that lives in Liminal now and is meant to move to its own repo.

JEI and EMI show what the server syncs to the client. A server run reads the same source, so recipes that
mods build at startup (for example Ex Deorum's 4 chunks to ore) are included. The jar scraper cannot see them.

## Use

```
make lab-doctor                 # checks Docker, the pack, the output folder, RAM, the port
make lab-snapshot EULA=1        # boots the server, writes .lab/snapshot.json (accepts the Minecraft EULA)
make lab-dump EULA=1            # same, then writes docs/recipe_data.json (what series-reach.py reads)
```

Options go in `LAB_ARGS`, for example `make lab-snapshot EULA=1 LAB_ARGS="--memory 10G --port 8123"`.
Or call it directly: `tools/modpack-lab/lab.sh snapshot --pack ../other-pack --out ./out --accept-eula`.

## How it works

1. Serves the pack folder (`pack.toml`, `index.toml`, `mods/`) with a small local web server.
2. Starts `itzg/minecraft-server` (NeoForge, version from `pack.toml`), pointing `PACKWIZ_URL` at it. The image
   installs the mods for the server side only.
3. If the server cannot load a mod because it is client-only (the pack does not mark every one), the mod is
   left out of the served copy of the pack and the run repeats. The list is kept in `.lab/exclude-mods.txt`.
4. A KubeJS script (`export/zz_lab_export.js`) prints each recipe as a `[LABDUMP]` line in the KubeJS log.
5. `parse_log.py` collects those lines into `snapshot.json`; the server is stopped.

## Files

- `lab.sh`: doctor and snapshot commands
- `export/zz_lab_export.js`: the in-game exporter (read-only)
- `packtool.py`: makes the pruned pack copy and detects client-only mods from the crash log
- `parse_log.py`: log lines to `snapshot.json` (schema 1)
- `lab.mk`: make targets
- `../../scripts/snapshot-to-dump.py`: Liminal-specific converter to the dump format

## Not verified yet (prototype)

Written without a Docker daemon or the game, so these are unconfirmed until the first real run:
- the KubeJS calls in the exporter (`recipe.json`, `Ingredient.of('#tag').itemIds`) on this KubeJS version
- whether the image's `PACKWIZ_URL` handling accepts this pack, and the server-side filtering of client-only mods
- whether KubeJS recipe removals and additions are already applied when the exporter runs

CurseForge mods that block downloads cannot be fetched by the installer. Put those jars in `.lab/extra-mods/`
and run again.

## Not captured

Worldgen, villager trades, global loot modifiers, and loot tables (the converter keeps those from the jar dump).
