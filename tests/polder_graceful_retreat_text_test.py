"""Polder Graceful Retreat must call Disengage a move action (issue KZNSJUZD).

Disengage is a move action; the High Elf feature with the same wording
(elf-high.yaml) and the printed rules say 'the Disengage move action'.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "races", "polder.yaml")
FEATURE_GUID = "22e632c0-d0f0-47a9-b776-2ff3ac7e17b2"
EXPECTED = ("When you take the Disengage move action, you can shift 1 additional "
            "square as part of the move action.")


def find(node):
    if isinstance(node, dict):
        if node.get("guid") == FEATURE_GUID and node.get("__typeName") == "CharacterFeature":
            return node
        for v in node.values():
            r = find(v)
            if r is not None:
                return r
    elif isinstance(node, list):
        for v in node:
            r = find(v)
            if r is not None:
                return r
    return None


with open(PATH, encoding="utf-8") as f:
    race = yaml.safe_load(f)

checks = 0
feature = find(race)
assert feature is not None, "Graceful Retreat feature %s not found" % FEATURE_GUID
assert feature["name"] == "Graceful Retreat", "unexpected feature name %r" % feature["name"]
checks += 1
assert feature["description"] == EXPECTED, \
    "feature description should say 'Disengage move action', got %r" % feature["description"]
checks += 1
mods = feature.get("modifiers") or []
assert len(mods) == 1, "expected one modifier, got %d" % len(mods)
checks += 1
assert mods[0]["description"] == EXPECTED, \
    "modifier description should say 'Disengage move action', got %r" % mods[0]["description"]
checks += 1
assert mods[0]["value"] == 1, "the extra shift must stay 1, got %r" % mods[0]["value"]
checks += 1

print("polder_graceful_retreat_text: %d checks passed" % checks)
sys.exit(0)
