# Compendium Content Technical Reference

This reference has been split into focused files for easier navigation.

## Reference Files

| File | Contents |
|------|----------|
| [reference/CORE.md](reference/CORE.md) | Common pitfalls, table names, GoblinScript booleans, UUID reference maps (action resources, conditions, ongoing effects, damage types, characteristics, keywords, custom attributes, standard abilities), file format/placement, ASCII-only rule |
| [reference/MONSTERS.md](reference/MONSTERS.md) | Monster YAML structure, ActivatedAbility fields, targeting system, all behavior types, power roll tiers, rules engine commands, aura system, CharacterModifier behaviors, TriggeredAbility fields/triggers, ongoing effects, multi-mode abilities, global rules index, example YAML patterns |
| [reference/CONDITIONS.md](reference/CONDITIONS.md) | Condition/ongoing-effect/rider/bestow system conceptual model, CharacterCondition YAML field reference, duration mechanics (inflicted vs ongoing effect vs bestowed), save ends mechanic, CharacterOngoingEffect with underlying condition, bestowcondition modifier, ConditionRider type, modifier behaviors, 5 condition templates, pitfalls |
| [reference/CHARACTERS.md](reference/CHARACTERS.md) | Class structure (levels, features, characteristic arrays, heroic resource), subclass structure, ancestry/race structure (modifierInfo, point-buy), kit structure (stat bonuses, damage tiers, signature ability, equipment, kit types), complication structure (benefit/drawback), title structure (echelon), treasure/equipment structure (categories, consumables, magical items), feature types reference, comparison table |

## Other References

| File | Contents |
|------|----------|
| [RULES_REFERENCE.md](RULES_REFERENCE.md) | Game rules |
| [../GoblinScript_Guide.md](../GoblinScript_Guide.md) | GoblinScript formula syntax |

## Quick Lookup

- **UUID for a condition, damage type, or resource?** -> [CORE.md](reference/CORE.md) UUID Reference Maps
- **How to structure a monster YAML?** -> [MONSTERS.md](reference/MONSTERS.md) Monster YAML Structure
- **What behavior types exist?** -> [MONSTERS.md](reference/MONSTERS.md) Behavior Types
- **How to build a class or kit?** -> [CHARACTERS.md](reference/CHARACTERS.md)
- **How do conditions, ongoing effects, and riders work?** -> [CONDITIONS.md](reference/CONDITIONS.md)
- **What are the valid table names?** -> [CORE.md](reference/CORE.md) Table Names
- **Power roll tier syntax?** -> [MONSTERS.md](reference/MONSTERS.md) Power Table Effect / Rules Engine Commands
