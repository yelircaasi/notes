"^[\*\$] (.+)$"
'{"text": "$1", "type": "book", "tags": ["cs", "", ""], "status": "toRead", "rating": "", "language": "", "extraTags": {}},'

def process_line(s, tag=""):
    tags, meat = ([""] + s.split(" <|> "))[-2:]
    tags = str([tag] + tags.split("{")[-1].split("}")[0].strip().split() + [""]).replace("'", '"')
    return f'{{"text": "{meat}", "type": "book", "tags": {tags}, "status": "toRead", "rating": "", "language": "", "extraTags": {{}}}},'


def process_lines(s, tag=""):
    lines = s.split("\n")
    def pl(line):
        return process_line(line, tag)
    print("\n".join((map(pl, lines))))

