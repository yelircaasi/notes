#!/usr/bin/env python

import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = (
    [sys.argv[1]] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]
)

KEYS = [
    "text",
    "link",
    "type",
    "subtype",
    "tags",
    "subtags",
    "status",
    "dateCreated",
    "dateModified",
    "extra",
    "sorter",
    "id",
]
EXTRA_KEYS = [
    "language",
    "rating",
    "extraTags",
    "notes",
    "name",
    "description",
    "category",
    "link",
    "recency",
    "features",
    "commits",
    "class",
    "nixName",
    "filetype",
]
DEFAULT = {
    "text": "",
    "link": "",
    "type": "UNSPECIFIED",
    "subtype": "UNSPECIFIED",
    "tags": ["SORT"],
    "subtags": [],
    "status": "toRead",
    "dateCreated": "1970-01-01",
    "dateModified": "1970-01-01",
    "extra": {},
    "sorter": "UNSPECIFIED",
    "id": None,
}
TYPES = [
    "",
    "ankiSet",
    "book",
    "cheatSheet",
    "course",
    "course",
    "discussion",
    "dots",
    "dotsSingleApp",
    "foodItem",
    "guide",
    "idea",
    "instruction",
    "lectureNotes",
    "listeningAtom",
    "media",
    "mediaWebsite",
    "paper",
    "periodical",
    "person",
    "readingAtom",
    "readingMaterial",
    "reference",
    "resource",
    "resourceList",
    "route",
    "scriptCollection",
    "software",
    "talk",
    "thought",
    "toContributeTo",
    "tool",
    "tutorial",
    "typescript",
    "UNSPECIFIED",
    "videoAtom",
    "videoSet",
    "videoSet",
    "viewingAtom",
    "vocabword",
]
STATI = [
    "toRead",
    "selected",
    "",
    "maybeLater" "needsWork",
    "nahReference",
    "selectedForLater",
    "backPocket",
    "alreadyInUse",
    "useAsReference",
    "selectedNeedsNix",
    "needToTry",
    "nah",
    "current",
    "rejected",
    "later",
]
TAGS = set(
    [
        "accent",
        "acoustics",
        "adversarial",
        "aesthetics",
        "africa",
        "agriculture",
        "algorithm",
        "allusion",
        "alpine",
        "analysis",
        "anatomy",
        "android",
        "anki",
        "annotation",
        "ansiColor",
        "anthropology",
        "aphorism",
        "app",
        "appDevelopment",
        "architecture",
        "art",
        "arxiv",
        "asciiArt",
        "assembler",
        "ast",
        "astronomy",
        "async",
        "attention",
        "audio",
        "autodiff",
        "backend",
        "bash",
        "beautifulAlgorithms",
        "benchmarking",
        "bibliography",
        "bigData",
        "biology",
        "bitextAlignment",
        "book",
        "bookNotes",
        "bookToLiveBy",
        "boot",
        "browser",
        "buddhist",
        "bugTracker",
        "build",
        "c",
        "calculator",
        "calendar",
        "car",
        "challenge",
        "changeDirectory",
        "chatbot",
        "chatgpt",
        "cheatsheet",
        "chemistry",
        "cinema",
        "cli" "cli",
        "clock",
        "clojure",
        "cloud",
        "cloudResource",
        "clustering",
        "codeAnalysis",
        "codeImage",
        "codeRunning",
        "color",
        "colorInterpolation",
        "colorSpaceMapping",
        "colorTheme",
        "comedy",
        "commandLine",
        "comment",
        "commercial",
        "commit",
        "communication",
        "community",
        "compilation",
        "complex",
        "computerVision",
        "conference",
        "config",
        "configSwitching",
        "connectivity",
        "consciousness",
        "container",
        "cOrCpp",
        "coreutils",
        "corpus",
        "correctThinking",
        "cowsay",
        "cpp",
        "cracking",
        "creativity",
        "cryptography",
        "crystal",
        "cs",
        "css",
        "cuda",
        "curiosity",
        "curriculum",
        "dashboard",
        "data",
        "database",
        "dataFormat",
        "dataGeneration",
        "dataset",
        "date",
        "debug",
        "decisionTheory",
        "decisionTree",
        "deepLearning",
        "dermatology",
        "design",
        "determinant",
        "devenv",
        "diagram",
        "diff",
        "differentiation",
        "disassembly",
        "discord",
        "discrete",
        "display",
        "distribution",
        "distro",
        "docker",
        "documentary",
        "documentation",
        "dotfileManager",
        "dotnet",
        "dots",
        "dualMonitor",
        "earley",
        "econometrics",
        "economics",
        "editingEnhancement",
        "editingExtensions",
        "editor",
        "eigen",
        "electronics",
        "emacs",
        "email",
        "embedded" "embedded",
        "emoji",
        "emulation",
        "emulator",
        "encoding",
        "engineering",
        "ethics",
        "evolution",
        "exercism",
        "factorAnalysis",
        "fairness",
        "fallacy",
        "family",
        "feminism",
        "fennel",
        "fileBrowser",
        "fileMonitor",
        "finance",
        "fitness",
        "flake",
        "flashcard",
        "font",
        "food",
        "forcedAlignment",
        "fortran",
        "forum",
        "foss",
        "freeCodeCamp",
        "fsharp",
        "fun",
        "functional",
        "fuzzyFinder",
        "game",
        "gameTheory",
        "gaming",
        "gan",
        "garbageCollection",
        "gardening",
        "gemini",
        "general",
        "geography",
        "geometry",
        "git",
        "githoarder",
        "gitlab",
        "gnome",
        "go",
        "grammar",
        "graph",
        "graphics",
        "grecromancer",
        "grpc",
        "gtd",
        "gtk",
        "gui",
        "guix",
        "habit",
        "hank",
        "hardware",
        "haskell",
        "henryhiggins",
        "hex",
        "hierarchical",
        "hindu",
        "history",
        "homeManager",
        "hpc",
        "html",
        "huggingface",
        "humanities",
        "humor",
        "hwOrExam",
        "hybridModifier",
        "hyprland",
        "i3",
        "icon",
        "ide",
        "idea",
        "identity",
        "ifThen",
        "image",
        "imageEditor",
        "indentation",
        "inequality",
        "initSystem",
        "institution",
        "interaction",
        "interactive",
        "interlinear",
        "interlineator",
        "interview",
        "introspection",
        "ipa",
        "ireland",
        "ironNvim",
        "java",
        "javascript",
        "javaScript",
        "jewish",
        "jira",
        "joke",
        "jordanNormalForm",
        "json",
        "julia",
        "jupyter",
        "juventas",
        "jvm",
        "kanata",
        "kde",
        "keras",
        "keybind",
        "keyboard",
        "keyboardLayout",
        "keyboardTrainer",
        "kmonad",
        "knutils",
        "kotlin",
        "kubernetes",
        "landscapeClient",
        "languageLearning",
        "languageSimilarity",
        "latent",
        "launcher",
        "lazyman",
        "learningTheory",
        "learnopencv",
        "license",
        "lifeHack",
        "linearAlgebra",
        "linguistics",
        "linux",
        "lisp",
        "literature",
        "llm",
        "llvm",
        "logging",
        "logic",
        "lowLevel",
        "lsp",
        "lua",
        "machineEmulators",
        "make",
        "malina",
        "map",
        "markdown",
        "math",
        "mathExpressionParsing",
        "mathForNN",
        "matrix",
        "matrixDecomposition",
        "media",
        "medicine",
        "meditation",
        "mentalFortitude",
        "mentalHealth",
        "ml",
        "mlops",
        "mobile",
        "model",
        "moments",
        "monitoring",
        "motivation",
        "movie",
        "multiplexer",
        "music",
        "naiveBayes",
        "nand2tetris",
        "nativeAmerican",
        "nbcat",
        "nebokrai",
        "neorg",
        "network",
        "neuralNetwork",
        "neuro",
        "news",
        "nim",
        "nix",
        "nixEli5",
        "nlp",
        "nlq",
        "node",
        "notebook",
        "noteToSelf",
        "notification",
        "novelWriting",
        "npm",
        "nsm",
        "nvidia",
        "nvim",
        "nvimPlugin",
        "obsidian",
        "ocaml",
        "octave",
        "oldvim",
        "opengl",
        "operatingSystem",
        "orgmode",
        "ornithology",
        "packaging",
        "pandoc",
        "paperReading",
        "paradigm",
        "parallelPhrases",
        "paremiology",
        "parenting",
        "parsing",
        "pde",
        "pedagogy",
        "performance",
        "perl",
        "person",
        "personalSite",
        "personalWebsite",
        "peudoscience",
        "philanthropy",
        "philosophy",
        "phon",
        "phone",
        "php",
        "picker",
        "pictrix",
        "pipeline",
        "podcast",
        "poetry",
        "politics",
        "polyglotToolkit",
        "polymathy",
        "practicalLiving",
        "presentation",
        "privacy",
        "productivity",
        "proglang",
        "proglangTable",
        "project",
        "proof",
        "proofsBook",
        "psychology",
        "publicSpeaking",
        "python",
        "pytorch",
        "qAndA",
        "qt",
        "quantum",
        "quote",
        "rag",
        "raku",
        "ralm",
        "randomForest",
        "raspberryPi",
        "reading",
        "reddit",
        "refactoring",
        "referenceProject",
        "regex",
        "regression",
        "relationship",
        "relativity",
        "resourceList",
        "ricing",
        "rl",
        "rlang",
        "rlcard",
        "rootDetector",
        "rosettaProjects",
        "rosettaRegex",
        "routewindow",
        "ruby",
        "running",
        "rust",
        "scala",
        "science",
        "scienceFiction",
        "scikit",
        "scraping",
        "screenRecorder",
        "screenshot",
        "scriptCollection",
        "scripting",
        "search",
        "security",
        "semantics",
        "sequence",
        "server",
        "setTheory",
        "sex",
        "sexuality",
        "sheetMusic",
        "shell",
        "shinto",
        "signalProcessing",
        "siteTheming",
        "snippet",
        "social",
        "socialScience",
        "sociology",
        "software",
        "solver",
        "song",
        "sops",
        "SORT",
        "sorting",
        "speechProcessing",
        "speechSynthesis",
        "sponsorship",
        "sport",
        "spotify",
        "stackexchange",
        "stackoverflow",
        "stata",
        "statistics",
        "streaming",
        "styleTransfer",
        "svg",
        "symbolicComputing",
        "system",
        "table",
        "taskRunner",
        "teams",
        "tech",
        "template",
        "templating",
        "terminal",
        "termulator",
        "testing",
        "tex",
        "tf",
        "theano",
        "thinkTank",
        "tmux",
        "top",
        "topology",
        "touchTyping",
        "trace",
        "transcription",
        "transformer",
        "translation",
        "travel",
        "treesitter",
        "tripPlanner",
        "tts",
        "tui",
        "typescript",
        "typing",
        "typst",
        "ui",
        "userscript",
        "veryShortIntroduction",
        "videoEditor",
        "vision",
        "visualization",
        "viterbi",
        "voiceConversion",
        "vscode",
        "wallpaper",
        "wasm",
        "weather",
        "webDev",
        "websocket",
        "widget",
        "wikipedia",
        "wiktionary",
        "windows",
        "wisdom",
        "wisdomLiterature",
        "wordEmbedding",
        "work",
        "writing",
        "xgboost",
        "yankPaste",
        "youtube",
        "zellij",
        "zen",
        "zettelkasten",
        "zig",
        "zoroastrian",
    ]
)


def remove_duplicates_keep_order(tags: list[str]) -> list[str]:
    already = set()
    cleaned = []
    for tag in tags:
        if not tag in already:
            already.add(tag)
            cleaned.append(tag)
    return cleaned


def lint_tags(tags: list[str]) -> list[str]:
    tags = list(filter(bool, tags))
    if len(tags) != len(set(tags)):
        # print("DUPLICATE TAGS:", tags)
        tags = remove_duplicates_keep_order(tags)

    return tags


def make_id() -> str:
    random16 = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"AUTO:{random16}"


def lint_note(note: dict) -> dict:
    note = DEFAULT | note

    note["tags"] = lint_tags(note["tags"])
    note["subtags"] = lint_tags(note["subtags"])
    extra = {k: v for k, v in note.items() if k not in KEYS}
    note = {k: v for k, v in note.items() if k in KEYS}
    # print(note)
    note["extra"].update(extra)

    return note


def format_notes(notes: list[dict]) -> str:
    s = json.dumps(notes, ensure_ascii=False)
    s = re.sub('("[^"]+": \{"text")', r"\n\1", s)
    return s


for p in files:
    print(p)
    with open(p) as f:
        notes = json.load(f)

    notes = {k: lint_note(v) for k, v in notes.items()}
    # notes = {k: v | {"id": k} for k, v in notes.items()}
    note_string = format_notes(notes)
    # print(note_string[:1000])

    with open(p, "w") as f:
        f.write(note_string)
