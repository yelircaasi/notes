#!/usr/bin/env python

import sys
import re
import json
from typing import Callable

from convert_to_note import Colorizer, convert

width = 100
double_bar = width * "═"
single_bar = width * "─"


def split_notes(s: str) -> list[str]:
    return tuple(map(str.strip("\n "), s.split(double_bar)[1:]))


def split_lines(s: str) -> tuple[str]:
    # print(s)
    lines = tuple(s.strip("═").split(single_bar)[:-1])
    return lines
    

def parse_dense_line(s: str) -> tuple[str]:
    id_, type_pair, status, all_tags = re.split(" +", s)[:4]
    # print(id_, type_pair, status, all_tags)
    type_, subtype = type_pair.split("::")[:2]
    tags, subtags = map(lambda x: x.split("-"), all_tags.strip().split("::")[:2])

    return (id_, type_, subtype, status, tags, subtags)


def parse_extra(s: str) -> tuple[str]:
    s = s.strip()
    if not s:
        return {}
    # print(list(map(lambda x: re.split(": *", x, 1), s.strip().split("\n"))))
    return dict(list(map(lambda x: re.split(": *", x, 1), s.split("\n"))))


def parse_date_line(s: str) -> tuple[str]:
    return re.split(" +", s)[:3]

def parse_note(s: str) -> dict:
    # print(s)
    # print(split_lines(s))
    dense_line, text, link, extra_string, date_line = split_lines(s)
    id_, type_, subtype, status, tags, subtags = parse_dense_line(dense_line)
    text = text
    extra = parse_extra(extra_string)
    date_created, date_modified, sorter = parse_date_line(date_line)

    return {
        "text": text.strip(),
        "link": link.strip(),
        "type": type_.strip(),
        "subtype": subtype.strip(),
        "tags": tags,
        "subtags": subtags,
        "status": status.strip(),
        "dateCreated": date_created.strip(),
        "dateModified": date_modified.strip(),
        "extra": extra,
        "sorter": sorter.strip(),
        "id": id_.strip(),
    }


def parse_notes(s: str) -> dict[str, dict]:
    return {note["id"]: note for note in map(parse_note, s.split(double_bar)[1:])}


test_str = '''
════════════════════════════════════════════════════════════════════════════════════════════════════
AUTO:Z1NUUY5S17E1J9T6  viewingAtom::vlog  toRead  humanities-SORT::italy-torino
────────────────────────────────────────────────────────────────────────────────────────────────────

Cosa vedere a Torino

────────────────────────────────────────────────────────────────────────────────────────────────────
https://www.youtube.com/watch?v=fngBTrfW5_g
────────────────────────────────────────────────────────────────────────────────────────────────────
language: IT
class: excellent
────────────────────────────────────────────────────────────────────────────────────────────────────
1970-01-01                      2024-06-17                              humanities7
────────────────────────────────────────────────────────────────────────────────────────────────────

════════════════════════════════════════════════════════════════════════════════════════════════════
AUTO:F8DI6CB1S5GI1BE1  ::  toRead  humanities-SORT::
────────────────────────────────────────────────────────────────────────────────────────────────────

Torino Città meravigiosa

────────────────────────────────────────────────────────────────────────────────────────────────────
https://www.youtube.com/watch?v=tNPNo-GZKFs
────────────────────────────────────────────────────────────────────────────────────────────────────
language: 
────────────────────────────────────────────────────────────────────────────────────────────────────
1970-01-01                      1970-01-01                              humanities8
────────────────────────────────────────────────────────────────────────────────────────────────────

════════════════════════════════════════════════════════════════════════════════════════════════════
AUTO:19DFU1G4YLI3G3AJ  ::  toRead  humanities-SORT::
────────────────────────────────────────────────────────────────────────────────────────────────────

tribina.hr

────────────────────────────────────────────────────────────────────────────────────────────────────
https://www.tribina.hr/
────────────────────────────────────────────────────────────────────────────────────────────────────
language: 
────────────────────────────────────────────────────────────────────────────────────────────────────
1970-01-01                      1970-01-01                              humanities9
────────────────────────────────────────────────────────────────────────────────────────────────────
'''

print(test_str)
print(single_bar)
print(double_bar)
print(test_str.split(single_bar))
print(test_str.split(double_bar))
d = parse_notes(test_str)

print(json.dumps(d, indent=2, ensure_ascii=False))
print("\n".join(map(convert, d.values())))
