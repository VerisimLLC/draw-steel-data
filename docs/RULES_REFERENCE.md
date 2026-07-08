# Draw Steel -- Mechanical Rules Reference

Extracted from Draw Steel: Heroes v1.01 and Draw Steel: Monsters.
This is a concise summary of mechanical rules only -- no lore, flavor, or individual stat blocks.

## Characteristics

Five characteristics, scored from -5 to +5:
- **Might (mgt)**: Strength, brawn
- **Agility (agl)**: Coordination, nimbleness
- **Reason (rea)**: Logic, education
- **Intuition (inu)**: Instincts, experience
- **Presence (prs)**: Force of personality

## Power Rolls

Roll **2d10 + characteristic**.

| Tier | Total |
|------|-------|
| Tier 1 | <= 11 |
| Tier 2 | 12-16 |
| Tier 3 | >= 17 |

**Natural 19-20** (unmodified 2d10): Always tier 3. On ability rolls using a main action, also a **critical hit** (grants extra main action).

**Downgrading**: Can always choose a lower tier.

### Edges and Banes

- **Edge**: +2 bonus. **Bane**: -2 penalty. Capped at 2 each.
- **Double Edge** (2+ edges, 0 banes): Auto-increase tier by 1.
- **Double Bane** (2+ banes, 0 edges): Auto-decrease tier by 1.
- Cancellation: 1 edge + 1 bane = normal. Double + double = normal.

## Combat Structure

### Turn Order
- Two sides alternate choosing who acts.
- Each creature gets: **1 main action + 1 maneuver + 1 move action**.
- Can convert main action to maneuver or move action.
- **Triggered action**: 1 per round, any turn, requires trigger.
- **Free triggered action**: Same but doesn't count against 1/round limit.

### Movement
- **Advance**: Move up to speed.
- **Disengage**: Shift 1 square (no opportunity attacks).
- Diagonal = 1 square. Move through allies freely. Move through enemies = difficult terrain.
- **Difficult terrain**: +1 square cost to enter. Can't shift into/out of.
- **Shifting**: Does not provoke opportunity attacks.

### Movement Types
Walk, Burrow, Climb (2:1 without trait), Swim (2:1 without trait), Jump (Might/Agility score squares), Crawl (2:1 while prone), Fly (fall if prone/speed 0; Hover = don't fall), Teleport (instantaneous, bypasses obstacles, ends grabbed/restrained).

### Forced Movement
- **Push X**: Away from you in straight line.
- **Pull X**: Toward you in straight line.
- **Slide X**: Any horizontal direction.
- Ignores difficult terrain, never provokes opportunity attacks.
- Larger creature forcing smaller: +1 distance with melee ability.

### Slamming
- Into creature: Both take 1 damage per remaining square.
- Into solid object: Target takes 2 + 1 per remaining square.

### Falling
2+ squares: 2 damage per square fallen (max 50). Land prone. Reduce height by Agility score.

## Standard Maneuvers
- **Aid Attack**: Edge for next ally attack vs adjacent enemy.
- **Catch Breath**: Spend Recovery, regain Stamina = recovery value.
- **Escape Grab**: Power Roll + Might/Agility. T1: fail. T2: escape + free strike. T3: escape.
- **Grab**: Power Roll + Might. T1: fail. T2: grab + free strike. T3: grabbed.
- **Hide**: Attempt concealment from unobserving creatures.
- **Knockback**: Power Roll + Might. T1: push 1. T2: push 2. T3: push 3.
- **Stand Up**: End prone.
- **Use Consumable**: Activate consumable on self/adjacent ally.

## Standard Main Actions
- **Charge**: Move up to speed in straight line, then melee free strike.
- **Defend**: Double bane on ability rolls against you until next turn.
- **Free Strike**: Make a free strike.
- **Heal**: Target adjacent creature spends Recovery or saves against one effect.

## Free Strikes

**Melee Weapon**: Distance Melee 1, Power Roll + M/A: T1: 2+M/A, T2: 5+M/A, T3: 7+M/A.
**Ranged Weapon**: Distance Ranged 5, Power Roll + M/A: T1: 2+M/A, T2: 4+M/A, T3: 6+M/A.

### Opportunity Attacks
When adjacent enemy moves to non-adjacent without shifting/teleporting: melee free strike as free triggered action. Can't make if you have bane/double bane against target.

## Flanking
Two+ allies on opposite sides of enemy. Edge on melee strikes. Requires line of effect and ability to take triggered actions.

## Cover and Concealment
- **Cover**: Half blocked by solid object. Bane on damage-dealing abilities.
- **Concealment**: Fully obscured by non-solid effect. Bane on strikes.
- **Invisible**: Always have concealment.

## Stamina, Damage, Death

- **Recovery Value**: 1/3 Stamina maximum (round down).
- **Winded**: Stamina <= 1/2 maximum.
- **Dying**: Stamina <= 0. Auto-bleeding (can't remove until no longer dying).
- **Death**: Stamina reaches negative of winded value.
- **Director creatures**: Die at 0 Stamina (or KO, attacker's choice).
- **Temporary Stamina**: Decreases first, doesn't stack (take greater).

### Damage Types
Untyped, acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic.

### Immunity/Weakness
- **Immunity X**: Reduce incoming damage by X. Applied LAST. "immunity all" = ignore completely.
- **Weakness X**: Increase incoming damage by X. Applied BEFORE immunity.

## Saving Throws
Roll 1d10. On 6+, the (save ends) effect ends. Made at end of creature's turn.

## Conditions

| Condition | Effect |
|-----------|--------|
| **Bleeding** | When using main/triggered action or Might/Agility power roll: lose 1d6 + level Stamina |
| **Dazed** | One thing per turn: main, maneuver, or move. No triggered/free triggered/free maneuvers |
| **Frightened** | Bane vs source, source has edge vs you, can't move closer |
| **Grabbed** | Speed 0, can't be force moved (except by grabber), bane on non-grabber abilities |
| **Prone** | Bane on strikes, melee against you has edge, must crawl (2:1), can't climb/jump/swim/fly |
| **Restrained** | Speed 0, can't Stand Up, can't be force moved, bane on rolls + M/A tests, abilities vs you have edge. Teleport ends it |
| **Slowed** | Speed = 2 (if lower, no change), can't shift |
| **Taunted** | Double bane on rolls not targeting taunter |
| **Weakened** | Bane on power rolls |

## Size Categories
1T (Tiny), 1S (Small), 1M (Medium), 1L (Large), 2, 3, 4, 5+. Size = squares occupied per dimension.

## Areas of Effect
- **Aura X**: Radius X, moves with creator, persists.
- **Burst X**: Radius X, instantaneous.
- **Cube X**: X squares per side.
- **Line A x B**: A = length, B = width/height, straight.
- **Wall X**: X total squares, each shares side with another, blocks line of effect.

## Ability Keywords
Area, Charge, Magic, Melee, Psionic, Ranged, Strike, Weapon.
Ranged strikes while enemy adjacent: bane on power roll.

## Potency
Effect applies if target's characteristic < potency value.
- Weak: highest char - 2. Average: highest char - 1. Strong: highest char.

## Surges
- Spend up to 3 when dealing rolled damage: each surge = extra damage equal to highest characteristic (one target).
- Spend 2 to increase potency by 1 for one target (max +1 from surges).
- Lost at end of combat.

## Hero Tokens (Group Resource)
- 1 token: Gain 2 surges, OR succeed failed save, OR reroll a test.
- 2 tokens: Regain Stamina = recovery value. Limit: one benefit per turn/test.

---

# Monster Rules (from Draw Steel: Monsters)

## Monster Stat Block Fields
Level, Organization, Role, Keywords, EV (Encounter Value), Size, Speed, Stamina, Stability, Free Strike (static damage), Immunity, Weakness, Movement, Characteristics, Signature Ability, Traits, Additional abilities, Malice abilities, Villain Actions.

## Creature Free Strikes
Director creatures deal static Free Strike damage (no roll). Distance = melee 1 or signature melee distance (whichever higher). Ranged = 5 or signature ranged distance. Gains Strike keyword + signature's Magic/Psionic/Weapon keywords. Damage type matches signature.

## Organization

| Org | Description | EV Modifier |
|-----|-------------|-------------|
| Minion | Weak, squads of up to 8, shared stamina pool | x0.5 (for 4) |
| Horde | Hardier than minions, outnumber heroes ~2:1 | x0.5 |
| Platoon | Well-rounded, one per hero | x1 |
| Elite | Hardy, stands vs 2 heroes | x2 |
| Leader | Buffs allies, has villain actions, stands vs 2+ heroes | x2 |
| Solo | An encounter itself, stands vs 6 heroes | x6 |

## Roles

| Role | Stamina Mod | Damage Mod | Description |
|------|-------------|------------|-------------|
| Ambusher | +20 | +1 | Slips past front-liners, hide/invisible |
| Artillery | +10 | +1 | Strong ranged, weak melee |
| Brute | +30 | +1 | High Stamina, high damage, pushes |
| Controller | +10 | +0 | Repositions foes, alters terrain |
| Defender | +30 | +0 | Absorbs damage, forces attention |
| Harrier | +20 | +0 | Mobile hit-and-run |
| Hexer | +10 | +0 | Debuffs with conditions |
| Mount | +20 | +0 | Meant to be ridden |
| Support | +20 | +0 | Buffs, heals, grants movement/actions |

## Villain Actions
- Leaders and Solos have exactly 3, each usable once per encounter.
- Max one per round (even across multiple villains).
- Used at end of any other creature's turn.
- Numbered 1-3 (opener, crowd control, ultimate).

## Malice

**Earning:**
- Start of combat: Malice = average Victories per hero.
- Each round: gain Malice = living heroes + round number.

**Spending** (at start of any monster's turn, one per turn):
- **Brutal Effectiveness (3 Malice)**: +1 potency on next ability.
- **Malicious Strike (5+ Malice)**: Next strike deals extra damage = highest characteristic to one target. +1 per extra Malice (max 3x highest char). Can't use two rounds in a row.

## Minion Rules

**Squads**: Up to 8 minions of same name form a squad. One captain per squad.

**Shared Stamina Pool**: Pool = individual Stamina x count. When pool drops by one minion's worth, one dies. Area effects: only minions in area can die.

**Action Economy**: Each minion gets move + main action, OR move + maneuver. No triggered actions.

**Squad Action**: Multiple minions using signature ability = one roll. Each additional minion on same target adds free strike damage.

## Squad Captains
- Non-mount, non-minion creature speaking minions' language.
- Takes turn with squad but uses full action economy.
- Each minion gains "With Captain" benefits.
- Lost captain replaced at start of next round (no action).

## Encounter Building

**Encounter Strength**: Per hero = 4 + (2 x level). Party ES = sum.

**Difficulty:**
- Trivial: Budget < party ES - 1 hero's ES. 0 Victories.
- Easy: Budget < party ES. 1 Victory.
- Standard: Budget = party ES to party ES + 1 hero's ES. 1 Victory.
- Hard: Budget up to party ES + 3 heroes' ES. 2 Victories.
- Extreme: Budget > hard. 2+ Victories.

**Quick Method (Hero Slots)**: Slots = heroes + 1 per 2 avg Victories.
- 8 minions = 1 slot. 2 horde = 1 slot. 1 platoon = 1 slot. 1 elite/leader = 2 slots. 1 solo = 6 slots.

## Monster Level Scaling Formulas

**EV**: ((2 x Level) + 4) x Org Modifier

**Stamina**: ((10 x Level) + Role Modifier) x Org Modifier. Optional: + (3 x Level) + 3.

**Damage**: (4 + Level + Damage Modifier) x Tier Modifier. Horde/minion: /2. Strikes: + highest characteristic.
- Tier Modifiers: T1 = 0.6, T2 = 1.1, T3 = 1.4

**Characteristics**: Highest = 1 + echelon (echelon = ceil(level/3)). Leaders/Solos: +1 to highest (max +5), +1 to all potencies (max 6).

**Free Strike**: = Tier 1 ability damage. Standard: 1 target. Elite/Leader/Solo: 2 targets.

**Target scaling**: +1 target over expected: damage x 0.8. +2 or more: x 0.5. -1 target: x 1.2.

## Instant Solo Conversion (from Leader/Elite)
- EV x3, Stamina x2.5
- Solo Turns trait: Two turns per round, can't act consecutively.
- End Effect trait: End of each turn, take 10 damage (unreducible) to end one save-ends effect.
- Solo Action (5 Malice): Take additional main action (even if dazed).

## Negotiation

**NPC Stats**: Interest (0-5), Patience (0-5), Motivations (2+), Pitfalls (1+).

| Attitude | Interest | Patience |
|----------|----------|----------|
| Hostile | 1 | 2 |
| Suspicious | 2 | 2 |
| Neutral | 2 | 3 |
| Open | 3 | 3 |
| Friendly | 3 | 4 |
| Trusting | 3 | 5 |

**Appeal to Motivation** (medium test): T1: patience -1. T2: interest +1, patience -1. T3: interest +1.
**No Motivation** (harder): T1: patience -1, interest -1. T2: patience -1. T3: interest +1, patience -1.
**Pitfall**: Auto-fail, interest -1, patience -1.

Interest outcomes: 5 = "Yes, and...", 4 = "Yes.", 3 = "Yes, but...", 2 = "No, but...", 1 = "No.", 0 = "No, and..."
