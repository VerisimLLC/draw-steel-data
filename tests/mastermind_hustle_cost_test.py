"""Mastermind level-5 ability Hustle! must cost 9 Focus (issue ZGCDK522).

The book lists "Hustle! (9 Focus)", the same cost as its sibling Battle Plan.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "subclasses", "mastermind.yaml")

FOCUS = "2d3d5511-4b80-46d1-a8c6-4705b9aa45ca"
HUSTLE_GUID = "8b4ec381-6d97-4fd9-a112-0d7179467d01"


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
hustle = [a for a in abilities if a.get("guid") == HUSTLE_GUID]
assert len(hustle) == 1, "expected exactly one Hustle! ability, found %d" % len(hustle)
hustle = hustle[0]
assert hustle["name"] == "Hustle!", "unexpected name %r" % hustle["name"]
checks += 1
assert hustle.get("resourceCost") == FOCUS, "Hustle! resourceCost should be Focus (%s), got %r" % (FOCUS, hustle.get("resourceCost"))
checks += 1
assert str(hustle.get("resourceNumber")) == "9", "Hustle! resourceNumber should be 9, got %r" % hustle.get("resourceNumber")
checks += 1

print("mastermind_hustle_cost: %d checks passed" % checks)
sys.exit(0)
