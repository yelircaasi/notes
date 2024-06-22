import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = (
    [sys.argv[1]] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]
)

with open("/home/isaac/repos/notes/categories.json") as f:
    cats = json.load(f)


def lint_note(note: dict) -> dict:
    
    if not "category" in note["extra"]:
        return note 
    
    cat_string = note["extra"]["category"]
    cat = cats[cat_string]

    note["tags"].extend(cat["tags"])
    note["subtags"].extend(cat["subtags"])
    note["type"] = cat["type"]
    if cat.get("subtype"):
        note["subtype"] = cat["subtype"]
    del note["extra"]["category"]

    return note

def format_notes(notes: list[dict]) -> str:
    s = json.dumps(notes, ensure_ascii=False)
    s = re.sub('("[^"]+": \{"text")', r"\n\1", s)
    return s

for p in files:
    print(p)
    with open(p) as f:
        notes = json.load(f)

    notes = {k: lint_note(v) for k, v in notes.items()}
    # notes = {k: v | {"id": k} for k, v in notes.items()}
    note_string = format_notes(notes)
    # print(note_string[:1000])

    with open(p, "w") as f:
        f.write(note_string)