"""Punisher Thunderclap must not be rated Gold (issue 27C4GXA3).

Rules text: "If this forced movement pushes the target away from the creature
they damaged, that creature takes half the triggering damage." No behavior
automates that clause (its implementationDetails says to adjudicate it
manually), so per the tier rubric (Gold = fully automated; a missing combat
mechanic is Bronze) the triggered ability, its companion copy and the
wrapping feature are Bronze (2).
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "subclasses", "punisher.yaml")

BRONZE = 2
EXPECTED = {
    "5f030001-0003-4096-bcde-7d8e9f0a1b2c": "Thunderclap feature",
    "5f030003-0003-4096-bcde-7d8e9f0a1b2c": "Thunderclap triggered ability",
    "5f03000d-0003-4096-bcde-7d8e9f0a1b2c": "Thunderclap (Companion) triggered ability",
}


def find_by_guid(node, out):
    if isinstance(node, dict):
        if node.get("guid") in EXPECTED:
            out.setdefault(node["guid"], []).append(node)
        for v in node.values():
            find_by_guid(v, out)
    elif isinstance(node, list):
        for v in node:
            find_by_guid(v, out)


with open(PATH, encoding="utf-8") as f:
    data = yaml.safe_load(f)

found = {}
find_by_guid(data, found)

checks = 0
for guid, label in EXPECTED.items():
    nodes = found.get(guid, [])
    assert len(nodes) == 1, "expected one %s (%s), found %d" % (label, guid, len(nodes))
    node = nodes[0]
    assert node.get("name") == "Thunderclap", "%s: unexpected name %r" % (label, node.get("name"))
    impl = node.get("implementation")
    assert impl == BRONZE, (
        "%s: implementation is %r, expected %d (Bronze); the half-damage-to-the-"
        "damaged-creature clause is not automated" % (label, impl, BRONZE))
    checks += 1

print("punisher_thunderclap_rating: %d checks passed" % checks)
