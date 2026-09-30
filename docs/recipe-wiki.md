# Offline recipe / item dump (Recipe Wiki)

Port of Verdant's maintainer tooling. Builds a **Liminal-local** recipe index from
installed Prism mod JARs plus `kubejs/server_scripts`, then writes small analysis
artifacts agents can read from git.

## Make targets

| Target | What it does |
|--------|----------------|
| `make recipe-wiki` | Full dump → `docs/recipe_data.json` + `docs/recipe_wiki.html` |
| `make recipe-analyze` | Summaries from the dump + AgriCraft plant datapack scan → `docs/recipe-analyze/` |
| `make recipe-audit` | `recipe-wiki` then `recipe-analyze` (use after mod list / KubeJS changes) |
| `make docs` | Serve `docs/` at http://localhost:8000/ |

## Outputs

| File | Role | Git |
|------|------|-----|
| `docs/recipe_data.json` | Machine-readable `item_id → recipes` | **Tracked** (commit after `make recipe-audit`) |
| `docs/recipe_wiki.html` | Browseable HTML (textures embedded; can be huge) | **Gitignored** (open locally) |
| `docs/recipe-analyze/summary.md` | Per-mod counts + farming namespace table | **Tracked** |
| `docs/recipe-analyze/by-mod/*.txt` | Item id lists per mod | **Tracked** |
| `docs/recipe-analyze/*-seeds.txt` | Seed-like result ids (MA, AgriCraft, …) | **Tracked** |
| `docs/recipe-analyze/agricraft-plants.txt` | AgriCraft datapack plants (not craft recipes) | **Tracked** after audit |
| `docs/recipe-analyze/agricraft-plants.txt.gz.b64` | Compressed plant-list seed for git | **Tracked** |

`scripts/analyze_recipe_wiki.py` is assembled from
`.github/recipe-analyze-parts/analyze.py.gz.b64` on first `make recipe-analyze`
(same idea as `recipe_wiki_core.py`).

**Regenerate and commit** after mod list or KubeJS recipe changes:

```bash
make recipe-audit
git add docs/recipe_data.json docs/recipe-analyze
git commit -m "chore: refresh recipe dump + analyze"
```

Cloud VMs usually lack Prism JARs. Ship tooling there; run `make recipe-audit` on a
Mac with `CP-Liminal-Dev` mods installed, then commit the generated files. Do **not**
invent or copy Verdant dump data into Liminal.

## How to run (full-pack dump)

1. Instance `CP-Liminal-Dev` has pulled the pack (`make serve-bg` + launch once) so
   `…/minecraft/mods/*.jar` exist.
2. From the Liminal repo root:

```bash
make recipe-audit
# or step by step:
make recipe-wiki
make recipe-analyze
# override mods folder:
RECIPE_WIKI_MODS_DIR=/path/to/minecraft/mods make recipe-audit
```

3. Open `docs/recipe_wiki.html` in a browser (local only), or `make docs` then visit
   `http://localhost:8000/recipe_wiki.html`.
4. Read `docs/recipe-analyze/summary.md` for counts; use `agricraft-plants.txt` for
   AgriCraft plant catalogs (recipe dump alone under-represents AgriCraft plants).

## AgriCraft plants vs recipe results

AgriCraft resource plants live in JAR datapacks (`data/*/agricraft/plants/*.json`,
including nested `datapacks/<pack>/data/...`). They are usually **not** craftable
recipe results, so they do not show up as seeds in `recipe_data.json`.
`make recipe-analyze` scans those plant JSONs separately. Lane decisions should use
**both** the recipe dump and `agricraft-plants.txt`, not recipe-visible seed counts alone.

## In-game companion

`kubejs/server_scripts/recipe_dump.js` logs **recipe counts by type** on world load
(`[CPL]` lines in `latest.log`). It does not write JSON. Comment it out before a
player-facing release if you do not want the log spam.

For a live registry export, use KubeJS in-game (`/kubejs export`) when needed;
that is separate from this offline JAR scan.

## Full-pack dump vs per-mod EMI

| Method | Use when |
|--------|----------|
| **Full-pack audit** (`make recipe-audit`) | Offline counts, search across mods, KubeJS remove/add visibility, MA + AgriCraft plant overlap |
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
