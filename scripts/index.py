#!/usr/bin/env python

import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = (
    [Path(sys.argv[1])]
    if sys.argv[1:]
    else [directory / f for f in os.listdir(directory)]
)


def extend_safe(d: dict, k: string, l: list) -> None:
    if not k in d:
        d.update({k: []})
    d[k].extend(l)


def count_unique(strings: list[str]) -> None:
    strings.sort()
    unique = set(strings)
    return {s: strings.count(s) for s in unique}


def collect(file: Path):
    tags = []
    subtags = []
    extra_attrs = []
    types = []
    stati = []

    with open(file) as f:
        notes = list(json.load(f).values())

    for note in notes:
        tags.extend(note["tags"])
        subtags.extend(note["subtags"])
        extra_attrs.extend(note["extra"].keys())
        types.append(note["type"])
        stati.append(note["status"])

    return {
        "tags": count_unique(tags),
        "subtags": count_unique(subtags),
        "extra_attrs": count_unique(extra_attrs),
        "types": count_unique(types),
        "stati": count_unique(stati),
    }


summary = {}
for file in files:
    summary.update({str(file.name).replace(".json", ""): collect(file)})

lookup = {}
for filename, filesummary in summary.items():
    for attr, attrsummary in filesummary.items():
        for value, count in attrsummary.items():
            if not attr in lookup:
                lookup.update({attr: {}})
            if not value in lookup[attr]:
                lookup[attr].update({value: {}})
            lookup[attr][value].update({filename: count})

with open("/home/isaac/repos/notes/SUMMARY.json", "w") as f:
    json.dump(summary, f, indent=4, ensure_ascii=False)
with open("/home/isaac/repos/notes/LOOKUP.json", "w") as f:
    json.dump(lookup, f, indent=4, ensure_ascii=False)

