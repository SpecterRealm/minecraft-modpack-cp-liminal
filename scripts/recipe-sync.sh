#!/usr/bin/env bash
# make recipe-sync: bring the Prism dev instance in line with the pack (headless packwiz install),
# drop jars that are not in mods/*.pw.toml, then run make recipe-pr (branch, dump, commit, PR).
# Close the game and Prism's instance window first. Needs: packwiz, java, curl, python3, git.
set -euo pipefail

: "${DEV_MC_DIR:?run via make recipe-sync}"
: "${BOOTSTRAP_JAR:?run via make recipe-sync}"
: "${INSTALLER_JAR:?run via make recipe-sync}"
JAVA=${JAVA:-java}
# The dump must read the same instance this script just synced
export RECIPE_WIKI_MODS_DIR="$DEV_MC_DIR/mods"
PACK_URL=${PACK_URL:-http://localhost:8080/pack.toml}

say() { printf '\n==> %s\n' "$*"; }
die() { printf '\nSTOP: %s\n' "$*" >&2; exit 1; }

for tool in packwiz "$JAVA" curl python3 git; do
  command -v "$tool" >/dev/null || die "$tool not found on PATH"
done
[ -d "$DEV_MC_DIR" ] || die "instance folder not found: $DEV_MC_DIR (create the Prism instance and run make setup-dev once)"
[ -z "$(git status --porcelain --untracked-files=no)" ] || die "tracked files have uncommitted changes. Commit or stash them first."

if [ ! -f "$BOOTSTRAP_JAR" ] || [ ! -f "$INSTALLER_JAR" ]; then
  say "Installer jars missing; downloading"
  curl -fsSL -o "$BOOTSTRAP_JAR" "$BOOTSTRAP_URL"
  curl -fsSL -o "$INSTALLER_JAR" "$INSTALLER_URL"
fi

cleanup() { make --no-print-directory serve-stop >/dev/null 2>&1 || true; }
trap cleanup EXIT

say "Refreshing the index and starting packwiz serve"
make --no-print-directory serve-bg
# serve-bg refreshes the index; a changed index is a pack change that must be committed on its own
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  git status --short
  die "packwiz refresh changed tracked files (see above). Commit that first, then run make recipe-sync again."
fi

for i in $(seq 1 20); do
  curl -fsS -o /dev/null "$PACK_URL" 2>/dev/null && break
  [ "$i" = 20 ] && die "packwiz serve did not answer on $PACK_URL (see .serve.log)"
  sleep 1
done

say "Installing the pack into $DEV_MC_DIR (headless packwiz installer)"
( cd "$DEV_MC_DIR" && "$JAVA" -jar "$BOOTSTRAP_JAR" -g --bootstrap-no-update "$PACK_URL" ) \
  || die "packwiz installer failed. Check the output above."

say "Stopping packwiz serve"
cleanup
trap - EXIT

say "Removing instance jars that are not in mods/*.pw.toml"
make --no-print-directory prune-dev-mods

say "Recipe and item dump"
make --no-print-directory recipe-pr
