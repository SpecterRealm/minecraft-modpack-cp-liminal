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

## Early window (macOS)

FancyMenu registers `fmlearlywindow`. On **macOS aarch64** that provider hangs before the title screen (log stops at `Loading ImmediateWindowProvider fmlearlywindow`).

Ship **`config/fml.toml`** (full NeoForge-valid file, pinned from Verdant) with:

```toml
earlyWindowProvider = "SimpleCustomEarlyLoading"
```

Canonical template: `pack-bootstrap/fml.toml` (copied by `make config-ship-full`). Do **not** remove FancyMenu for this — only pin the early-window provider away from `fmlearlywindow`. Simple Custom Early Loading stays in `mods/` (one pin only).

See Verdant `docs/config-workflow.md` / `docs/modpack-export-practices.md` for full policy.
