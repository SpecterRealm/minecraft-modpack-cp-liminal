# Colony Protocol: Liminal — Quest reward tables (scaffold)

**Spine:** Planetfall foothold → parallel V/E/I reunite → colonial / resistance / TechnoMage (stubs)

**Locks applied:** teach + QoL rewards · never sole progression path · Field Manual topic advancements · flexible progression · learning ladder.

| Chapter | Quest | QoL reward | Field Manual advancement | Notes |
|---------|-------|------------|--------------------------|-------|
| Welcome | Field Manual | Field Manual | `orientation + liminal/planetfall` |  |
| Mechanical Path | Sieve & Factory Reminder | bread | `specterrealm:field_manual/liminal/mechanical_reunite` | Parallel Mid stub |
| Magic Path | Source & Grow Reminder | bread | `specterrealm:field_manual/liminal/magic_reunite` | Parallel Mid stub |
| Lab Path | Convert & Breed Reminder | bread | `specterrealm:field_manual/liminal/lab_reunite` | Parallel Mid stub |
| Colonial Settle | Settle Fantasy (stub) | xp | `specterrealm:field_manual/liminal/colonial` | Late stub |
| Resistance | Pushback (stub) | xp | `specterrealm:field_manual/liminal/resistance` | Late stub |
| TechnoMage | Veil Comprehension (stub) | xp | `specterrealm:field_manual/liminal/technomage` | Late stub |
| Side Quests | Optional Paths (stub) | xp | `specterrealm:field_manual/liminal/side_niches` | Late stub |

## Placeholder Manual topic IDs

- `specterrealm:field_manual/orientation`
- `specterrealm:field_manual/liminal/planetfall`
- `specterrealm:field_manual/liminal/early_stash`
- `specterrealm:field_manual/liminal/silent_gear`
- `specterrealm:field_manual/liminal/mechanical_reunite`
- `specterrealm:field_manual/liminal/magic_reunite`
- `specterrealm:field_manual/liminal/lab_reunite`
- `specterrealm:field_manual/liminal/bridges`
- `specterrealm:field_manual/liminal/colonial`
- `specterrealm:field_manual/liminal/resistance`
- `specterrealm:field_manual/liminal/technomage`
- `specterrealm:field_manual/liminal/side_niches`

Advancement JSON + Patchouli entries land in `specterrealm-core` later (see series `field-manual-architecture.md`). Scaffold grants IDs now so quest wiring is ready.

## Starter quest book

FTB Quests does **not** auto-give `ftbquests:book` on NeoForge 1.21.1 (2101.x). This pack ships `kubejs/server_scripts/quest_book_login.js` to grant the book if missing, plus `options.txt` binding **B** to the quest journal (Elysian #16 / Verdant keybind pattern).
