#!/usr/bin/env bash
# config-diff.sh — compare repo config/ vs live Prism instance config/

set -euo pipefail

# shellcheck source=config-instance-env.sh
source "$(dirname "$0")/config-instance-env.sh"

config_instance_require

echo "Instance: $INSTANCE_CONFIG"
echo "Shipped:  $SHIP_CONFIG"
echo ""

echo "── Files that differ (shipped vs instance)"
DIFFERING="$(diff -rq "$SHIP_CONFIG" "$INSTANCE_CONFIG" 2>/dev/null | grep ' differ$' || true)"
if [[ -z "$DIFFERING" ]]; then
  echo "  (none)"
else
  echo "$DIFFERING"
fi

echo ""
echo "── Only in config/ (pack repo; not on instance)"
diff -rq "$SHIP_CONFIG" "$INSTANCE_CONFIG" 2>/dev/null | grep "Only in $SHIP_CONFIG" || true

echo ""
echo "── Only on instance (not in repo config/)"
diff -rq "$SHIP_CONFIG" "$INSTANCE_CONFIG" 2>/dev/null | grep "Only in $INSTANCE_CONFIG" || true

echo ""
echo "Tip: copy selected paths with  make config-promote PROMOTE=\"relative/path.toml\""
