# DMHub Compendium Data (Great Library)

This directory is a **standalone git repository** containing a full export of **all
compendium content from the master "Great Library" game** — the canonical DMHub game
that holds the complete Draw Steel content set. Everything is stored as human-readable
**YAML "Local Assets"**: classes, ancestries/races, kits, careers, cultures, titles,
complications, feats, skills, languages, monsters, global rules, images, audio, maps
tiles/walls/objects, documents, and more.

It is checked in as its own repo (see `.git/`) so the master content can be versioned,
diffed, and re-imported independently of the engine and the codex mod that surround it.

> **How this relates to the rest of the repo.** The parent `draw-steel-codex/` is the
> Lua game-system mod. Its `compendium/` folder holds the technical *reference
> documentation* for these data structures (authored while building this content). The
> evergreen parts of that documentation have been copied here into `docs/` (and
> `GoblinScript_Guide.md`) so that **this data repo is self-documenting** — you can
> understand every YAML structure without leaving this directory.

## Where to look

| You want to... | Go to |
|---|---|
| Understand what the whole export contains | This file (below) |
| Understand any YAML data structure in depth | [`docs/REFERENCE.md`](docs/REFERENCE.md) — the documentation index |
| Build/read a class, subclass, ancestry, kit, complication, title, or treasure | [`docs/reference/CHARACTERS.md`](docs/reference/CHARACTERS.md) |
| Build/read a monster | [`docs/reference/MONSTERS.md`](docs/reference/MONSTERS.md) |
| Understand conditions, ongoing effects, riders | [`docs/reference/CONDITIONS.md`](docs/reference/CONDITIONS.md) |
| Look up UUIDs, table names, common pitfalls | [`docs/reference/CORE.md`](docs/reference/CORE.md) |
| Read formula syntax used throughout the YAML | [`GoblinScript_Guide.md`](GoblinScript_Guide.md) |
| Read the game rules | [`docs/RULES_REFERENCE.md`](docs/RULES_REFERENCE.md) |

## Export format

- **`_manifest.yaml`** (repo root) lists every top-level category and its item count at
  export time, along with `exportedAt`. It is the table of contents for the raw data.
- Each top-level folder is one **asset category**. Files are YAML, one asset per file.
- **File naming** is either a stable **UUID** (`8f3a…-….yaml`) or a human **slug**
  (`censor.yaml`, `human.yaml`). Slugs are used for hand-authored, human-meaningful
  entries; UUID filenames are used for bulk/imported entries. The authoritative id is the
  `id:` field *inside* the file, not the filename.
- Most files carry: `__typeName` (the DMHub C# type this deserializes into), `id`,
  `ctime`/`mtime` (creation/modification epoch millis), and a type-specific body.
- A folder may contain a **`_meta.yaml`** (folder metadata, e.g. `id: classes`) — it is
  not a content item and is excluded from the manifest counts.

## Top-level categories

Counts are as of the export recorded in `_manifest.yaml`.

| Folder | Items | Contents |
|---|---:|---|
| `objectTables/` | 3091 | **The game-system content**, split into ~56 sub-tables (classes, races, kits, monsters group, global rules, …). See the breakdown below — this is where most authored content lives. |
| `imageLibraries/` | 849 | Image library definitions (grouped collections of images used by the compendium). |
| `images/` | 756 | Image asset records (UUID-named), each pointing at the underlying stored image. |
| `monsters/` | 691 | Individual monster/creature asset records (UUID-named). |
| `objects/` | 570 | Map object / prop definitions used by the map editor. |
| `objectFolders/` | 15 | Folder hierarchy grouping `objects/`. |
| `monsterFolders/` | 135 | Folder hierarchy grouping `monsters/`. |
| `tilesheets/` | 28 | Map tile sheets (floor/terrain tiles). |
| `walls/` | 14 | Wall brush definitions for the map editor. |
| `brushes/` | 19 | Map painting brushes. |
| `emoji/` | 15 | Custom emoji assets. |
| `imageAtlas/` | 1 | Packed image atlas metadata. |
| `documentFolders/` | 6 | Folder hierarchy grouping journal documents. |
| `pdfDocuments/` | 21 | PDF reference documents. |
| `audioFolders/` | 7 | Folder hierarchy grouping audio. |
| `audio/` | 62 | Audio clip asset records (music/SFX). |

## `objectTables/` — the game-system content

`objectTables/` holds the Draw Steel rules content, one sub-folder per table. The table
names here are the same ones referenced throughout the documentation (see
[`docs/reference/CORE.md`](docs/reference/CORE.md) → *Table Names*). Counts are current
item counts.

### Character options (documented in [`CHARACTERS.md`](docs/reference/CHARACTERS.md))

| Table | Items | Contents |
|---|---:|---|
| `classes` | 33 | Class definitions: levels, features, characteristic arrays, heroic resource. |
| `subclasses` | 51 | Subclass definitions layered onto classes. |
| `races` | 13 | Ancestries/races (point-buy trait `modifierInfo`). |
| `kits` | 50 | Kits: stat bonuses, damage tiers, signature ability, equipment. |
| `careers` | 20 | Character careers. |
| `cultures` | 26 | Cultures. |
| `cultureaspects` | 15 | Language/environment/upbringing culture aspects. |
| `complications` | 100 | Complications (benefit + drawback pairs). |
| `titles` | 64 | Titles, organized by echelon. |
| `feats` | 71 | Perks/feats. |
| `skills` | 59 | Skills. |
| `backgrounds` | 1 | Background definitions. |
| `deities` | 44 | Deities. |
| `deitydomains` | 12 | Deity domains. |
| `characteristicstable` | 23 | Characteristic definitions/arrays. |
| `characterresources` | 31 | Resource types (heroic resources, recoveries, etc.). |
| `charactertypes` | 1 | Character type definitions. |
| `customattributes` | 143 | Custom character attributes referenced by features/modifiers. |
| `downtimeactivities` | 14 | Downtime/respite activities. |

### Abilities, effects & rules (documented in [`MONSTERS.md`](docs/reference/MONSTERS.md))

| Table | Items | Contents |
|---|---:|---|
| `standardabilities` | 140 | Shared/standard abilities (grab, knockback, etc.). |
| `abilitytemplates` | 11 | Ability area/targeting templates. |
| `globalrulemods` | 40 | Global rule modifiers applied game-wide (`GlobalRuleMod`). |
| `characterongoingeffects` | 931 | Ongoing effects (`CharacterOngoingEffect`) — the largest table. |
| `charconditions` | 36 | Conditions (`CharacterCondition`). |
| `conditionriders` | 91 | Condition riders (`ConditionRider`). |
| `characterresources` | (above) | — |
| `damagetypes` | 12 | Damage types. |
| `weaponproperties` | 9 | Weapon property definitions. |
| `equipmentcategories` | 8 | Equipment categorization. |
| `tbl-gear` | 497 | Gear / treasure / equipment items. |
| `currency` | 1 | Currency definitions. |
| `powerrolls` | 1 | Power roll configuration. |
| `featureprefabs` | 7 | Reusable feature prefabs. |
| `creaturetemplates` | 6 | Creature templates applied to monsters. |

### Monsters & encounters (documented in [`MONSTERS.md`](docs/reference/MONSTERS.md))

| Table | Items | Contents |
|---|---:|---|
| `monstergroup` | 110 | Monster group / "band" definitions. |
| `minionwithcaptain` | 10 | Minion-with-captain groupings. |
| `encounters` | 5 | Prebuilt encounters. |
| `negotiators` | 3 | Negotiation NPC definitions. |
| `montagetests` | 2 | Montage test definitions. |
| `adventuretables` | 7 | Adventure/random tables. |
| `parties` | 6 | Party definitions. |

### World & flavor

| Table | Items | Contents |
|---|---:|---|
| `languages` | 72 | Languages. |
| `languagerelations` | 18 | Language relationship graph. |
| `namegenerators` | 47 | Name generators. |
| `documents` | 85 | Journal/reference documents. |
| `pdfreferences` | 2 | PDF reference links. |
| `journalstyles` | 13 | Journal styling presets. |
| `visiontype` | 1 | Vision type definitions. |
| `campaignnotes` | 1 | Campaign notes. |
| `compendiumpermissions` | 6 | Compendium permission records. |
| `audioplaylists` | 4 | Audio playlists. |
| `audiovariantpools` | 1 | Audio variant pools. |

### Importer intermediates

These tables hold data used by the content importer pipeline (parsing source books into
DMHub structures); they are not usually hand-authored.

| Table | Items |
|---|---:|
| `importerabilityeffects` | 18 |
| `importermonstertraits` | 46 |
| `importerpowertableeffects` | 53 |
| `importerstandardfeatures` | 20 |

## Notes

- **GoblinScript** — most numeric/conditional fields (damage, ranges, conditions,
  triggers) are GoblinScript formula strings. Read [`GoblinScript_Guide.md`](GoblinScript_Guide.md)
  and the `docs/reference/GOBLINSCRIPT-*.md` files before editing formula fields.
- **UUID cross-references** — YAML fields frequently reference other entries by UUID
  (resource ids, condition ids, damage types, keywords). The lookup maps are in
  [`docs/reference/CORE.md`](docs/reference/CORE.md).
- **Editing** — these files are consumed by DMHub's Local Assets loader. Prefer editing
  via the app where possible; hand-edits must keep `__typeName` and `id` intact and stay
  ASCII-only (see the ASCII rule in `docs/reference/CORE.md`).
