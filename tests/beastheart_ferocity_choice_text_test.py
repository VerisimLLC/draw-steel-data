"""Beastheart level-3 '7-Ferocity Ability' choice prompt must read 'Choose an ability' (issue BMT7BE8U)."""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "classes", "beastheart.yaml")
GUID = "f00bcc5f-4566-41a2-9e79-ee57e12e811e"

with open(PATH, encoding="utf-8") as f:
    doc = yaml.safe_load(f)


def find(node):
    if isinstance(node, dict):
        if node.get("guid") == GUID:
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


checks = 0
feature = find(doc)
assert feature is not None, "feature %s not found" % GUID
checks += 1
assert feature["name"] == "7-Ferocity Ability", "unexpected feature name %r" % feature["name"]
checks += 1
assert feature["description"] == "Choose an ability", "expected 'Choose an ability', got %r" % feature["description"]
checks += 1

print("beastheart_ferocity_choice_text: %d checks passed" % checks)
sys.exit(0)
