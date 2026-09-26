#!/usr/bin/env bash
# config-ship-full.sh — pre-export prep for config/ (seed fml.toml, sanity check).
# Repo config/ is the shipped tree; run make config-pull after playtest to refresh from instance.
#
# Usage: make config-ship-full

set -euo pipefail

# shellcheck source=config-instance-env.sh
source "$(dirname "$0")/config-instance-env.sh"

mkdir -p "$SHIP_CONFIG"

if [[ -f "$BOOTSTRAP_FML" ]]; then
  cp "$BOOTSTRAP_FML" "$SHIP_CONFIG/fml.toml"
  echo "→ seeded config/fml.toml from pack-bootstrap/ (SimpleCustomEarlyLoading)"
elif [[ -f "$REPO_ROOT/overrides/config/fml.toml" ]]; then
  cp "$REPO_ROOT/overrides/config/fml.toml" "$SHIP_CONFIG/fml.toml"
  echo "→ seeded config/fml.toml from overrides/config/ (migrate to pack-bootstrap/)"
else
  echo "⚠️  No pack-bootstrap/fml.toml — export may hang on macOS without earlyWindowProvider" >&2
fi

count="$(find "$SHIP_CONFIG" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "✓ config/ has $count files"
if [[ "$count" -lt 80 ]]; then
  echo "⚠️  Thin config tree — run make config-pull after a full dev load, then packwiz refresh" >&2
fi
echo "  Next: packwiz refresh && make export-cf && make validate-export"
