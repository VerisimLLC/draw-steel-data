"""Prowler's 2nd-level Wild Nature feature must be named Supersniffer (issue 7SKNW5EN).

Like Guardian (Watchdog), Punisher (This One's Yours) and Spark (Stormheart),
the feature and its modifier carry the feature's real name, not a placeholder.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "subclasses", "prowler.yaml")

with open(PATH, encoding="utf-8") as f:
    doc = yaml.safe_load(f)

GUID = "ef9f4f71-b510-4848-b3f0-c7cff47c84bb"


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
assert feature is not None, "Wild Nature feature %s not found" % GUID
checks += 1
assert feature["name"] == "Supersniffer", "expected feature name 'Supersniffer', got %r" % feature["name"]
checks += 1
mod = feature["modifiers"][0]
assert mod["behavior"] == "modcompanion", "expected the modcompanion modifier"
checks += 1
assert mod["name"] == "Supersniffer", "expected modifier name 'Supersniffer', got %r" % mod["name"]
checks += 1
assert mod["feature"]["name"] == "Supersniffer", "companion feature name must stay 'Supersniffer'"
checks += 1

print("prowler_supersniffer_name: %d checks passed" % checks)
sys.exit(0)
