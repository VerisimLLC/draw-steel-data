# Class Implementation Reference

How heroic resources, level progression, and class features are implemented in DMHub.

## Heroic Resource Implementation

### Class-Level Fields

```yaml
heroicResourceName: "Thirst"        # Display name
heroicResourceChecklist:             # UI display + trigger linkage
  - guid: <uuid>                     # Links to ReplenishBehavior.checklistid
    name: "Start of Combat"          # Short label
    details: "Description text"      # Tooltip
    quantity: "Victories"            # Amount (string, GoblinScript, or GoblinScriptTable)
    mode: encounter                  # Optional: "round" (1/round), "encounter" (1/encounter)
```

### Three Required Modifiers

Every heroic resource needs these three modifiers in a CharacterFeature:

**1. Resource Declaration:**
```yaml
- __typeName: CharacterModifier
  behavior: resource
  resourceType: "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"  # ALWAYS this UUID
  num: 0
  name: "Thirst"
  source: "Vampire Class Feature"
```

**2. Gain-at-Start Attribute** (die size for per-turn roll):
```yaml
- __typeName: CharacterModifier
  behavior: attribute
  attribute: "4d6eb7b5-85d1-41c0-a462-05cff692749a"  # "Heroic Resource Gain at Start"
  value: 3                                              # d3 = 3, d6 = 6, etc.
  name: "Thirst"
  source: "Vampire Class Feature"
```

**3. Trigger Modifiers** (one per gain event):

### Trigger Patterns

**Start of Combat** (gain = Victories):
```yaml
- __typeName: CharacterModifier
  behavior: trigger
  triggeredAbility:
    __typeName: TriggeredAbility
    trigger: rollinitiative
    mandatory: "game:heroicresourcetriggers"
    targetType: self
    conditionFormula: "Victories > 0"
    triggerPrompt: "Gain Thirst equal to Victories."
    behaviors:
      - __typeName: ActivatedAbilityReplenishBehavior
        checklistid: <matching-checklist-guid>
        chatMessage: "Draw Steel"
        resourceid: "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"
        quantity: "Victories"
        applyto: caster
```

**Start of Turn** (gain = 1dN, level-scaling):
```yaml
- __typeName: CharacterModifier
  behavior: trigger
  triggeredAbility:
    __typeName: TriggeredAbility
    trigger: beginturn
    whenActive: combat
    mandatory: "game:heroicresourcetriggers"
    targetType: self
    conditionFormula: "Heroic Resource Gain at Start > 0"
    behaviors:
      - __typeName: ActivatedAbilityReplenishBehavior
        checklistid: <matching-checklist-guid>
        chatMessage: "Start of Turn"
        resourceid: "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"
        quantity:
          __typeName: GoblinScriptTable
          editableField: true
          entries:
            - threshold: 1
              script: "1d Heroic Resource Gain at Start"
            - threshold: 7
              script: "(1d Heroic Resource Gain at Start) + 1"
          field: Level
          id: table
        applyto: caster
```

**Once-per-round conditional** (e.g., on damage/condition):
```yaml
- __typeName: CharacterModifier
  behavior: trigger
  resourceRefreshType: round           # MUST match usageLimitOptions
  resourceCostId: <own-modifier-guid>  # Points to self for charge tracking
  triggeredAbility:
    __typeName: TriggeredAbility
    trigger: dealdamage                # or inflictcondition, losehitpoints, etc.
    whenActive: combat
    mandatory: "game:heroicresourcetriggers"
    targetType: self
    conditionFormula: "Target.Winded or Target.Conditions has \"Bleeding\""
    usageLimitOptions:
      resourceid: <own-modifier-guid>
      charges: "1"
      resourceRefreshType: round
    behaviors:
      - __typeName: ActivatedAbilityReplenishBehavior
        checklistid: <matching-checklist-guid>
        quantity: "1"
        resourceid: "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"
        applyto: caster
```

**Condition Applied** (trigger: inflictcondition):
Available symbols: `Condition` (name string), `Attacker`, `Has Attacker`.
```yaml
trigger: inflictcondition
conditionFormula: 'Condition is Bleeding'
subject: any                         # Fires when ANY creature gets the condition
subjectRange: "10"                   # Within 10 squares
```

### Multi-Option Triggers (modeList)

When a trigger offers the player a **choice** of benefits rather than one fixed
effect (Tactician's Mark, "choose one of the following"), put the options in
`modeList` and gate each behavior with `modesSelected`. The trigger panel renders
one card per option and the player picks.

```yaml
- __typeName: CharacterModifier
  behavior: trigger
  triggeredAbility:
    __typeName: TriggeredAbility
    trigger: losehitpoints
    subject: enemy
    targetType: attacker
    conditionFormula: HasAbility and Ability.doesdamage
    triggerPrompt: Choose one Mark benefit.
    multipleModes: true
    modeList:
    - text: Additional Damage                    # mode 1 = the trigger's own card
      rules: The ability deals {2*Reason|double your Reason score in} additional damage.
      condition: ""
    - text: Spend Recovery
      rules: The damage dealer can spend a Recovery.
      condition: Attacker.Resources.Recovery > 0
      conditionReason: No recoveries remaining   # offered greyed out, not hidden
    - text: Shift
      rules: The damage dealer can shift up to {Reason|a number of squares equal to your Reason score}.
      condition: Attacker.Movement Speed > 0
      conditionReason: Speed is 0
    - text: Taunt
      rules: The marked creature is taunted by you (EoT).
      condition: Attacker.ID = Self.ID and Ability.Keywords has "Melee"
    behaviors:
    - __typeName: ActivatedAbilityDrawSteelCommandBehavior
      rule: Taunted (EoT)
      applyto: subject
      modesSelected: [4]                          # indexes into modeList
```

**Key points:**

- **`modeList[1]` is the trigger's own activate card**, not an option in the list.
  Its `text` and `rules` become the trigger's headline; only modes 2+ are
  condition-checked. A `condition` or `conditionReason` on mode 1 does nothing.
- **`modesSelected` indexes `modeList`, 1-based** -- the mode's authored position,
  not its position among the options the player actually sees. Hidden modes leave
  holes in the displayed list; the runtime carries the real index through, so you
  always write the `modeList` position here.
- **A failing `condition` hides the mode** unless you give it a
  `conditionReason`. With a reason set, the mode is offered anyway: dimmed,
  annotated with that text, but still pressable, so the player can see what they
  are missing and the table can allow it. Blank (the default) hides as before.
  Use a reason when the option is *temporarily* out of reach ("No recoveries
  remaining"); leave it blank when the option is simply irrelevant in context.
- **`rules` and `conditionReason` are both GoblinScript-interpolated** --
  `{Reason|a number of squares equal to your Reason score}` renders the computed
  number with that fallback text.
- Condition formulas here see the trigger's context symbols (`Attacker`, `Ability`,
  `Self`), which is how `Attacker.Resources.Recovery > 0` works above.

Fields are edited in the ability editor's **Modes** section; `conditionReason` is
the "Condition Reason" input under Mode Condition and tells a player *why* they cannot
use the ability.

### Key UUIDs

| UUID | Purpose |
|------|---------|
| `2d3d5511-4b80-46d1-a8c6-4705b9aa45ca` | Heroic Resource type (ALL classes) |
| `4d6eb7b5-85d1-41c0-a462-05cff692749a` | "Heroic Resource Gain at Start" attribute |
| `5bd90f9b-46be-4cf2-8ca6-a96430d62949` | Recovery resource type |

### GoblinScript Symbols

| Symbol | Type | Description |
|--------|------|-------------|
| `Heroic Resources Available to Spend` | Number | Current resource count |
| `Heroic Resources This Turn` | Number | High-water mark this turn |
| `Heroic Resource Gain at Start` | Number | Die size for per-turn roll |
| `Victories` | Number | Current victories |

### Growing Resources (Insatiable Thirst Pattern)

For benefit/drawback tables keyed to resource thresholds, use `behavior: growingresources`:
```yaml
- __typeName: CharacterModifier
  behavior: growingresources
  progression:
    - level: 0
      resources: 2
      description: "+Presence to speed and disengage."
      tooltip: "Full description..."
    - level: 0
      resources: 4
      description: "Gain 1 surge on damage to bleeding/winded/dying."
    - level: 4
      resources: 8
      description: "Might and Agility +1 for resisting potencies."
```
The `level` field gates by character level. `resources` is the threshold.
This drives the UI display. The actual mechanical effects need separate modifiers
with `filterCondition: "Heroic Resources This Turn >= 2"` etc.

## Variable Resource Spending (channeledResource)

For abilities where the player chooses how much heroic resource to spend:

```yaml
channeledResource: "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"  # Heroic resource UUID
channelIncrement: 1                    # Cost per charge (1 = spend 1 at a time)
channelDescription: "Spend Thirst for enhanced effects"
maxChannel: "Heroic Resources Available to Spend"  # Max spendable
```

Behaviors can reference `Charges` to scale effects:
```yaml
behaviors:
  - __typeName: ActivatedAbilityDamageBehavior
    roll: "Level + 2 + Charges * 2"    # Scales with Thirst spent
    cannotBeReduced: true               # Damage bypasses immunities
```

Conditional effects at thresholds:
```yaml
  - __typeName: ActivatedAbilityDrawSteelCommandBehavior
    filterTarget: "Charges + Target.ConditionCount >= 3"
    rule: "N8 weakened (save ends)"
```

## Unreducible Damage (cannotBeReduced)

Set `cannotBeReduced: true` on `ActivatedAbilityDamageBehavior` to bypass
numeric damage immunities. Used by Bleeding condition, Bloodbound, and Drink Most Exquisite.

```yaml
- __typeName: ActivatedAbilityDamageBehavior
  cannotBeReduced: true
  roll: "Level + 2"
  damageType: corruption
```

### Insatiable Thirst Benefits/Drawbacks Pattern

Each benefit/drawback is a separate CharacterModifier with filterCondition:
```yaml
# Thirst 2+ benefit: speed bonus
- __typeName: CharacterModifier
  behavior: attribute
  attribute: speed
  value: "Presence"
  filterCondition: "Heroic Resources This Turn >= 2"
  name: "Insatiable Thirst: Speed"
```

For the drawback suppression mechanic, create a custom ongoing effect
"Drawbacks Suppressed" and check `not (Ongoing Effects has "Drawbacks Suppressed")`
in each drawback modifier's filterCondition.
