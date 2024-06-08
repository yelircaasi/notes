#!/usr/bin/env python

import sys
import json
from typing import Callable


class Colorizer:
    def __init__(self) -> None:
        self.BLACK = "\u001b[30m"
        self.RED = "\u001b[31m"
        self.GREEN = "\u001b[32m"
        self.YELLOW = "\u001b[33m"
        self.BLUE = "\u001b[34m"
        self.MAGENTA = "\u001b[35m"
        self.CYAN = "\u001b[36m"
        self.WHITE = "\u001b[37m"
        self.RESET = "\u001b[0m"

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


c = Colorizer()
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
    "unsupported": ""
}
status_icons = {
    "toRead": "󰄱",
    "done": "󰄲",
    "unsupported": ""
}
tag_icons = {
    "biology": "󰻖",
    "unsupported": "X"
}


def preprocess_tags(tags: list[str]) -> str:
    return c.cyan('|'.join(tags))

def preprocess_subtags(subtags: list[str]) -> str:
    return c.yellow('|'.join(subtags))
    


def wrap_line(line: str, length: int, formatter: Callable) -> str:
    ...


def convert(note: dict) -> str:
    width = 100
    double_bar = c.magenta(width * "═")
    single_bar = c.black(width * "─")

    tags = preprocess_tags(note['tags'])
    subtags = preprocess_subtags(note['subtags'])
    id_ = c.blue(note['id'][:21])
    note_text = c.magenta(note["note"])
    type_ = type_icons.get(note.get("type", "unsupported"), "?")
    status = status_icons.get(note.get("status", "unsupported"), "?")


    

    return "\n".join([
        double_bar,
        f"{id_:<35} {tags:^33} {subtags:^33} {type_:>8} {status:>8}",
        single_bar,
        note_text,
        single_bar

    ])


with open(sys.argv[1]) as f:
    notes = json.load(f)

print("\n".join(map(convert, notes[:10])))