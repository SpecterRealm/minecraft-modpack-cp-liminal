#!/usr/bin/env bash
# Verify index.toml / pack.toml match packwiz refresh output.
# Usage:
#   scripts/check-pack-index.sh          — fail if drift (CI, make check-index)
#   scripts/check-pack-index.sh --fix    — refresh + stage index files (pre-commit)

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

FIX=false
if [[ "${1:-}" == "--fix" ]]; then
  FIX=true
fi

export PATH="${HOME}/go/bin:${PATH}"

if ! command -v packwiz >/dev/null 2>&1; then
  echo "check-pack-index: packwiz not on PATH" >&2
  echo "  Install: go install github.com/packwiz/packwiz@latest" >&2
  echo "  Ensure ~/go/bin is on PATH" >&2
  exit 1
fi

packwiz refresh

if git diff --quiet -- index.toml pack.toml; then
  exit 0
fi

echo "check-pack-index: pack index drift detected (index.toml and/or pack.toml)" >&2
git diff --stat -- index.toml pack.toml >&2

if $FIX; then
  git add index.toml pack.toml
  echo "check-pack-index: staged index.toml + pack.toml after packwiz refresh" >&2
  exit 0
fi

echo "check-pack-index: run 'make refresh' and commit the changes" >&2
echo "::error::Pack index is stale — run 'make refresh' (or make check-index) and commit index.toml + pack.toml" >&2
exit 1
