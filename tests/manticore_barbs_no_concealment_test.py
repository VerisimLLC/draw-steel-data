"""Manticore Barrage of Barbs aura must not grant concealment (issue CF79MKWH).

The ability text only makes the area difficult terrain, deals 3 poison damage
per square entered and applies bleeding; it says nothing about concealment.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "monstergroup", "manticore.yaml")

with open(PATH, encoding="utf-8") as f:
    group = yaml.safe_load(f)

checks = 0
abilities = []


def walk(node):
    if isinstance(node, dict):
        if node.get("name") == "Barrage of Barbs" and "behaviors" in node:
            abilities.append(node)
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


walk(group)
assert len(abilities) == 1, "expected one Barrage of Barbs ability, found %d" % len(abilities)
checks += 1

auras = [b["aura"] for b in abilities[0]["behaviors"] if b.get("__typeName") == "ActivatedAbilityAuraBehavior"]
assert len(auras) == 1, "expected one aura behavior, found %d" % len(auras)
checks += 1
aura = auras[0]

assert not aura.get("concealment", False), "Barrage of Barbs aura must not grant concealment"
checks += 1
assert aura.get("difficult_terrain") is True, "aura must still be difficult terrain"
checks += 1
assert aura.get("damage") == 3 and aura.get("movedamage") == "poison", "aura must still deal 3 poison damage per square"
checks += 1

print("manticore_barbs_no_concealment: %d checks passed" % checks)
sys.exit(0)
