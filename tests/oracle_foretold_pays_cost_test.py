"""Oracle It Was Foretold must not waive the routed ability's heroic resource cost
(issue MAQZWSYN).

The feature reads "you can take one main action before any other creature and before
your first turn" -- it grants the action, not a free heroic ability. Its invoked
ability routes the chosen main action through an augmented-ability modifier; unless
that modifier sets mustPayResourceCost, DSAugmentAbilities.lua replaces the routed
ability's cost with the (empty) cost of the invoker, so heroic abilities cost nothing.
"""
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATHS = [
    os.path.join(ROOT, "objectTables", "classes", "oracle.yaml"),
    os.path.join(ROOT, "objectTables", "subclasses", "oracle.yaml"),
]

MODIFIER_GUID = "9829176c-b253-4087-b6bf-9ce94e84c7b8"


def find_guid(node, guid, out):
    if isinstance(node, dict):
        if node.get("guid") == guid:
            out.append(node)
        for v in node.values():
            find_guid(v, guid, out)
    elif isinstance(node, list):
        for v in node:
            find_guid(v, guid, out)


checks = 0
for path in PATHS:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    found = []
    find_guid(data, MODIFIER_GUID, found)
    assert len(found) == 1, "%s: expected one It Was Foretold modifier, found %d" % (path, len(found))
    mod = found[0]
    assert mod.get("behavior") == "modifyability", "%s: unexpected behavior %r" % (path, mod.get("behavior"))
    checks += 1
    assert mod.get("mustPayResourceCost") is True, (
        "%s: It Was Foretold's routed main action must pay its own heroic resource cost "
        "(mustPayResourceCost is %r)" % (path, mod.get("mustPayResourceCost")))
    checks += 1

print("oracle_foretold_pays_cost: %d checks passed" % checks)
