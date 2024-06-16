#!/usr/bin/env python

import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = [Path(sys.argv[1])] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]


def collect(file_list: list):
    attrs = []
    tags = []
    subtags = []
    extra_attrs = []
    types = []
    stati = []

    for file in file_list:
        with open(file) as f:
            notes = list(json.load(f).values())
        
        for note in notes:
            attrs.extend(note.keys())
            tags.extend(note["tags"])
            subtags.extend(note["subtags"])
            extra_attrs.extend(note["extra"].keys())
            types.append(note["type"])
            stati.append(note["status"])

    return attrs, tags, subtags, extra_attrs, types, stati


def print_unique(strings: list[str]) -> None:
    strings.sort()
    unique = set(strings)
    counts = [f"{strings.count(s):>6} {s}" for s in unique]
    print("\n".join(sorted(counts, reverse=True)))


attrs, tags, subtags, extra_attrs, types, stati = collect(files)
print("======== ATTRS =========")
print_unique(attrs)
print("======== TAGS =========")
print_unique(tags)
print("======== SUBTAGS =========")
print_unique(subtags)
print("======== EXTRA =========")
print_unique(extra_attrs)
print("======== TYPES =========")
print_unique(types)
print("======== STATI =========")
print_unique(stati)
