#!/usr/bin/env python

import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = [sys.argv[1]] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]

KEYS = ["note", "id", "type", "tags", "subtags", "status", "dateCreated", "dateModified", "extra", "sorter"]
DEFAULT = {
    "note": "",
    "id": None,
    "type": "UNSPECIFIED",
    "tags": ["SORT"],
    "subtags": [],
    "status": "toRead",
    "dateCreated": "1970-01-01",
    "dateModified": "1970-01-01",
    "extra": {},
    "sorter": "UNSPECIFIED"
}
TYPES = [
    "",
    "UNSPECIFIED",
    "book",
    "readingMaterial",
    "readingAtom",
    "viewingAtom",
    "course",
    "dots",
    "periodical",
    "idea",
    "dotsSingleApp",
    "media-website",
    "person",
    "scripts",
    "videoSet",
    "reference",
    "thought",
    "ankiSet",
    "resourceList",
    "listeningAtom",
    "discussion",
]
STATI = [
    "toRead",
    "selected",
    ""
    "needsWork",
    "selectedForLater",
    "backPocket",
    "alreadyInUse"
    "useAsReference",
    "selectedNeedsNix",
    "needToTry"
]

def remove_duplicates_keep_order(tags: list[str]) -> list[str]:
    already = set()
    cleaned = []
    for tag in tags:
        if not tag in already:
            already.add(tag)
            cleaned.append(tag)
    return cleaned


def lint_tags(tags: list[str]) -> list[str]:
    tags = list(filter(bool, tags))
    if len(tags) != len(set(tags)):
        # print("DUPLICATE TAGS:", tags)
        tags = remove_duplicates_keep_order(tags)
    
    return tags
    
def make_id() -> str:
    random16 = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"AUTO:{random16}"


def lint_note(note: dict) -> dict:
    note = DEFAULT | note
    if note["id"] is None:
        note["id"] = make_id()
    note["tags"] = lint_tags(note["tags"])
    note["subtags"] = lint_tags(note["subtags"])
    extra = {k: v for k, v in note.items() if k not in KEYS}
    note = {k: v for k, v in note.items() if k in KEYS}
    # print(note)
    note["extra"].update(extra)

    return note


def format_notes(notes: list[dict]) -> str:
    s = json.dumps(notes, ensure_ascii=False).replace("}, {", "},\n{")
    return s
    



for p in files:
    print(p)
    with open(p) as f:
        notes = json.load(f)

    notes = list(map(lint_note, notes))
    note_string = format_notes(notes)

    with open(p, "w") as f:
        f.write(note_string)





