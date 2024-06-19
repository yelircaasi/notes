'''
Characters not treated as special characters by Bash:
A-Za-z % - _ ~ ^ @ [ ] { } : , . / ? +

NEW CONSIDERATIONS =============================================
bash special characters not allowed; neither are spaces
structural characters in the query language are { } , . : 
: should be reserved for binding attribute names to values, such as type:book
_ and - would be nice to have as valid identifier characters
support character sets from other languages, such as cyrillic
~ for negation
= for id
@ to reference saved queries
/ for status
+ to prefix extra attributes
^ for date
* for rating
% for type
﹪ for subtype
euro sign for (human) language
] for programming language

other unicode characters?

? allow matching 'empty' values, such as None or ""

Examples: 

consilium edit {@biologyTop,philosophy,neuroscience}.^2023-01-01.*5.{%book,%idea,%site}
================================================================

(rejected: --additional_argument bound to value with non non-space non-alphanumeric character)
-> instead: use environment variables, all of which are optional

MAYBE LATER:
@[] to reference the path to a file -> assumed to be relative if not starting with / ; ~ allowed and . not allowed; _/ refers to query_files in nots directory


@[...] to refer to the contents of a path
~ negation
[...] - regex search within string: ?tag[regex],tag2[regex2]

?@savedTagQueryAlias
=@savedSetAlias

@savedQueryAlias

=id1,id2,id3def condition_from_string(s: str) -> Callable[[dict], bool]:
    # to be fully implemented for all attributes later; just tags for now
    def inner(d: dict):
        return s in d["tags"]
    
    return inner


def condition_from_dict(query_tree: dict) -> Callable:
    def condition_from_element(element: str | dict) -> Callable[[dict], bool]:
        if isinstance(element, str):
            return condition_from_string(element)
        elif isinstance(element, dict):
            return condition_from_dict(element)
    
    if "AND" in query_tree:
        return lambda d: all(map(lambda f: f(d), map(condition_from_element, query_tree["AND"])))
    elif "OR" in query_tree:
        return lambda d: any(map(lambda f: f(d), map(condition_from_element, query_tree["OR"])))
    else:
        raise ValueError
=[regex for id]
:type
:type:subtype
::type:subtype or empty type
:type::subtype - type and subtype or empty subtype

%status
%%status or empty

*rating above
*~rating below
**rating or empty


[substring/regex in text]
[substring/regex in text, case insensitive]i
{substring/regex in link}
{substring/regex in link, case insensitive}i

^DDDD-DD-DD - oldest date modified
^^DDDD-DD-DD - oldest date created
^~DDDD-DD-DD - newest date modified
^^~DDDD-DD-DD - newest date created

+extraTag:value
++extraTag:value or empty


?tag.tag.tag:subtag.subtag.subtag
  . OR operator for tags
  , OR operator for tags
  {...} for tag grouping, but for now givedef condition_from_string(s: str) -> Callable[[dict], bool]:
    # to be fully implemented for all attributes later; just tags for now
    def inner(d: dict):
        return s in d["tags"]
    
    return inner


def condition_from_dict(query_tree: dict) -> Callable:
    def condition_from_element(element: str | dict) -> Callable[[dict], bool]:
        if isinstance(element, str):
            return condition_from_string(element)
        elif isinstance(element, dict):
            return condition_from_dict(element)
    
    if "AND" in query_tree:
        return lambda d: all(map(lambda f: f(d), map(condition_from_element, query_tree["AND"])))
    elif "OR" in query_tree:
        return lambda d: any(map(lambda f: f(d), map(condition_from_element, query_tree["OR"])))
    else:
        raise ValueError AND precedence over OR, 
    requiring more work on the user's end for simpler implementation.
  ~ for tag negation
  example: @tag1.tag2,tag3.tag4

_language
__language or empty value for language


Tentative:

]progLang (need to change to camel case)
]]fileType
'''
from typing import Any, Callable
import re


def parse_id(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("=[A-Za-z,]+|=\[[A-Za-z]\]+", subquery)

    if subquery.startswith("=["):
        rgx = re.compile(subquery[2: -1])
        return lambda d: re.search(rgx, d["id"])
    # elif subquery.startswith("="):
    else:
        sq = subquery[1:]
        return lambda d: sq == d["id"]


def parse_tag_dsl(tag_subquery: str, include_empty: bool = False) -> Callable[[dict[str, Any], bool]]:
    """
To parse your custom DSL into a Python expression as described, we need to follow a similar process: tokenize the input, parse the tokens into an abstract syntax tree (AST), and then generate the equivalent Python code from the AST. Given your specific DSL syntax, we'll focus on identifiers, brackets, and the two infix operators.
Step-by-Step Implementation

    Tokenizer: Split the input into tokens recognizing identifiers, brackets, and operators.
    Parser: Convert the tokens into an AST.
    Code Generation: Convert the AST into a Python lambda expression.

Implementation in Python

Here's how you can achieve this:

```python

import re

# Step 1: Tokenizer
def tokenize(dsl_code):
    token_specification = [
        ('LBRACE', r'\{'),        # Left bracket
        ('RBRACE', r'\}'),        # Right bracket
        ('AND', r'\.'),           # AND operator
        ('OR', r','),             # OR operator
        ('IDENTIFIER', r'[a-z][A-Za-z]*'),  # Identifiers
        ('SKIP', r'[ \t]+'),      # Skip over spaces and tabs
        ('MISMATCH', r'.'),       # Any other character
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    tokens = []
    for mo in re.finditer(token_regex, dsl_code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens

# Step 2: Parser
def parse(tokens):
    def parse_expression(tokens):
        if not tokens:
            return None
        
        expr = []
        while tokens:
            token = tokens.pop(0)
            if token[0] == 'IDENTIFIER':
                expr.append(('IDENTIFIER', token[1]))
            elif token[0] == 'AND':
                expr.append(('AND',))
            elif token[0] == 'OR':
                expr.append(('OR',))
            elif token[0] == 'LBRACE':
                inner_expr = parse_expression(tokens)
                expr.append(('EXPR', inner_expr))
            elif token[0] == 'RBRACE':
                break
        
        return expr

    return parse_expression(tokens)

# Step 3: Code Generation
def generate_python_code(ast):
    def generate_expression(expr):
        stack = []
        for token in expr:
            if token[0] == 'IDENTIFIER':
                stack.append(f"'{token[1]}' in x")
            elif token[0] == 'AND':
                right = stack.pop()
                left = stack.pop()
                stack.append(f"({left} and {right})")
            elif token[0] == 'OR':
                right = stack.pop()
                left = stack.pop()
                stack.append(f"({left} or {right})")
            elif token[0] == 'EXPR':
                inner_expr = generate_expression(token[1])
                stack.append(f"({inner_expr})")
        
        return stack[0] if stack else ''

    return f"lambda x: {generate_expression(ast)}"

# Putting it all together
def dsl_to_python(dsl_code):
    tokens = tokenize(dsl_code)
    ast = parse(tokens)
    python_code = generate_python_code(ast)
    return python_code

# Example usage
dsl_code = "{var1.var2},{var3.var4}"
python_code = dsl_to_python(dsl_code)
print(python_code)  # Output should be: lambda x: ('var1' in x and 'var2' in x) or ('var3' in x and 'var4' in x)
```

Explanation

    Tokenizer: The tokenize function uses regular expressions to split the input into tokens, recognizing identifiers, brackets, and operators.
    Parser: The parse function converts the list of tokens into an AST. It handles nested expressions inside brackets and supports AND/OR operations.
    Code Generation: The generate_python_code function converts the AST into a Python lambda expression. It constructs the appropriate logical operations based on the AST.

This implementation will take your custom DSL and produce the corresponding Python lambda expression, as specified.
    """
    ...

def parse_tags(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^\?[A-Za-z\[\]\.,]", subquery)
    subquery += ":"
    tag_query, subtag_query = re.split(":+", subquery)[1:3]
    tag_match_empty = bool(re.match("^::", subquery))
    subtag_match_empty = bool(re.match("^:+[A-Za-z]+::"))

    tag_condition = parse_tag_dsl(tag_query, include_empty=tag_match_empty)
    subtag_condition = parse_tag_dsl(subtag_query, include_empty=subtag_match_empty)

    return lambda d: tag_condition(d) and subtag_condition(d)


def parse_type(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^:", subquery)

    if subquery.startswith(""):
        _test = ...
    else:
        _test = ...
    return _test


def parse_status(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^~", subquery)

    if subquery.startswith(""):
        _test = ...
    else:
        _test = ...
    return _test


def parse_due_date(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^\^~?{1,2}\d{4}-\d\d-\d\d", subquery)
    
    if subquery.startswith("^^"):
        _test = ...
    else:
        _test = ...
    return _test


def parse_rating(subquery: str) -> Callable[[dict[str, Any]], bool]:
    m = re.match("^\*+~?$", subquery)
    assert m
    sq = m.group(0)
    
    if subquery.endswith("?~") or subquery.endswith("?~"):
        return lambda d: d["rating"] in sq
    elif subquery.endswith("opt"):
        return lambda d: (d["rating"]) or not (bool(d["rating"]))
    elif subquery.endswith("~"):
        return lambda d: d["rating"] in sq
    else:
        return lambda d: sq in d["rating"]


def parse_date(subquery: str) -> Callable[[dict[str, Any]], bool]:
    m = re.match("^\^{1,2}~?(\d{4}-\d\d-\d\d)$", subquery)
    assert bool(m)
    date = m.group(1)
    
    if subquery.startswith("^^~"):
        return lambda d: d[""]
    elif subquery.startswith("^^"):
        return ...
    elif subquery.startswith("^~"):
        return ...
    elif subquery.startswith("^"):
        return ...


def parse_extra_attribute(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^\+", subquery)

    if subquery.startswith("++"):
        _test = ...
    else:
        _test = ...
    return _test


def parse_language(subquery: str) -> Callable[[dict[str, Any]], bool]:
    assert re.match("^_", subquery)

    if subquery.startswith("__"):
        _test = ...
    else:
        _test = ...
    return _test


dispatcher = {
    "=": parse_id,
    "?": parse_tags,
    ":": parse_type,
    "%": parse_status,
    "*": parse_rating,
    "^": parse_date,
    "+": parse_extra_attribute,
    "_": parse_language,
}

order = {
    "=": 0,
    "?": 1,
    ":": 2,
    "~": 3,
    "%": 4,
    "*": 5,
    "^": 6,
    "+": 7,
    "_": 8,
}


def parse_query_old(subqueries: list[str]) -> Callable[[dict[str, Any]], bool]:
    subqueries.sort(key=lambda sq: order.get(sq[0], 9))
    filters = tuple(map(lambda sq: dispatcher[sq[0]](sq)))
    
    def inner(d: dict[str, dict]) -> list[dict]:
        condition = lambda note: all(map(lambda filt: filt(note), filters))
        return tuple(filter(condition, d.values()))

    return inner


def parse_query(q: str) -> Callable:
    """
Now, building on the previous task, I want to generate a data structure corresponding to the boolean expression above, but converted to a dictionary whose keys are "AND" or "OR" and whose values are lists containing identifiers (strings) or objects.. So x.{y,z} would evaluate to {"AND": ["x", {"AND": ["y", "z"]}]} and {a.b},{a,d} would evaluate to {"OR": [{"AND": ["a", "b"]}, {"OR": ["a", "d"]}]}
ChatGPT

To transform your custom DSL into a nested dictionary structure, we need to modify the code to construct a dictionary instead of generating a Python lambda expression.
Implementation Steps

    Tokenizer: We'll use the same tokenizer as before to split the input into tokens.
    Parser: We'll modify the parser to construct a nested dictionary structure representing the boolean logic.
    Dictionary Construction: Convert the AST into the desired dictionary format.

Implementation in Python

Here’s how you can achieve this:

python

import re

# Step 1: Tokenizer
def tokenize(dsl_code):
    token_specification = [
        ('LBRACE', r'\{'),        # Left bracket
        ('RBRACE', r'\}'),        # Right bracket
        ('AND', r'\.'),           # AND operator
        ('OR', r','),             # OR operator
        ('IDENTIFIER', r'[a-z][A-Za-z]*'),  # Identifiers
        ('SKIP', r'[ \t]+'),      # Skip over spaces and tabs
        ('MISMATCH', r'.'),       # Any other character
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    tokens = []
    for mo in re.finditer(token_regex, dsl_code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens

# Step 2: Parser
def parse(tokens):
    def parse_expression(tokens):
        if not tokens:
            return None
        
        expr = []
        while tokens:
            token = tokens.pop(0)
            if token[0] == 'IDENTIFIER':
                expr.append(('IDENTIFIER', token[1]))
            elif token[0] == 'AND':
                expr.append(('AND',))
            elif token[0] == 'OR':
                expr.append(('OR',))
            elif token[0] == 'LBRACE':
                inner_expr = parse_expression(tokens)
                expr.append(('EXPR', inner_expr))
            elif token[0] == 'RBRACE':
                break
        
        return expr

    return parse_expression(tokens)

# Step 3: Dictionary Construction
def generate_dict_structure(ast):
    def generate_expression(expr):
        stack = []
        current_op = None
        for token in expr:
            if token[0] == 'IDENTIFIER':
                stack.append(token[1])
            elif token[0] == 'AND':
                current_op = 'AND'
            elif token[0] == 'OR':
                current_op = 'OR'
            elif token[0] == 'EXPR':
                stack.append(generate_expression(token[1]))
        
        if current_op == 'AND':
            return {"AND": stack}
        elif current_op == 'OR':
            return {"OR": stack}
        elif len(stack) == 1:
            return stack[0]
        else:
            return stack
    
    result = generate_expression(ast)
    return result

# Putting it all together
def dsl_to_dict(dsl_code):
    tokens = tokenize(dsl_code)
    ast = parse(tokens)
    dict_structure = generate_dict_structure(ast)
    return dict_structure

# Example usage
dsl_code = "{var1.var2},{var3.var4}"
dict_structure = dsl_to_dict(dsl_code)
print(dict_structure)  # Output should be: {"OR": [{"AND": ["var1", "var2"]}, {"AND": ["var3", "var4"]}]}

dsl_code2 = "x.{y,z}"
dict_structure2 = dsl_to_dict(dsl_code2)
print(dict_structure2)  # Output should be: {"AND": ["x", {"OR": ["y", "z"]}]}

Explanation

    Tokenizer: The tokenize function splits the input into tokens recognizing identifiers, brackets, and operators.
    Parser: The parse function converts the list of tokens into an AST. It handles nested expressions inside brackets and supports AND/OR operations.
    Dictionary Construction: The generate_dict_structure function traverses the AST to construct a nested dictionary representing the boolean logic.

This implementation should correctly transform your DSL into the desired dictionary format. Adjustments can be made for more complex DSL structures or additional features.
    """
    ...


def condition_from_string(s: str) -> Callable[[dict], bool]:
    # to be fully implemented for all attributes later; just tags for now
    def inner(d: dict):
        return s in d["tags"]
    
    return inner


def condition_from_dict(query_tree: dict) -> Callable:
    def condition_from_element(element: str | dict) -> Callable[[dict], bool]:
        if isinstance(element, str):
            return condition_from_string(element)
        elif isinstance(element, dict):
            return condition_from_dict(element)
    
    if "AND" in query_tree:
        return lambda d: all(map(lambda f: f(d), map(condition_from_element, query_tree["AND"])))
    elif "OR" in query_tree:
        return lambda d: any(map(lambda f: f(d), map(condition_from_element, query_tree["OR"])))
    else:
        raise ValueError


"""
{x,y,z}.{a,b}
td = {
    "AND": [
        {"OR": ["x", "y", "z"]},
        {"OR": ["a", "b"]}
    ]
}


note = {"tags": ["a", "x"]}
note = {"tags": ["a", "b"]}
"""