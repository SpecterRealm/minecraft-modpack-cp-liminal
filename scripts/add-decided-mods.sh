#!/usr/bin/env bash
# archers and rogues-and-warriors are CurseForge slugs (projects 932359, 1048409); use the curseforge source for them.
# Add the decided mods to one pack. Needs packwiz and network access to Modrinth/CurseForge.
set -u
dir=${1:?pack repo dir}; src=${2:?modrinth|curseforge}; pack=${3:?verdant|elysian|influx|liminal}
case $pack in
  verdant) mods="cosmetic-armor-reworked mekanism-turrets archers" ;;
  elysian) mods="wizards cosmetic-armor-reworked rogues-and-warriors" ;;
  influx)  mods="paladins-and-priests bard-more-rpg-classes genetics-resequenced mutant-monsters cosmetic-armor-reworked" ;;
  liminal) mods="wizards paladins-and-priests bard-more-rpg-classes genetics-resequenced mutant-monsters cosmetic-armor-reworked mekanism-turrets archers rogues-and-warriors" ;;
  *) echo "unknown pack $pack" >&2; exit 1 ;;
esac
cd "$dir" || exit 1
for m in $mods; do
  case $m in \?*) echo "SKIP (slug unconfirmed): ${m#?}"; continue ;; esac
  packwiz "$src" add "$m" || echo "FAILED: $m"
done
packwiz refresh
