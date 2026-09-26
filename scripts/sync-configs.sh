#!/usr/bin/env bash
# sync-configs.sh — rsync Prism instance config/ into repo config/ (shipped tree).
# Additive merge (no --delete). Seeds pack-bootstrap/fml.toml after sync.
# See docs/config-workflow.md

set -euo pipefail

# shellcheck source=config-instance-env.sh
source "$(dirname "$0")/config-instance-env.sh"
# shellcheck source=config-ship-excludes.sh
source "$REPO_ROOT/scripts/config-ship-excludes.sh"

config_instance_require

RSYNC_EXCLUDES=(
  "${CONFIG_RSYNC_EXCLUDES[@]}"
  --exclude='fml.toml'
)

echo "Config sync — $(date '+%Y-%m-%d %H:%M:%S')"
echo "  From: $INSTANCE_CONFIG"
echo "  To:   $SHIP_CONFIG"
echo ""

mkdir -p "$SHIP_CONFIG"

rsync -a \
  "${RSYNC_EXCLUDES[@]}" \
  "$INSTANCE_CONFIG/" "$SHIP_CONFIG/"

if [[ -f "$BOOTSTRAP_FML" ]]; then
  cp "$BOOTSTRAP_FML" "$SHIP_CONFIG/fml.toml"
  echo "→ seeded config/fml.toml from pack-bootstrap/"
else
  echo "⚠️  No pack-bootstrap/fml.toml — export may hang on macOS" >&2
fi

count="$(find "$SHIP_CONFIG" -type f | wc -l | tr -d ' ')"
echo ""
echo "✓ config/ updated ($count files)"
echo "  make config-diff     # review drift vs instance"
echo "  packwiz refresh      # if new paths under config/"
