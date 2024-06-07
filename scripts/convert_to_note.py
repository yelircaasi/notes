import sys
import json


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


def convert(note: dict) -> str:
    width = 100
    double_bar = c.black(width * "═")
    single_bar = c.black(width * "─")

    

    return "\n".join([
        double_bar,
        c.cyan("|".join(note["tags"])),
        single_bar,
        c.magenta(note["note"]),
        single_bar

    ])


with open(sys.argv[1]) as f:
    notes = json.load(f)

print("\n".join(map(convert, notes[:10])))
