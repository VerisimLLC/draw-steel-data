"""Beastheart companion Gummy Ball must be size 1L (issue KKGWSCGV).

The Beastheart rules list the Gummy Ball as Size 1L. Without a creatureSize
property the creature falls back to the default size 1M.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "monsters", "5e2f1d83-4b6c-4a76-b528-1c3d8e7f5a92.yaml")

with open(PATH, encoding="utf-8") as f:
    mon = yaml.safe_load(f)

checks = 0
props = mon["info"]["properties"]
assert props["monster_type"] == "Gummy Ball", "expected the Gummy Ball, got %r" % props["monster_type"]
checks += 1
size = props.get("creatureSize")
assert size == "1L", "expected creatureSize '1L' (rulebook), got %r (missing means default 1M)" % size
checks += 1

print("gummy_ball_size: %d checks passed" % checks)
sys.exit(0)
