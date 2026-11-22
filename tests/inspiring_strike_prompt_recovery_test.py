"""Inspiring Strike tier 3 must let each hero choose to spend a Recovery (issue HDM2EVKS).

The Tactician's Inspiring Strike reads, at tier 3: "you and one ally within 10
squares can spend a Recovery". "Can" makes it optional, so both invocations must
use "Prompt Spend Recovery" (always asks the controller), not "May Spend
Recovery", which spends silently when the creature is on the caster's computer.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "classes", "tactician.yaml")

PROMPT_SPEND_RECOVERY = "3b05eb22-02fd-4654-85e9-d71104172166"
MAY_SPEND_RECOVERY = "f57cb6f7-13b9-4ebb-8e88-88ead0a9c203"
TIER3_INVOKED_GUID = "96292480-560a-4325-9a1c-23edcf46ed36"


def find(node, pred, out):
    if isinstance(node, dict):
        if pred(node):
            out.append(node)
        for v in node.values():
            find(v, pred, out)
    elif isinstance(node, list):
        for v in node:
            find(v, pred, out)


with open(PATH, encoding="utf-8") as f:
    data = yaml.safe_load(f)

checks = 0
strikes = []
find(data, lambda n: n.get("__typeName") == "ActivatedAbility" and n.get("name") == "Inspiring Strike", strikes)
assert len(strikes) == 1, "expected exactly one Inspiring Strike ability, found %d" % len(strikes)
checks += 1

tier3 = []
find(strikes[0], lambda n: n.get("__typeName") == "ActivatedAbility" and n.get("guid") == TIER3_INVOKED_GUID, tier3)
assert len(tier3) == 1, "expected the tier 3 invoked ability, found %d" % len(tier3)
tier3 = tier3[0]

invokes = [b for b in tier3["behaviors"] if b.get("__typeName") == "ActivatedAbilityInvokeAbilityBehavior"]
targets = sorted(b.get("applyto") for b in invokes)
assert targets == ["caster", "targets"], "expected recovery invocations for caster and targets, got %r" % targets
checks += 1

for b in invokes:
    sa = b.get("standardAbility")
    assert sa != MAY_SPEND_RECOVERY, (
        "tier 3 (%s) uses May Spend Recovery, which spends the Recovery without asking" % b.get("applyto"))
    assert sa == PROMPT_SPEND_RECOVERY, (
        "tier 3 (%s) should use Prompt Spend Recovery, got %r" % (b.get("applyto"), sa))
    assert str(b.get("standardAbilityParams", {}).get("numrecoveries")) == "1", "numrecoveries should stay 1"
    checks += 1

print("inspiring_strike_prompt_recovery: %d checks passed" % checks)
sys.exit(0)
