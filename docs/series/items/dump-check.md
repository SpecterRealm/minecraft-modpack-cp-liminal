# Dump check: installed-mod recipe dump against the series catalog

Checked on 2026-10-01 against the second clean Liminal dump (`docs/recipe_data.json`, 199 jars, 11,069 recipe-result items, 134 namespaces) and `mods/*.pw.toml` at the same commit. Method: compare the dump's namespaces, `scan/*.json` mod ids, `profiles.json` and the pack's mod list.

## Result

| Check | Result |
|---|---|
| Pack mods with no `scan/` file and no `profiles.json` entry | **19 of 199**, the same 19 in both lists (below) |
| Installed namespaces in the dump with no scan item list | `appliedcreate` (35 items, a real pack mod), `irons_lib`, `productivelib` (libraries) |
| Pack mods missing from the dump entirely | none that add items (the 19 below are structures, client mods, libraries and add-ons) |
| Profiles for mods not in the Liminal pack | 57 (removed mods and mods of other packs; harmless, kept for the other packs and history) |

## The 19 pack mods without scan or profile

| Group | Mods | Needs a profile? |
|---|---|---|
| Structures and worldgen | `forest-watchtower`, `jungle-treehouse-village`, `ruined-lighthouse`, `skeleton-ghost-ship`, `underwater-village`, `wizard-tower`, `illager-arena`, `terralith` | No items. One-line profile only (they belong in the Liminal structure review) |
| Client and quality of life | `essential-mod`, `xaeros-minimap`, `xaeros-world-map`, `invtweaks-emu-for-ipn` | No items; one-line profile |
| Libraries and add-ons | `irons-lib`, `kubejs-eyejs`, `applied-kubejs-kjs-ae2`, `tough-as-nails-vanilla-pack`, `specterrealm` | No items; one-line profile |
| **Adds items** | **`applied-create`** (35 items: pattern providers, stress cells and circuits), **`useful-projecte`** | **Yes: profile and item list** |

So the real catalog gaps are `applied-create` and `useful-projecte`. The dump already has `applied-create`'s item ids (`docs/recipe-analyze/by-mod/appliedcreate.txt`).

## Counts that look different but are not gaps

- `mekanismgenerators` shows 1,073 scan items against 31 dump results: the Mekanism repo's language file also lists Tools, Additions and fluids and blocks that have no recipe. Scan counts are language-file totals, the dump counts items that are crafted. Do not compare them directly.
- `mysticalagriculture` (195 scan, 387 dump) and `theurgy` (116 scan, 358 dump): the dump sees generated crop and essence items that the language file does not list one by one.
- `ars_elemancy` (105 scan, 21 dump): installed in Liminal and removed from Elysian only, so expected.

## Analyzer bug found by this check (fixed)

The first version of the analyzer counted any `modId = "..."` in a jar's metadata as an installed mod, including optional dependencies. That marked `immersiveengineering` (an optional dependency of another mod, not in the pack) as installed, and it hid at least one phantom namespace (`silentgems`: recipes shipped by another jar, no Silent Gems jar). The analyzer now reads only `[[mods]]` entries. After the next `make recipe-pr`, the summary's list of namespaces with no installed jar will be longer, and `immersiveengineering` and `silentgems` will be in it.

## Done in the follow-up

- `profiles.json` now has all 19 (`series-profiles.py check` passes; `mod-profiles.md` regenerated).
- **`applied-create`**: profiled from the dump. 36 items: andesite and brass pattern providers, ME gearbox, kinetic energy acceptor, stress circuits (AE2 inscriber), stress storage cells and components from 1k to 256m, creative stress cell. Rated good for Liminal (an AE2 and Create bridge) and partial for Verdant. No scan file: there is no public repo, so the dump is its item source.
- **`useful-projecte`**: the installed jar (`emc_transfer_fill_mod`) has **no items and no recipes in the dump**. It is a behavior mod; what it does is unverified. Check in game before keeping it.
- The other 17 got one-line profiles marked not reviewed.

## Next

1. Re-run `make recipe-sync` after the analyzer fix merges to correct the installed list.
2. Check `useful-projecte` in game.
