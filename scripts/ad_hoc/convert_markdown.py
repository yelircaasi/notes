"^[\*\$] (.+)$"
'{"note": "$1", "type": "", "tags": ["proglang", "julia", ""], "status": "toRead", "rating": "", "language": "", "extraTags": {}},'

def process_line(s, tag=""):
    tags, meat = ([""] + s.split(" <|> "))[-2:]
    tags = str([tag] + tags.split("{")[-1].split("}")[0].strip().split() + [""]).replace("'", '"')
    return f'{{"note": "{meat}", "type": "book", "tags": {tags}, "status": "toRead", "rating": "", "language": "", "extraTags": {{}}}},'


def process_lines(s, tag=""):
    lines = s.split("\n")
    def pl(line):
        return process_line(line, tag)
    print("\n".join((map(pl, lines))))
