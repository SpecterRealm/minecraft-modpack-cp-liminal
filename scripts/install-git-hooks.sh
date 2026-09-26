#!/usr/bin/env bash
# Point this repo at .githooks/ (pre-commit runs check-pack-index --fix when needed).

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

chmod +x .githooks/pre-commit scripts/check-pack-index.sh

git config core.hooksPath .githooks

echo "Installed git hooks → .githooks/"
echo "  pre-commit: packwiz refresh when kubejs/config/mods/etc. are staged"
echo ""
echo "To verify: make check-index"
