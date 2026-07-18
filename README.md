# Draw Steel Data

This repository is the complete compendium content for MCDM's **Draw Steel** RPG as it
ships in the **Draw Steel Codex** virtual tabletop
([get the Codex on Steam](https://store.steampowered.com/app/2902740/Draw_Steel/)).
It is a full export of the master "Great Library" game -- every class, ancestry, kit,
career, complication, title, monster, ability, condition, item, image record, audio
record, map tile, and journal document -- stored as human-readable YAML, one asset per
file.

The repo is self-documenting:

| You want to... | Go to |
|---|---|
| See what the export contains, category by category | [`DATA_REFERENCE.md`](DATA_REFERENCE.md) |
| Understand any YAML data structure in depth | [`docs/REFERENCE.md`](docs/REFERENCE.md) |
| Read the formula language used throughout the YAML | [`GoblinScript_Guide.md`](GoblinScript_Guide.md) |
| Read the game rules | [`docs/RULES_REFERENCE.md`](docs/RULES_REFERENCE.md) |

## Loading This Data Into the Codex

The Codex can point a game at a local directory of YAML asset files instead of its cloud
assets. This is the **Local Assets** developer feature, and it is how you run a game
directly off a clone of this repo: the game loads its compendium from your working copy,
edits you make in-game are written back to the files, and edits you make in a text
editor hot-reload into the running game.

### 1. Clone the repo

```
git clone https://github.com/VerisimLLC/draw-steel-data.git
```

### 2. Turn on Developer Mode

The Local Assets section only appears in Developer Mode. In the Codex, open **Settings**
and enable the **Developer Mode** checkbox, or type `/dev true` into the in-game chat.

### 3. Point your game at the clone

Local Assets is configured **per game**, so start by opening the game you want to use.

1. Open **Settings** and go to the **Editing** tab.
2. Scroll to the **Local Assets (Developer)** section.
3. In the **Directory** field, enter the path to your clone (or click **Browse...** and
   pick the folder).
4. The status line under the buttons now reads *"Set, but not active yet: reload the
   game to activate."*
5. Leave the game and re-enter it (the directory is read when the game loads).
6. Check the status line again: it should read *"Active: this game's assets are loading
   from &lt;your path&gt;."*

> **Do not click "Populate Directory" when pointing at this repo.** Populate exports the
> game's *current cloud assets* into the directory, overwriting any files with matching
> names -- it would stomp the repo's content with whatever the game had before. Populate
> exists for the opposite workflow: filling an *empty* directory to start a fresh export
> of your own game. (The app warns before populating a non-empty directory, and the
> button disables itself once local assets are active with files present.)

While active:

- The game's **cloud assets are ignored entirely**; everything loads from the directory.
- **Edits made in-game** (the compendium editor, monster sheets, etc.) are **written
  back to the directory as YAML**.
- **External changes to the files** -- your text editor, `git pull`, a branch switch --
  **hot-reload into the running game** within a few seconds of saving.
- If you point the setting at a directory that does not exist, it is created and
  populated from the game's assets automatically on next load.

## Staying in Sync: What You Are Signing Up For

Pointing a game at a git clone makes your working tree part of the game's live state.
Understand the consequences before you commit to it:

- **Your clone becomes the single source of truth for that game.** The cloud copy of the
  game's assets is frozen at whatever it held when you switched over; nothing you do in
  local mode is uploaded to it.
- **Playing dirties your working tree.** Every in-game edit -- tweaking a monster,
  renaming an item, even edits made incidentally during play -- writes YAML into your
  clone. Check `git status` regularly and commit or discard deliberately, or real
  changes will sit unversioned in your working copy.
- **The app rewrites files in its own canonical format.** When the in-app compendium
  saves an asset it regenerates the whole file: key order, quoting, and `mtime`
  timestamps change, and a file may be renamed if you rename the asset in-game. Expect
  noisy diffs that mix your intended change with formatting churn, and do not count on
  hand-crafted comments or formatting surviving (YAML comments are not preserved).
- **Pulling upstream changes affects a running game immediately.** `git pull` while the
  game is open hot-reloads the changed assets. Merge conflicts between upstream edits
  and your local in-game edits are ordinary git conflicts -- resolve them in the YAML,
  save, and the game picks up the result.
- **Switching back to cloud assets abandons local changes.** Clearing the Directory
  setting returns the game to its (stale) cloud assets. Your local edits stay in the
  clone -- nothing merges them back to the cloud.

A good habit: treat the clone like any other source checkout. Work on a branch, commit
after a play or editing session with a message describing what changed, and keep an eye
on `git diff` so app-driven rewrites do not smuggle in changes you did not intend.

## YAML Structure

Each top-level folder is an asset category; `objectTables/` holds the game-system
content, one sub-folder per table (classes, monsters, kits, ongoing effects, and so on
-- see [`DATA_REFERENCE.md`](DATA_REFERENCE.md) for the full breakdown). Files are one
asset each, named either by a human slug (`alchemy.yaml`) or a UUID; **the authoritative
id is the `id:` field inside the file, not the filename**. `_manifest.yaml` at the root
is the export's table of contents, and a folder's `_meta.yaml` holds folder metadata,
not content.

Most files share a common shape: a `__typeName` (the engine type the file deserializes
into), an `id`, `ctime`/`mtime` epoch-millisecond timestamps, and a type-specific body.
A small entry is entirely readable:

```yaml
# objectTables/skills/alchemy.yaml
__typeName: Skill
id: cdae52cd-ef20-461d-ae18-253023cdb827
mtime: 1768772481184
name: Alchemy
description: Make bombs and potions
attribute: rea
ctime: 1699774846758
specializations: []
_table: Skills
```

Values can nest typed objects (`__usertype`) and reference other assets by UUID:

```yaml
# objectTables/damagetypes/fire-b9044969.yaml
__typeName: DamageType
id: b3ae972b-0b4a-4810-b331-36f98000843b
hidden: true
mtime: 1704705257439
ctime: 1699689533018
display:
  bgcolor:
    __usertype: LuaColor
    h: 0
    s: 0.857422232627869
    v: 0.977229297161102
    a: 1
  hueshift: 0
  brightness: 1
  saturation: 1
iconid: 6be37af0-e113-46ca-aec3-e72d57abb185
name: Fire
_table: damageTypes
```

Larger entries -- classes, monsters, abilities -- nest much deeper: features contain
modifiers, abilities contain behaviors, and numeric or conditional fields (damage,
distances, triggers, prerequisites) are **GoblinScript** formula strings evaluated at
runtime. Read [`GoblinScript_Guide.md`](GoblinScript_Guide.md) before editing formula
fields, and the type-by-type references under [`docs/reference/`](docs/reference/)
before authoring new entries.

When hand-editing:

- Keep `__typeName` and `id` intact -- they are how the engine types and identifies the
  asset. UUID fields that reference other assets must point at real entries.
- **ASCII only.** No em dashes, curly quotes, or other Unicode punctuation.
- Remember the in-app compendium writes these same files: your formatting will be
  normalized the next time the asset is saved in-game, so put durable information in the
  data, not in the layout.

## AI Policy

We do allow contributions to this repository that are written using AI tooling, however all contributions must be read, and understood by a human engineer who can take responsibility for them. When making pull requests, please disclose if any substantial part of the code was written using AI.

We are wary about the prospect of being flooded with pull requests that contain large amounts of generated code, so we may decline to accept substantial sized PR's, especially if they use AI generation since accepting PR's means that the maintainers have to take full responsibility for them. If you want to make extensive modifications, consider using your own mod to do so.