# Included from Makefile - offline recipe dump + analyze (see docs/recipe-wiki.md).
# Needs installed JARs under CP-Liminal-Dev (or RECIPE_WIKI_MODS_DIR).
# After mod list / KubeJS changes: make recipe-audit && commit docs/recipe_data.json + docs/recipe-analyze/.

.PHONY: recipe-wiki recipe-analyze recipe-audit recipe-pr recipe-sync

recipe-wiki:
	@echo "→ building recipe wiki from mods JARs + kubejs..."
	python3 scripts/build_recipe_wiki.py
	@echo "→ open docs/recipe_wiki.html locally (gitignored; textures make it large) or: make docs"

recipe-analyze:
	@echo "→ analyzing recipe_data.json + AgriCraft plant datapacks..."
	@python3 -c "import base64,gzip,pathlib; b=base64.b64decode(pathlib.Path('.github/recipe-analyze-parts/analyze.py.gz.b64').read_text()); pathlib.Path('scripts/analyze_recipe_wiki.py').write_bytes(gzip.decompress(b))"
	python3 scripts/analyze_recipe_wiki.py
	@echo "→ see docs/recipe-analyze/summary.md"

recipe-audit: recipe-wiki recipe-analyze
	@echo "→ recipe-audit done; commit docs/recipe_data.json and docs/recipe-analyze/ when intentional"

# One command: new branch, dump, commit, push, PR (see scripts/recipe-dump-pr.sh).
recipe-pr:
	@bash scripts/recipe-dump-pr.sh

# Headless packwiz install into the Prism dev instance, prune stale jars, then recipe-pr (scripts/recipe-sync.sh).
recipe-sync:
	@DEV_MC_DIR="$(DEV_MC_DIR)" BOOTSTRAP_JAR="$(BOOTSTRAP_JAR)" INSTALLER_JAR="$(INSTALLER_JAR)" \
		BOOTSTRAP_URL="$(BOOTSTRAP_URL)" INSTALLER_URL="$(INSTALLER_URL)" PRISM_INSTANCE="$(PRISM_INSTANCE)" \
		bash scripts/recipe-sync.sh
