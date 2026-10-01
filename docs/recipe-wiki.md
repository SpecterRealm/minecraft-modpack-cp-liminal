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
| `make recipe-sync` | **Full refresh in one command**: headless packwiz install into the dev instance, prune stale jars, then `recipe-pr` |
| `make recipe-pr` | **One command**: new branch, `recipe-audit`, commit, push, draft PR (`scripts/recipe-dump-pr.sh`) |
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

## One command (recommended)

```bash
cd <pack repo root>
make recipe-pr
```

It stops if the working tree is not dirty-free, branches from `origin/main` as `chore/recipe-dump-<pack>-<timestamp>`, runs `make recipe-audit`, commits `docs/recipe_data.json` and `docs/recipe-analyze/`, pushes, and opens a draft PR with `gh` (without `gh` it prints the compare link). If nothing changed against `main` it exits without a branch. Needs the `CP-<Pack>-Dev` Prism instance pulled once, or `RECIPE_WIKI_MODS_DIR=/path/to/mods make recipe-pr`. Same command in Verdant, Elysian, Influx and Liminal.

## After a mod-list change: `make recipe-sync`

`make recipe-pr` reads whatever jars are in the dev instance and does not run packwiz. When the mod list changed, use:

```bash
make recipe-sync
```

It starts `packwiz serve` (after `packwiz refresh`), runs the packwiz installer headlessly in the dev instance, stops the server, runs `make prune-dev-mods`, then `make recipe-pr`. Needs `packwiz`, `java` (or `JAVA=/path/to/java`), `curl` and `python3`; close the game first. It stops if `packwiz refresh` changed tracked files (commit that first) or if the installer fails. If `recipe-pr` fails before committing, it returns you to your original branch.

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
