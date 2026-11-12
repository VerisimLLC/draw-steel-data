"""Hobgoblin Firerunner must have only its own abilities (issue 47G7KDEE).

The stat block gives it Flaming Kick (signature) and Blazing Trail (maneuver).
Fire Crossbow and Fire Ball Volley belong to the Hobgoblin Incendiarist.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "monsters", "hobgoblin-firerunner.yaml")

with open(PATH, encoding="utf-8") as f:
    monster = yaml.safe_load(f)

props = monster["info"]["properties"]
checks = 0
assert props["monster_type"] == "Hobgoblin Firerunner", "unexpected monster %r" % props["monster_type"]
checks += 1

names = [a["name"] for a in props["innateActivatedAbilities"]]
for wrong in ("Fire Crossbow", "Fire Ball Volley"):
    assert wrong not in names, "Firerunner must not have the Incendiarist's %r; abilities are %r" % (wrong, names)
    checks += 1
assert names == ["Flaming Kick", "Blazing Trail"], "expected ['Flaming Kick', 'Blazing Trail'], got %r" % names
checks += 1

print("firerunner_abilities: %d checks passed" % checks)
sys.exit(0)
