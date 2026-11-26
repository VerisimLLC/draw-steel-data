"""Circle of Graves Rise! must summon even at the minion maximum (issue AYEJ9DRT).

Rules text: "summon a signature undead minion in their space at no cost even
if you're at your minion maximum, but only if they can be organized into one
of your squads." Both triggered abilities (Rise! for a minion target, Rise!
Non-Minion otherwise) must set ignoreSummonerLimits on their summon behavior,
as Explosive Parade in summoner.yaml does. The 8-minion squad cap is enforced
by the squad chooser independently of this flag.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "subclasses", "circle-of-graves.yaml")

with open(PATH, encoding="utf-8") as f:
    doc = yaml.safe_load(f)

GUIDS = {
    "a870b648-3b17-4c2d-8973-00e3161680ae": "Rise! Non-Minion",
    "30f25188-7a55-41ac-8f7a-05538c0918c7": "Rise!",
}

found = {}


def walk(node):
    if isinstance(node, dict):
        if node.get("__typeName") == "TriggeredAbility" and node.get("guid") in GUIDS:
            found[node["guid"]] = node
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


walk(doc)

checks = 0
for guid, name in GUIDS.items():
    assert guid in found, "triggered ability %s (%s) not found" % (name, guid)
    ability = found[guid]
    assert ability["name"] == name, "expected name %r, got %r" % (name, ability["name"])
    checks += 1
    summons = [b for b in ability["behaviors"] if b.get("__typeName") == "ActivatedAbilitySummonBehavior"]
    assert len(summons) == 1, "%s: expected one summon behavior, got %d" % (name, len(summons))
    checks += 1
    assert summons[0].get("ignoreSummonerLimits") is True, \
        "%s: summon behavior must set ignoreSummonerLimits: true (works even at minion maximum)" % name
    checks += 1

print("circle_of_graves_rise_minion_limit: %d checks passed" % checks)
sys.exit(0)
