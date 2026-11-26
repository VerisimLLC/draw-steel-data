"""War Dog Teletalite must have Teleport movement (issue 8BA6Z54K).

The printed stat block reads Speed 5 (teleport). Like other "Speed N (teleport)"
monsters (Hobgoblin Redglare, Demon Remasch), the teleport speed is stored as
movementSpeeds.teleport = N alongside walkingSpeed.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "monsters", "war-dog-teletalite.yaml")

with open(PATH, encoding="utf-8") as f:
    doc = yaml.safe_load(f)

checks = 0
props = doc["info"]["properties"]
assert props["monster_type"] == "War Dog Teletalite", "wrong monster file"
checks += 1
assert props["walkingSpeed"] == 5, "expected Speed 5, got %r" % props["walkingSpeed"]
checks += 1
speeds = props["movementSpeeds"]
assert isinstance(speeds, dict) and "teleport" in speeds, \
    "expected a teleport movement type, got movementSpeeds=%r" % (speeds,)
checks += 1
assert speeds["teleport"] == 5, "expected teleport 5, got %r" % speeds["teleport"]
checks += 1

print("war_dog_teletalite_teleport: %d checks passed" % checks)
sys.exit(0)
