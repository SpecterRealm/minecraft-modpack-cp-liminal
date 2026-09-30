# Offline recipe / item dump (Recipe Wiki)

Port of Verdant's maintainer tooling. Builds a **Liminal-local** recipe index from
installed Prism mod JARs plus `kubejs/server_scripts`.

## Outputs

| File | Role |
|------|------|
| `docs/recipe_data.json` | Machine-readable `item_id → recipes` (generated) |
| `docs/recipe_wiki.html` | Browseable HTML (generated; can be large) |

Generated dumps are gitignored by default. Commit only when you intentionally want
a snapshot in-repo.

## How to run (full-pack dump)

1. Instance `CP-Liminal-Dev` has pulled the pack (`make serve-bg` + launch once) so
   `…/minecraft/mods/*.jar` exist.
2. From the Liminal repo root:

```bash
make recipe-wiki
# or
python3 scripts/build_recipe_wiki.py
# or another mods folder:
RECIPE_WIKI_MODS_DIR=/path/to/minecraft/mods python3 scripts/build_recipe_wiki.py
```

3. Open `docs/recipe_wiki.html` in a browser, or `make docs` then visit
   `http://localhost:8000/recipe_wiki.html`.

## In-game companion

`kubejs/server_scripts/recipe_dump.js` logs **recipe counts by type** on world load
(`[CPL]` lines in `latest.log`). It does not write JSON. Comment it out before a
player-facing release if you do not want the log spam.

For a live registry export, use KubeJS in-game (`/kubejs export`) when needed;
that is separate from this offline JAR scan.

## Full-pack dump vs per-mod EMI

| Method | Use when |
|--------|----------|
| **Full-pack dump** (`make recipe-wiki`) | Offline counts, search across mods, KubeJS remove/add visibility, MA↔AgriCraft overlap audits |
| **Per-mod EMI** (in-game, filter `@modid` / namespace) | Quick visual check of one mod's index while playing |

EMI shows the **live** viewer index (after hide tags / EMI++ groups). The offline
dump reads **JAR datapack recipes + KubeJS script text** and may disagree with EMI
on dynamic or plugin-only recipes.

## Do not reuse Verdant dump data

Verdant's `docs/recipe_data.json` / `recipe_wiki.html` are **Verdant-only**. Liminal
has a different mod list (AgriCraft, Mystical Agriculture, Productive stack, PE, …)
and different KubeJS. **Never** copy or cite Verdant dump numbers for Liminal
MA / AgriCraft / farming-lane counts. Always regenerate from `CP-Liminal-Dev`.

## Related

- Workflow: [workflow.md](workflow.md)
- Farming lane context (MA↔AgriCraft): Project store farming notes (outside this repo)
