name: assemble-recipe-wiki
on:
  push:
    branches: [cursor/fix-recipe-wiki-script-5d2f]
    paths:
      - .github/workflows/assemble-recipe-wiki.yml
      - .github/recipe-wiki-parts/**
  workflow_dispatch:
permissions:
  contents: write
jobs:
  assemble:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Assemble recipe_wiki_core.py
        run: |
          set -euo pipefail
          cat .github/recipe-wiki-parts/core.part0 .github/recipe-wiki-parts/core.part1 > scripts/recipe_wiki_core.py
          python3 -m py_compile scripts/build_recipe_wiki.py scripts/recipe_wiki_core.py scripts/recipe_wiki_render.py
          test -f scripts/recipe_wiki_template.html
          rm -rf .github/recipe-wiki-parts .github/workflows/assemble-recipe-wiki.yml
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add -A
          if git diff --cached --quiet; then echo noop; exit 0; fi
          git commit -m "chore: assemble recipe_wiki_core.py for plaintext recipe wiki"
          git push
