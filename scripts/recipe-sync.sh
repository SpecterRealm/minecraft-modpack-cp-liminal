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
# Leftover generated dump files (from an earlier run that stopped early) are not real changes: discard them
GEN_EXCLUDES=(':(exclude)docs/recipe_data.json' ':(exclude)docs/recipe-analyze' ':(exclude)docs/recipe_wiki.html')
if [ -n "$(git status --porcelain --untracked-files=no)" ] && [ -z "$(git status --porcelain --untracked-files=no -- . "${GEN_EXCLUDES[@]}")" ]; then
  echo "Discarding leftover generated dump files (they are regenerated each run):"
  git status --porcelain --untracked-files=no
  git checkout -- docs/recipe_data.json docs/recipe-analyze 2>/dev/null || true
  git checkout -- docs/recipe_wiki.html 2>/dev/null || true
fi
[ -z "$(git status --porcelain --untracked-files=no)" ] || die "tracked files have uncommitted changes. Commit or stash them first."

if [ ! -f "$BOOTSTRAP_JAR" ] || [ ! -f "$INSTALLER_JAR" ]; then
  say "Installer jars missing; downloading"
  curl -fsSL -o "$BOOTSTRAP_JAR" "$BOOTSTRAP_URL"
  curl -fsSL -o "$INSTALLER_JAR" "$INSTALLER_URL"
fi

cleanup() { make --no-print-directory serve-stop >/dev/null 2>&1 || true; }
trap cleanup EXIT

# One packwiz serve at a time: port 8080 is shared by every pack
if command -v lsof >/dev/null 2>&1 && lsof -nP -iTCP:8080 -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Port 8080 is already in use:"
  lsof -nP -iTCP:8080 -sTCP:LISTEN | head -3
  make --no-print-directory serve-stop >/dev/null 2>&1 || true
  sleep 1
  if lsof -nP -iTCP:8080 -sTCP:LISTEN >/dev/null 2>&1; then
    die "something else still listens on 8080 (listed above). Stop it (a serve from another pack: cd there and make serve-stop) and run again."
  fi
fi

say "Refreshing the index and starting packwiz serve"
if ! make --no-print-directory serve-bg; then
  echo; echo "--- last lines of .serve.log ---"; tail -20 .serve.log 2>/dev/null || true
  die "packwiz serve did not start (log above). Common cause: port 8080 in use by another pack's serve (make serve-stop there)."
fi
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
INSTALL_LOG=$(mktemp)
if ! ( cd "$DEV_MC_DIR" && "$JAVA" -jar "$BOOTSTRAP_JAR" -g --bootstrap-no-update "$PACK_URL" ) 2>&1 | tee "$INSTALL_LOG"; then
  :
fi
if grep -q "Failed to download modpack\|Update cancelled" "$INSTALL_LOG"; then
  echo
  if grep -q "must be downloaded manually" "$INSTALL_LOG"; then
    echo "These mods are excluded from the CurseForge API and must be downloaded by hand."
    echo "Download each file in a browser, save it to the path shown, then run make recipe-sync again:"
    grep -A1 "must be downloaded manually" "$INSTALL_LOG" | grep "Please go to" | sort -u | sed 's/^/  /'
  fi
  rm -f "$INSTALL_LOG"
  die "packwiz installer failed (details above). The same mods block the Prism launch too."
fi
rm -f "$INSTALL_LOG"

say "Stopping packwiz serve"
cleanup
trap - EXIT

say "Removing instance jars that are not in mods/*.pw.toml"
make --no-print-directory prune-dev-mods

say "Recipe and item dump"
make --no-print-directory recipe-pr
