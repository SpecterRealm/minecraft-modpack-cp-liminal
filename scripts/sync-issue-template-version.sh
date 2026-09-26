#!/usr/bin/env bash
# Set pack-version default/placeholder in GitHub issue forms from pack.toml.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PACK_TOML="$ROOT/pack.toml"
VERSION="${1:-}"

if [[ -z "$VERSION" ]]; then
  VERSION="$(grep -E '^version\s*=' "$PACK_TOML" | sed 's/.*= "\(.*\)"/\1/')"
fi

if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
  echo "Invalid or missing version (pack.toml or argument): '$VERSION'" >&2
  exit 1
fi

TEMPLATES=(
  "$ROOT/.github/ISSUE_TEMPLATE/crash.yaml"
  "$ROOT/.github/ISSUE_TEMPLATE/quest_issue.yaml"
  "$ROOT/.github/ISSUE_TEMPLATE/recipe_issue.yaml"
)

for f in "${TEMPLATES[@]}"; do
  [[ -f "$f" ]] || { echo "Missing template: $f" >&2; exit 1; }
  python3 - "$f" "$VERSION" <<'PY'
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
version = sys.argv[2]
text = path.read_text()
lines = text.splitlines(keepends=True)

in_pack_version = False
seen_default = False
out: list[str] = []

for line in lines:
    if re.match(r"\s+id: pack-version\s*$", line):
        in_pack_version = True
        seen_default = False
        out.append(line)
        continue

    if in_pack_version and re.match(r"\s+id: ", line):
        in_pack_version = False

    if in_pack_version and re.match(r"\s+default: ", line):
        out.append(f"      default: '{version}'\n")
        seen_default = True
        continue

    if in_pack_version and re.match(r"\s+placeholder: ", line):
        if not seen_default:
            out.append(f"      default: '{version}'\n")
            seen_default = True
        out.append(f"      placeholder: '{version}'\n")
        continue

    out.append(line)

path.write_text("".join(out))
PY
  echo "  $(basename "$f"): pack-version → $VERSION"
done

echo "Issue templates synced to pack version $VERSION"
