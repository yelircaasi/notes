import json
import re
import sys
from pathlib import Path
import os


directory = Path("json-notes")
files = [directory / f for f in os.listdir(directory)]


def format_notes(notes: list[dict]) -> str:
    s = json.dumps(notes, ensure_ascii=False).replace("}, {", "},\n{")
    return s


for file in files:
    sorter = str(file).split("/")[-1].replace(".json", "")
    print(sorter)

    with open(file) as f:
        notes = json.load(f)

    for i, note in enumerate(notes):
        note["sorter"] = f"{sorter}{i}"

    note_string = format_notes(notes)

    with open(file, "w") as f:
        f.write(note_string)

