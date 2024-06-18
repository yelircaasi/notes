#!/usr/bin/env python

import json
import sys

p = sys.argv[1]

with open(p) as f:
    notes = json.load(f)

cats = set()

for id_, note in notes.items():
    cats.add(note["extra"].get("category"))

print("\n".join(cats))
