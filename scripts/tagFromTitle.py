import sys
import re
import json

p = sys.argv[1]
with open(p) as f:
    txt = f.read()


def default():
    return {"note": "", "type": "", "tags": ["", "", ""], "subtags": [""], "status": "toRead", "language": ""}

def parse_tags(line: str) -> tuple[list[str], list[str]]:
    segments = re.sub("#-> +", "", line).split("|") + [""]
    return tuple(map(lambda t: list(map(str.strip, t.strip().split(","))), segments[:2]))


lines = txt.split("\n")

new = []
tags = []
subtags = []
for line in filter(bool, map(str.strip, lines)):
    if line.startswith("#->"):
        tags, subtags = parse_tags(line)
        # print(tags, subtags)
    elif line.startswith("{"):
        try:
            d = json.loads(line.strip(","))
        except:
            print(line)
            print("failed")
            exit()
        if not "subtags" in d:
            d.update({"subtags": []})
        d["tags"].extend(tags)
        d["subtags"].extend(subtags)
        new.append(d)
    elif line.startswith("* "):
        d = default()
        d["note"] = line[2:]
        d["tags"].extend(tags)
        d["subtags"].extend(subtags)
        new.append(d)

    else:
        print("===============", line)

with open(p, "w") as f:
    txt = json.dumps(new, ensure_ascii=False).replace("}, {", "},\n{")
    f.write(txt)
