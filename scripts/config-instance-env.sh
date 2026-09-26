#!/usr/bin/env bash
# Shared Prism dev instance paths for config sync/diff/promote scripts.
# shellcheck disable=SC2034
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PRISM_DATA="${PRISM_DATA:-$HOME/Library/Application Support/PrismLauncher}"
PRISM_INSTANCE="${PRISM_INSTANCE:-CP-Verdant-Dev}"
DEV_MC_DIR="${DEV_MC_DIR:-$PRISM_DATA/instances/$PRISM_INSTANCE/minecraft}"
INSTANCE_CONFIG="${INSTANCE_CONFIG:-$DEV_MC_DIR/config}"
SHIP_CONFIG="$REPO_ROOT/config"
BOOTSTRAP_FML="$REPO_ROOT/pack-bootstrap/fml.toml"

config_instance_require() {
  if [[ ! -d "$INSTANCE_CONFIG" ]]; then
    echo "✗ Instance config not found: $INSTANCE_CONFIG" >&2
    echo "  Set PRISM_INSTANCE / DEV_MC_DIR if not using CP-Verdant-Dev." >&2
    return 1
  fi
}
