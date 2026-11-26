"""Blessing of Fate and Destiny's second mode label must say roll 3 (issue AJ437WEU).

The ability's rules text (and the mode's own rules line) say the target must
roll three dice and use the lowest two, so the button must read
'Roll 3 and Take Lowest 2', not 'Roll 2 and Take Lowest 2'.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "classes", "conduit.yaml")
ABILITY_GUID = "3c7f72e3-4067-4ab8-8c0c-7b3862ee1bb4"


def find(node):
    if isinstance(node, dict):
        if node.get("guid") == ABILITY_GUID and node.get("__typeName") == "ActivatedAbility":
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
    data = yaml.safe_load(f)

checks = 0
ability = find(data)
assert ability is not None, "Blessing of Fate and Destiny ability %s not found" % ABILITY_GUID
assert ability["name"] == "Blessing of Fate and Destiny", "unexpected name %r" % ability["name"]
checks += 1
modes = ability.get("modeList") or []
assert len(modes) == 2, "expected two modes, got %d" % len(modes)
checks += 1
assert modes[0]["text"] == "Roll 3 and Choose", "first mode label changed: %r" % modes[0]["text"]
checks += 1
assert "roll three dice and use the lowest two" in modes[1]["rules"], \
    "second mode rules should describe rolling three, got %r" % modes[1]["rules"]
checks += 1
assert modes[1]["text"] == "Roll 3 and Take Lowest 2", \
    "second mode label should be 'Roll 3 and Take Lowest 2', got %r" % modes[1]["text"]
checks += 1

print("conduit_fate_destiny_mode_label: %d checks passed" % checks)
sys.exit(0)
