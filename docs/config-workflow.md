# Config workflow — Colony Protocol: Liminal

**`config/`** is the shipped mod config tree (indexed by packwiz). There is **no** repo `overrides/` folder.

## Commands

| Target | Purpose |
|--------|---------|
| `make config-pull` | Additive rsync instance → `config/` |
| `make config-diff` | Diff repo vs live Prism instance |
| `make config-promote PROMOTE="…"` | Copy selected paths instance → repo |
| `make config-ship-full` | Seed `fml.toml` + export prep |

Prism instance: **`CP-Liminal-Dev`** (`PRISM_INSTANCE` override OK).

Requires `rsync` on the local Mac (not available in Cloud VMs).

See Verdant `docs/config-workflow.md` for full policy.
