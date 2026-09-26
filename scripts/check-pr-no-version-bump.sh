#!/usr/bin/env bash
# PRs must not bump pack.toml version — version + tag happen on main after merge.
set -euo pipefail

BASE_REF="${1:-main}"

git fetch origin "$BASE_REF" --depth=1 --quiet

MAIN_VER="$(git show "origin/${BASE_REF}:pack.toml" | grep -E '^version\s*=' | sed 's/.*= "\(.*\)"/\1/')"
HEAD_VER="$(grep -E '^version\s*=' pack.toml | sed 's/.*= "\(.*\)"/\1/')"

if [[ "$MAIN_VER" != "$HEAD_VER" ]]; then
  echo "::error::pack.toml version must not change in a PR (main: $MAIN_VER, PR: $HEAD_VER)." >&2
  echo "Merge feature work first, then on main run: make release-rc (or make release VERSION=...)" >&2
  exit 1
fi

echo "✓ pack.toml version unchanged ($MAIN_VER)"
