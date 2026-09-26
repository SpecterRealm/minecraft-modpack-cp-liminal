#!/usr/bin/env bash
# Bump pack version in pack.toml (single source of truth for exports).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PACK_TOML="$ROOT/pack.toml"
NEW="${1:-}"

if [[ -z "$NEW" ]]; then
  echo "Usage: $0 <x.y.z>   or: make set-version VERSION=x.y.z" >&2
  exit 1
fi

if [[ ! "$NEW" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
  echo "Version must look like semver x.y.z (optional -prerelease): got '$NEW'" >&2
  exit 1
fi

if [[ ! -f "$PACK_TOML" ]]; then
  echo "Missing $PACK_TOML" >&2
  exit 1
fi

OLD="$(grep -E '^version\s*=' "$PACK_TOML" | sed 's/.*= "\(.*\)"/\1/')"
if [[ "$OLD" == "$NEW" ]]; then
  echo "pack.toml already at version $NEW"
  bash "$ROOT/scripts/sync-issue-template-version.sh" "$NEW"
  echo "Next: add/update ## [$NEW] in CHANGELOG.md if needed."
  echo "Then either:"
  echo "  - GitHub release flow: make release VERSION=$NEW  (or make release CHANNEL=rc/dev/prod)"
  echo "  - Local/manual exports: make refresh && make all"
  exit 0
fi

if [[ "$(uname)" == Darwin ]]; then
  sed -i '' "s/^version = .*/version = \"$NEW\"/" "$PACK_TOML"
else
  sed -i "s/^version = .*/version = \"$NEW\"/" "$PACK_TOML"
fi

echo "pack.toml: $OLD → $NEW"
bash "$ROOT/scripts/sync-issue-template-version.sh" "$NEW"
echo "Next: add a ## [$NEW] section to CHANGELOG.md."
echo "Then either:"
echo "  - GitHub release flow: make release VERSION=$NEW  (or make release CHANNEL=rc/dev/prod)"
echo "  - Local/manual exports: make refresh && make all"
