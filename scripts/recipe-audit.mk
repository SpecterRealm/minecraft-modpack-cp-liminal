# Included from Makefile - offline recipe dump + analyze (see docs/recipe-wiki.md).
# Needs installed JARs under CP-Liminal-Dev (or RECIPE_WIKI_MODS_DIR).
# After mod list / KubeJS changes: make recipe-audit && commit docs/recipe_data.json + docs/recipe-analyze/.

.PHONY: recipe-analyze recipe-audit

recipe-wiki:
	@echo "→ building recipe wiki from mods JARs + kubejs..."
	python3 scripts/build_recipe_wiki.py
	@echo "→ open docs/recipe_wiki.html locally (gitignored; textures make it large) or: make docs"

recipe-analyze:
	@echo "→ analyzing recipe_data.json + AgriCraft plant datapacks..."
	python3 scripts/analyze_recipe_wiki.py
	@echo "→ see docs/recipe-analyze/summary.md"

recipe-audit: recipe-wiki recipe-analyze
	@echo "→ recipe-audit done; commit docs/recipe_data.json and docs/recipe-analyze/ when intentional"
