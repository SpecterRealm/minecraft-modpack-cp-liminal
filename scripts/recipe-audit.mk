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
	@if [ ! -f scripts/analyze_recipe_wiki.py ]; then \
		if [ -f .github/recipe-analyze-parts/analyze.py.gz.b64 ]; then \
			python3 -c "import base64,gzip,pathlib; b=base64.b64decode(pathlib.Path('.github/recipe-analyze-parts/analyze.py.gz.b64').read_text()); pathlib.Path('scripts/analyze_recipe_wiki.py').write_bytes(gzip.decompress(b))"; \
		else \
			cat .github/recipe-analyze-parts/analyze.part* > scripts/analyze_recipe_wiki.py; \
		fi; \
	fi
	@if [ ! -f docs/recipe-analyze/agricraft-plants.txt ] && [ -f docs/recipe-analyze/agricraft-plants.txt.gz.b64 ]; then \
		python3 -c "import base64,gzip,pathlib; b=base64.b64decode(pathlib.Path('docs/recipe-analyze/agricraft-plants.txt.gz.b64').read_text()); pathlib.Path('docs/recipe-analyze/agricraft-plants.txt').write_bytes(gzip.decompress(b))"; \
	fi
	python3 scripts/analyze_recipe_wiki.py
	@echo "→ see docs/recipe-analyze/summary.md"

recipe-audit: recipe-wiki recipe-analyze
	@echo "→ recipe-audit done; commit docs/recipe_data.json and docs/recipe-analyze/ when intentional"
