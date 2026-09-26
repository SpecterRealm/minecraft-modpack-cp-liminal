#!/usr/bin/env bash
# Shared rsync exclude flags for config snapshot + full ship.
# Source from other scripts: source "$(dirname "$0")/config-ship-excludes.sh"
# shellcheck disable=SC2034
CONFIG_RSYNC_EXCLUDES=(
  --exclude='.DS_Store'
  --exclude='*.bak'
  --exclude='README.md'
  --exclude='.synced-at'
  --exclude='sodium-fingerprint.json'
  --exclude='sodium-options.json'
  --exclude='iris.properties'
  --exclude='iris-excluded.json'
  --exclude='xaerohud.txt'
  --exclude='xaeropatreon.txt'
  --exclude='xaero/'
  --exclude='fabric/'
  --exclude='fancymenu/user_variables.db'
  --exclude='fancymenu/layout_editor/'
  --exclude='fancymenu/legacy_checklist.txt'
  --exclude='fancymenu/ui_themes/'
  --exclude='inventoryprofilesnext/Test/'
  --exclude='inventoryprofilesnext/20may/'
  --exclude='inventoryprofilesnext/30May/'
  --exclude='inventoryprofilesnext/31 May/'
)
