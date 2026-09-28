# CurseForge export — Colony Protocol: Liminal

**CF project:** [colony-protocol-liminal](https://www.curseforge.com/minecraft/modpacks/colony-protocol-liminal) · Authors / project id **`1715485`**  
Set GitHub repo variable `CURSEFORGE_PROJECT_ID=1715485` when upload automation is wired (Verdant `curseforge-upload.md` pattern).

**Default:** `make export-cf` → `dist/Colony-Protocol-Liminal-<version>-curseforge.zip`

## Rules (match Verdant)

| Rule | Why |
|------|-----|
| CF-hosted mods → **`manifest.json` only** | Moderation rejects those JARs in `overrides/mods/` |
| Never add a repo folder named `overrides/` | Produces nested `overrides/overrides/` |
| Pin Sodium/Iris with `--file-id` | Latest alpha breaks Iris pairing |

## NeoForge 1.21.1 pins (from Verdant — already soft-pinned here)

Shared stack includes Sodium + Iris from Verdant `mods/*.pw.toml`. Before first CF upload, re-read Verdant `docs/curseforge-export.md` for current file IDs and `make validate-export`.

## Non-CurseForge JARs

Only approved JARs in `overrides/mods/` (target: SpecterRealm Core). See CurseForge Non-CurseForge mods policy.
