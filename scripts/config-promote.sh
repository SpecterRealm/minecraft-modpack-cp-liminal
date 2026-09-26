#!/usr/bin/env bash
# config-promote.sh — copy paths from Prism instance config/ into repo config/.
# Usage: make config-promote PROMOTE="exdeorum-common.toml Mekanism/general.toml"

set -euo pipefail

# shellcheck source=config-instance-env.sh
source "$(dirname "$0")/config-instance-env.sh"

if [[ $# -eq 0 ]]; then
  echo "Usage: make config-promote PROMOTE=\"file.toml [subdir/…]\"" >&2
  echo "  Paths are relative to config/." >&2
  exit 1
fi

config_instance_require

for rel in "$@"; do
  rel="${rel#config/}"
  src="$INSTANCE_CONFIG/$rel"
  dest="$SHIP_CONFIG/$rel"
  if [[ ! -e "$src" ]]; then
    echo "✗ Not on instance: $rel" >&2
    exit 1
  fi
  mkdir -p "$(dirname "$dest")"
  if [[ -d "$src" ]]; then
    rsync -a "$src/" "$dest/"
    echo "→ promoted directory $rel/"
  else
    cp -f "$src" "$dest"
    echo "→ promoted $rel"
  fi
done

echo ""
echo "Next: packwiz refresh   # if new paths under config/"
echo "      git add config/"
