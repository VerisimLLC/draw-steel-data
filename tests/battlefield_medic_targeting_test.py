"""Support retainer's Battlefield Medic must target self or one ally (issue CF77AQ9Q).

The book lists it as "Melee 1 | Self or one ally". It was authored with
targetType "selforally", which is not an ability target type, so no target
could be chosen. Self-or-ally abilities elsewhere use targetType "target",
targetAllegiance "ally" and selfTarget true.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "creaturetemplates", "support-abilities.yaml")

MEDIC_GUID = "b5f92af9-284d-4f1f-8fc0-e9516c68a2ac"
VALID_TARGET_TYPES = {"target", "self", "all", "line", "cone", "cube", "sphere",
                      "cylinder", "emptyspace", "anyspace"}


def find_abilities(node, out):
    if isinstance(node, dict):
        if node.get("__typeName") == "ActivatedAbility":
            out.append(node)
        for v in node.values():
            find_abilities(v, out)
    elif isinstance(node, list):
        for v in node:
            find_abilities(v, out)


with open(PATH, encoding="utf-8") as f:
    data = yaml.safe_load(f)

abilities = []
find_abilities(data, abilities)

checks = 0
medic = [a for a in abilities if a.get("guid") == MEDIC_GUID]
assert len(medic) == 1, "expected exactly one Battlefield Medic ability, found %d" % len(medic)
medic = medic[0]
assert medic["name"] == "Battlefield Medic", "unexpected name %r" % medic["name"]
checks += 1
assert medic.get("targetType") in VALID_TARGET_TYPES, \
    "Battlefield Medic targetType %r is not a valid ability target type" % medic.get("targetType")
checks += 1
assert medic.get("targetType") == "target", "Battlefield Medic targetType should be 'target', got %r" % medic.get("targetType")
checks += 1
assert medic.get("targetAllegiance") == "ally", "Battlefield Medic should target allies, got targetAllegiance %r" % medic.get("targetAllegiance")
checks += 1
assert medic.get("selfTarget") is True, "Battlefield Medic should be able to target self (selfTarget), got %r" % medic.get("selfTarget")
checks += 1
assert medic.get("range") == 1 and str(medic.get("numTargets")) == "1", \
    "Battlefield Medic should stay Melee 1, one target; got range %r numTargets %r" % (medic.get("range"), medic.get("numTargets"))
checks += 1

print("battlefield_medic_targeting: %d checks passed" % checks)
sys.exit(0)
