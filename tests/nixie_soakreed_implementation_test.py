"""Circle of Spring's Nixie Soakreed option must not claim more automation
than the Nixie Soakreed monster has (issue VW9QB7N6).

The Summoner builder badge for a Signature Minion option is read from the
option's own `implementation`. The monster's Soaking Bog trait is rated 2
(Bronze), so the option must not be rated above the monster's lowest trait.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBCLASS = os.path.join(ROOT, "objectTables", "subclasses", "circle-of-spring.yaml")
MONSTER = os.path.join(ROOT, "monsters", "nixie-soakreed.yaml")
OPTION_GUID = "de9d3d57-2363-4462-97ce-2df415e64ca5"


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


with open(SUBCLASS, encoding="utf-8") as f:
    subclass = yaml.safe_load(f)
with open(MONSTER, encoding="utf-8") as f:
    monster = yaml.safe_load(f)

checks = 0

options = [n for n in walk(subclass) if n.get("guid") == OPTION_GUID]
assert len(options) == 1, "expected one Nixie Soakreed option, found %d" % len(options)
option = options[0]
assert option.get("name") == "Nixie Soakreed", "option guid must name Nixie Soakreed, got %r" % option.get("name")
checks += 1

traits = {n["name"]: n["implementation"] for n in walk(monster)
          if n.get("__typeName") == "CharacterFeature" and "implementation" in n}
assert traits.get("Soaking Bog") == 2, "expected Soaking Bog rated 2 (Bronze), got %r" % traits.get("Soaking Bog")
checks += 1

lowest = min(traits.values())
assert option.get("implementation") <= lowest, (
    "Nixie Soakreed option claims implementation %r, above the monster's lowest trait rating %r (%s)"
    % (option.get("implementation"), lowest, traits))
checks += 1

print("nixie_soakreed_implementation: %d checks passed" % checks)
sys.exit(0)
