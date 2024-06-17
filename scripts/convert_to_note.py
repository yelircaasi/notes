#!/usr/bin/env python

import sys
import json
from typing import Callable


class Colorizer:
    def __init__(self, use_colors: bool = True) -> None:
        if use_colors:
            self.BLACK = "\u001b[30m"
            self.RED = "\u001b[31m"
            self.GREEN = "\u001b[32m"
            self.YELLOW = "\u001b[33m"
            self.BLUE = "\u001b[34m"
            self.MAGENTA = "\u001b[35m"
            self.CYAN = "\u001b[36m"
            self.WHITE = "\u001b[37m"
            self.RESET = "\u001b[0m"
        else:
            self.BLACK = ""
            self.RED = ""
            self.GREEN = ""
            self.YELLOW = ""
            self.BLUE = ""
            self.MAGENTA = ""
            self.CYAN = ""
            self.WHITE = ""
            self.RESET = ""

    def _format(self, text: str, color_code: str) -> str:
        return f"{color_code}{text}{self.RESET}"

    def black(self, text: str) -> str:
        return self._format(text, self.BLACK)

    def red(self, text: str) -> str:
        return self._format(text, self.RED)

    def green(self, text: str) -> str:
        return self._format(text, self.GREEN)

    def yellow(self, text: str) -> str:
        return self._format(text, self.YELLOW)

    def blue(self, text: str) -> str:
        return self._format(text, self.BLUE)

    def magenta(self, text: str) -> str:
        return self._format(text, self.MAGENTA)

    def cyan(self, text: str) -> str:
        return self._format(text, self.CYAN)

    def white(self, text: str) -> str:
        return self._format(text, self.WHITE)


c = Colorizer(use_colors=True)
print(c.black("black"))
print(c.red("red"))
print(c.green("green"))
print(c.blue("blue"))
print(c.yellow("yellow"))
print(c.cyan("cyan"))
print(c.magenta("magenta"))
print(c.white("white"))


type_icons = {
    "": "",
    "listeningAtom": "_",
    "readingAtom": "_",
    "viewingAtom": "_",
    "listeningSet": "_",
    "readingSet": "_",
    "viewingSet": "_",
    "dots": "_",
    "resourceList": "_",
    "course": "_",
    "software": "_",
    "idea": "_",
    "person": "_",
    "tool": "_",
    "reference": "_",
    "foodItem": "_",
    "route": "_",
    "ankiSet": "_",
    "discussion": "_",
    "vocabWord": "_",
    "instruction": "_",
    "unsupported": ""
}
status_icons = {
    "toRead": "󰄱",
    "done": "󰄲",
    "unsupported": "",
    "": "_",
    "toReread": "_",
    "currentReading": "_",
    "alreadyRead": "_",
    "softwareSelected": "_",
    "softwareNahReference": "_",
    "softwareSelectedForLater": "_",
    "softwareBackPocket": "_",
    "softwareAlreadyInUse": "_",
    "softwareUseAsReference": "_",
    "softwareSelectedNeedsNix": "_",
    "softwareNeedToTry": "_",
    "softwareNah": "_",
    "softwareRejected": "_",
    "softwareLater": "_",
    "softwareNeedsWork": "_",
}
tag_icons = {
    "biology": "󰻖",
    "unsupported": "X"
}


def preprocess_tags(tags: list[str], subtags: list[str]) -> str:
    return "".join((
        '-'.join(map(c.cyan, tags)),
        "::",
        '-'.join(map(c.yellow, subtags))
    ))


def wrap_line(line: str, length: int, formatter: Callable) -> str:
    ...


def convert(note: dict) -> str:
    width = 100
    double_bar = c.magenta(width * "═")
    single_bar = c.black(width * "─")

    tags_and_subtags = preprocess_tags(note['tags'], note['subtags'])
    id_ = c.blue(note['id'][:21])
    note_text = f"\n{c.magenta(note['text'])}\n"
    # type_text = type_icons.get(note.get("type", "unsupported"), "?")
    type_text = c.red(f"{note['type']}::{note['subtype']}")
    # status = status_icons.get(note.get("status", "unsupported"), "?")
    status = note["status"]
    link_text = c.red(note["link"])
    # extra = c.black(json.dumps(note["extra"], indent=2, ensure_ascii=False) or "")
    extra = c.black("\n".join((f"{k}: {v}" for k, v in note["extra"].items())))
    date_line = f"{c.red(note['dateCreated'])}                      {c.blue(note['dateModified'])}                              {c.black(note['sorter'])}"

    

    return "\n".join([
        double_bar,
        f"{id_:<20}  {type_text}  {status}  {tags_and_subtags}",
        # f"{id_:<35} {type_:>8} {status:>8} {tags_and_subtags:>50}",
        single_bar,
        note_text,
        single_bar,
        link_text,
        single_bar,
        extra,
        single_bar,
        date_line,
        single_bar,
        ""

    ])


with open(sys.argv[1]) as f:
    notes = list(json.load(f).values())[:10]

print("\n".join(map(convert, notes)))
