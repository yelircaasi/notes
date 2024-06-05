import sys
import re
import json

p = sys.argv[1]
with open(p) as f:
    txt = f.read()


def default():
    return {"note": "", "type": "", "tags": ["math", "", ""], "status": "toRead", "language": ""}


lines = txt.split("\n")

new = []
tags = []
for line in filter(bool, map(str.strip, lines)):
    if line.startswith("#->"):
        tags = list(map(str.strip, re.sub("#-> +", "", line).split(",")))
        print(tags)
    elif line.startswith("{"):
        try:
            d = json.loads(line.strip(","))
        except:
            print(line)
            exit()
        d["tags"].extend(tags)
        new.append(d)
    elif line.startswith("* "):
        d = default()
        d["note"] = line[2:]
        d["tags"].extend(tags)
        new.append(d)

    else:
        print("===============", line)

with open(p, "w") as f:
    json.dump(new, f, ensure_ascii=False)