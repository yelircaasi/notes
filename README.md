# json-notes (jn)

json-notes, with command `jn`

A command-line tool for managing notes, with an emphasis on tags and accessibility.

## Desiderata

* easy to add notes, including links shared from my mobile device (copying and sorting links has taken up too much of my time)
* easy to edit notes in a comfortable TUI or in a snappy CLI - low overhead; makes it comfortable to jot down ideas and save links without breaking my focus
* support for import/export to/from a variety of data formats
* easy to query and sort notes, with an informative set of attributes, especially tags, that make it easy to find what I am looking for
* versioning and backup via git
* streamlined note-to-task pipeline - easy to generate tasks from notes
* storage format that is both human-readable and machine-readable: JSON, the GOAT of data formats! - allows me to harness the awesome power of Neovim and its finest plugins, as well as the many excellent command-line data-wrangling tools such as jq, ripgrep, ast-grep, regular expressions, and so on
* no vendor lock-in
* well-defined schema
* intuitive and comfortable CLI command structure
* improved command-line interface relative to what Python argparse offers; nested subcommands instead of endless hyphens
* raise exceptions early, with informative error messages
One of the advantaged of a tag-first system, rather than enforcing a strict hierarchical structure, is that I can avoid headaches related to ambiguous categories; often a note belongs to multiple topics, and tags can handle this better than a partitioning topic hierarchy.
* attractive output, summaries, and visualizations

## Usage

Each command is of the form `jn FILE_NAME ACTION [ARGS]`. If 'ALL' is passed for `FILE_NAME`, all files are treated jointly.

A special case is when 'meta' is passed as the filename, as this supports several commands for getting general information and help. See the 'Meta' section below for more information.

### Actions

* no action: enter interactive TUI mode
* `add-file FILENAME` - add a new JSON file with the name `FILENAME`, where the .json ending is optional
* `add FILENAME NOTE_TEXT [ATTR_NAME:ATTR_VALUE ...]` - add a new note
* `show` - pretty-print notes matching the query
* `import FILETYPE FILEPATH` - import notes from a supported datatype, one of json, markdown, txt, yaml, toml, djot.
* `export FILETYPE [PREDICATES]` - export notes to a supported datatype, one of json, markdown, djot, latex, yaml, toml, html, ... .
* `summarize [PREDICATES]` - print a brief summary of the data matching the predicates
* `summarize-visual` - like `summarize`, but enhanced with visual output
* `split [NEW_FILENAME]` - split filename.json into {{FILENAME}}.json and (by default) {{FILENAME}}-subset.json, typically for more convenient editing
* `join [OTHER_FILENAME]` - reverse `split`, taking by default {{FILENAME}}-subset.json
* `fetch-email` - collect notes from emails whose subject line begins with 'jn '; additional attributes may be passed in the body (first line) or in the subject line following 'jn '. This follows the same general ATTRIBUTE:VALUE syntax and is parsed in the same way.
`sort` - TODO

### Meta Actions

To see the structure of the notes directory, use 'meta' as a stand-in for the filename, following which the following commands are available:

* `files` - list the files contained in the notes directory, along with the brief description contained in `meta.json`
* `describe FILENAME` - prints all available metadata regarding FILENAME (contained in meta.json)
* `fuzzy FILENAME` - returns the closest match to FILENAME in the notes directory
* `category CATEGORY` - prints the files belonging to CATEGORY, along with their descriptions
* `add-description FILENAME` - add or overwrite the description for FILENAME

### Query Syntax

Each query predicate is supplied as a regular command-line argument, having the form `ATTRIBUTE:CONDITION`. Each attribute has certain permissible condition types, and the condition is validated and parsed differently depending on the attribute. For example, `priority:<0.5` evaluates to true for all notes `d` satisfying `d['priority'] < 0.5`.

To avoid implementing an entire parser for and embedded query language, multiple query predicates are treated conjunctively; they must all evaluate to true. To circumvent this, it is possible to pass a pure-Python lambda, which is evaluated as is and must act on a dictionary of the pre-defined form. For example, `"lambda d: (d['status']=='todo') and (("science" in d['tags']) or (d['priority'] > 0.7))"` is a valid query which may be passed at the command line.

A sophisticated parser and embedded query language may be added later, but this has low priority relative to other features on the roadmap.

### Data Format

For simplicity and consistency, each note object is required to have the same keys, with the `extra` key enabling storage of additional custom information. The full specification is found in `jn-schema.json`, but here is a brief overview:

* `id` - uuid of the note
* `text` - array of strings corresponding to lines in the note
* `type` - one of ...
* `status` - one of "todo", "later", "urgent"
* `rating` - one of "\*", "\*\*", "\*\*\*", "\*\*\*\*", "\*\*\*\*\*"
* `depends` - uuid of the note 'blocking' the current note, i.e. a note that must be read or processed before the current note can be read/processed
* `extra` - object contaiing arbitrary attributes
