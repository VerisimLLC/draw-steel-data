"""Gear item 'An ounce of ferrous metal' must be spelled correctly (issue X3YR26GG).

The Telemagnet's item prerequisite names it 'an ounce of ferrous metal'.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "objectTables", "tbl-gear", "an-ounce-of-ferrous-metai.yaml")

with open(PATH, encoding="utf-8") as f:
    item = yaml.safe_load(f)

checks = 0
assert item["id"] == "5e7e3d46-2c97-4c46-8850-4e632f7908b1", "item id must not change"
checks += 1
assert item["name"] == "An ounce of ferrous metal", "expected name 'An ounce of ferrous metal', got %r" % item["name"]
checks += 1

print("ferrous_metal_name: %d checks passed" % checks)
sys.exit(0)
