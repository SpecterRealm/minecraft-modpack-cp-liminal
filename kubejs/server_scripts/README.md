# server_scripts

| Script | Role |
|--------|------|
| `quest_book_login.js` | Give `ftbquests:book` if missing on join + short login tip |
| `emi_hide_creative.js` | Tag creative/unobtainable items → `c:hidden_from_recipe_viewers` |
| `recipe_dump.js` | Dev: log recipe counts by type on world load (`[CPL]`). Comment out before release. |

Offline JAR+KubeJS index: `make recipe-wiki` / `docs/recipe-wiki.md` (do not reuse Verdant `recipe_data.json`).

Client companion: `kubejs/client_scripts/emi_hide_creative.js`.

## Recipe viewer (EMI++)

Stack groups: `kubejs/assets/cpliminal/stack_groups/` (Verdant port — SS, backpacks, Silent Gear, Comforts, armor, Ex Deorum sieves, portable tanks, filled buckets). Config: `config/emixx/emixx-client.toml`.

See design: [Liminal `docs/series/pack-architecture.md`](https://github.com/SpecterRealm/minecraft-modpack-cp-liminal/blob/main/docs/series/pack-architecture.md); pack scope in `docs/pack-identity.md`.
