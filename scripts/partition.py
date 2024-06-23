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

def make_name(basename: str) -> Path:
    return Path(f"/home/isaac/repos/notes/json-notes-alt/{basename}.json")

with open("/home/isaac/repos/notes/PARTITION.json") as f:
    partitions = json.load(f)
for part in partitions:
    part["tags"] = set(part["tags"])
    part["types"] = set(part["types"])

def find_file(note: dict) -> str:
    for part in partitions:
        if part["tags"].intersection(note["tags"]) == part["tags"]:
            if (not part["types"]) or (note["type"] in part["types"]) or (note["subtype"] in part["types"]):
                return part["filename"]
    return "miscellaneous"


full = {k["filename"]: {} for k in partitions}

for file in files:
    with open(file) as f:
        notes = json.load(f)
    for id_, note in notes.items():
        file_base = find_file(note)
        full[file_base].update({id_: note})


def format_notes(notes: list[dict]) -> str:
    s = json.dumps(notes, ensure_ascii=False)
    s = re.sub('("[^"]+": \{"text")', r"\n\1", s)
    return s   

for k in full:
    with open(make_name(k), "w") as f:
        f.write(format_notes(full[k]))

