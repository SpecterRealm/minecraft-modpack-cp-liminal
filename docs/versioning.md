# Pack versioning — Colony Protocol: Liminal

**Single source of truth:** `pack.toml` → `version = "x.y.z"`

| Output | Pattern |
|--------|---------|
| CurseForge zip | `dist/Colony-Protocol-Liminal-<version>-curseforge.zip` |
| Modrinth pack | `dist/Colony-Protocol-Liminal-<version>.mrpack` |
| Changelog | Root `CHANGELOG.md` |

## Semver

| Bump | When |
|------|------|
| **MAJOR** | Save-breaking or new pack era |
| **MINOR** | New quests/chapters, new mods, progression |
| **PATCH** | Bugfixes, config/text only |

Pre-release: `-dev.N` (internal), `-rc.N` (tester handoff).

## Maintainer rules

- Do **not** bump `pack.toml` version in feature PRs (CI blocks).
- Tag releases from `main` only after merge.
- Bump: `make set-version VERSION=x.y.z` then update `CHANGELOG.md`.

Tooling from CP Verdant `docs/pack-template.md` / `docs/versioning.md`.
