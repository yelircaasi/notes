#!/usr/bin/env python

import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = [sys.argv[1]] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]

KEYS = ["note", "id", "type", "tags", "subtags", "status", "dateCreated", "dateModified", "extra", "sorter"]
DEFAULT = {
    "note": "",
    "id": None,
    "type": "UNSPECIFIED",
    "subtype": "UNSPECIFIED",
    "tags": ["SORT"],
    "subtags": [],
    "status": "toRead",
    "dateCreated": "1970-01-01",
    "dateModified": "1970-01-01",
    "extra": {},
    "sorter": "UNSPECIFIED"
}
TYPES = [
    "",
    "UNSPECIFIED",
    "book",
    "readingMaterial",
    "readingAtom",
    "viewingAtom",
    "course",
    "dots",
    "typescript",
    "periodical",
    "idea",
    "dotsSingleApp",
    "media-website",
    "person",
    "scripts",
    "videoSet",
    "reference",
    "thought",
    "ankiSet",
    "listeningAtom",
    "discussion",
    "toContributeTo",
]
STATI = [
    "toRead",
    "selected",
    ""
    "needsWork",
    "selectedForLater",
    "backPocket",
    "alreadyInUse"
    "useAsReference",
    "selectedNeedsNix",
    "needToTry"
]
TAGS = set([
    "agriculture",
    "annotation",
    "ansiColor",
    "benchmarking",
    "bibliography",
    "clock",
    "clojure",
    "cli",
    "typescript",
    "system",
    "pde",
    "comment",
    "connectivity",
    "correctThinking",
    "cracking",
    "embedded",
    "crystal",
    "curriculum",
    "dataGeneration",
    "diagram",
    "documentary",
    "dotfileManager",
    "fallacy",
    "family",
    "fsharp",
    "gemini",
    "grammar",
    "grpc",
    "hierarchical",
    "ironNvim",
    "languageSimilarity",
    "performance",
    "hpc",
    "polymathy",
    "proof",
    "data",
    "map",
    "nvidia",
    "allusion",
    "game",
    "social",
    "proofsBook",
    "stackoverflow",
    "svg",
    "computerVision",
    "forcedAlignment",
    "symbolicComputing",
    "table",
    "trace",
    "zellij",
    "matrixDecomposition",
    "treesitter",
    "tripPlanner",
    "git",
    "sponsorship",
    "nsm",
    "attention",
    "transformer",
    "resourceList",
    "biology",
    "sex",
    "top",
    "asciiArt",
    "dataFormat",
    "evolution",
    "shinto",
    "lazyman",
    "clustering",
    "comedy",
    "humor",
    "keyboard",
    "app",
    "jordanNormalForm",
    "juventas",
    "terminal",
    "android",
    "latent",
    "llvm",
    "proof",
    "translation",
    "rlang",
    "history",
    "boot",
    "car",
    "corpus",
    "dashboard",
    "huggingface",
    "screenshot",
    "template",
    "paremiology",
    "speechSynthesis",
    "assembler",
    "gan",
    "podcast",
    "compilation",
    "mathExpressionParsing",
    "flashcard",
    "mentalHealth",
    "parenting",
    "privacy",
    "raku",
    "relationship",
    "rosettaRegex",
    "sequence",
    "templating",
    "wasm",
    "science",
    "peudoscience",
    "freeCodeCamp",
    "dots",
    "music",
    "architecture",
    "async",
    "bookNotes",
    "commandLine",
    "fuzzyFinder",
    "jira",
    "kmonad",
    "lsp",
    "rust",
    "search",
    "creativity",
    "container",
    "ornithology",
    "diff",
    "phon",
    "differentiation",
    "bigData",
    "codeRunning",
    "landscapeClient",
    "logic",
    "notification",
    "paradigm",
    "videoEditor",
    "dermatology",
    "learningTheory",
    "neuralNetwork",
    "economics",
    "nix",
    "docker",
    "scikit",
    "gtk",
    "accent",
    "motivation",
    "nbcat",
    "server",
    "editingEnhancement",
    "mathForNN",
    "pedagogy",
    "notebook",
    "exercism",
    "finance",
    "graphics",
    "database",
    "nlp",
    "cinema",
    "audio",
    "rl",
    "machineEmulators",
    "operatingSystem",
    "parallelPhrases",
    "php",
    "python",
    "llm",
    "proglangTable",
    "ast",
    "complex",
    "fairness",
    "introspection",
    "kde",
    "medicine",
    "meditation",
    "mentalFortitude",
    "ocaml",
    "qt",
    "sorting",
    "websocket",
    "cloud",
    "cloudResource",
    "hybridModifier",
    "packaging",
    "stata",
    "editor",
    "jupyter",
    "sociology",
    "rlcard",
    "solver",
    "sport",
    "nvim",
    "lifeHack",
    "ide",
    "pytorch",
    "security",
    "teams",
    "topology",
    "decisionTheory",
    "distribution",
    "encoding",
    "gardening",
    "sexuality",
    "stackexchange",
    "software",
    "tex",
    "acoustics",
    "cryptography",
    "mlops",
    "scala",
    "learnopencv",
    "media",
    "chatgpt",
    "algorithm",
    "ethics",
    "foss",
    "logging",
    "markdown",
    "moments",
    "taskRunner",
    "icon",
    "interlinear",
    "perl",
    "tf",
    "knutils",
    "regression",
    "wisdomLiterature",
    "polyglotToolkit",
    "userscript",
    "embedded"
    "pde",
    "wordEmbedding",
    "zoroastrian",
    "java",
    "javaScript",
    "food",
    "haskell",
    "ifThen",
    "tui",
    "cli"
    "tmux",
    "linearAlgebra",
    "aphorism",
    "astronomy",
    "configSwitching",
    "cowsay",
    "dotnet",
    "fileMonitor",
    "githoarder",
    "graph",
    "henryhiggins",
    "hex",
    "interlineator",
    "publicSpeaking",
    "spotify",
    "typing",
    "typst",
    "weather",
    "indentation",
    "monitoring",
    "c",
    "geometry",
    "dataset",
    "design",
    "discrete",
    "bookToLiveBy",
    "gui",
    "keyboardTrainer",
    "styleTransfer",
    "writing",
    "nvimPlugin",
    "cuda",
    "factorAnalysis",
    "gameTheory",
    "hwOrExam",
    "opengl",
    "interview",
    "phone",
    "SORT",
    "politics",
    "africa",
    "earley",
    "fileBrowser",
    "keybind",
    "productivity",
    "project",
    "econometrics",
    "network",
    "vision",
    "ui",
    "cOrCpp",
    "oldvim",
    "testing",
    "javascript",
    "lowLevel",
    "fitness",
    "decisionTree",
    "qAndA",
    "touchTyping",
    "hank",
    "quantum",
    "randomForest",
    "thinkTank",
    "mobile",
    "grecromancer",
    "ireland",
    "poetry",
    "xgboost",
    "philosophy",
    "adversarial",
    "autodiff",
    "calendar",
    "chemistry",
    "codeAnalysis",
    "colorInterpolation",
    "colorSpaceMapping",
    "date",
    "discord",
    "hindu",
    "joke",
    "json",
    "keyboardLayout",
    "license",
    "nim",
    "webDev",
    "network",
    "color",
    "noteToSelf",
    "sheetMusic",
    "widget",
    "zig",
    "raspberryPi",
    "personalWebsite",
    "gnome",
    "yankPaste",
    "anatomy",
    "documentation",
    "feminism",
    "reddit",
    "work",
    "communication",
    "nlq",
    "snippet",
    "transcription",
    "ipa",
    "scriptCollection",
    "codeRunning",
    "linguistics",
    "beautifulAlgorithms",
    "siteTheming",
    "linux",
    "anki",
    "consciousness",
    "devenv",
    "travel",
    "general",
    "image",
    "parsing",
    "math",
    "config",
    "gaming",
    "humanities",
    "colorTheme",
    "rosettaProjects",
    "cs",
    "calculator",
    "coreutils",
    "dualMonitor",
    "habit",
    "html",
    "identity",
    "jvm",
    "naiveBayes",
    "nand2tetris",
    "paperReading",
    "picker",
    "presentation",
    "theano",
    "visualization",
    "appDevelopment",
    "arxiv",
    "cpp",
    "flake",
    "reading",
    "proglang",
    "youtube",
    "css",
    "malina",
    "viterbi",
    "go",
    "font",
    "jewish",
    "multiplexer",
    "hardware",
    "cheatsheet",
    "forum",
    "quote",
    "literature",
    "wisdom",
    "aesthetics",
    "alpine",
    "browser",
    "changeDirectory",
    "codeImage",
    "community",
    "curiosity",
    "email",
    "emoji",
    "fortran",
    "interaction",
    "kotlin",
    "make",
    "pandoc",
    "relativity",
    "scienceFiction",
    "scraping",
    "screenRecorder",
    "build",
    "guix",
    "rag",
    "ralm",
    "voiceConversion",
    "bash",
    "buddhist",
    "distro",
    "book",
    "editingExtensions",
    "wallpaper",
    "veryShortIntroduction",
    "speechProcessing",
    "backend",
    "bugTracker",
    "commit",
    "conference",
    "disassembly",
    "display",
    "eigen",
    "emulation",
    "geography",
    "gitlab",
    "imageEditor",
    "keras",
    "node",
    "orgmode",
    "art",
    "streaming",
    
    "kanata",
    "nebokrai",
    "idea",
    "signalProcessing",
    "julia",
    "documentation",
    "neuro",
    "psychology",
    "news",
    "debug",
    "deepLearning",
    "languageLearning",
    "statistics",
    "socialScience",
    "determinant",
    "emulator",
    "fennel",
    "launcher",
    "matrix",
    "movie",
    "npm",
    "obsidian",
    "octave",
    "anthropology",
    "philanthropy",
    "refactoring",
    "ruby",
    "setTheory",
    "termulator",
    "windows",
    "zettelkasten",
    "emacs",
    "referenceProject",
    "i3",
    "tts",
    "vscode",
    "song",
    "wiktionary",
    "homeManager",
    "model",
    "person",
    "bitextAlignment",
    "gtd",
    "wikipedia",
    "ricing",
    "chatbot",
    "regex",
    "garbageCollection",
    "inequality",
    "initSystem",
    "kubernetes",
    "nativeAmerican",
    "novelWriting",
    "pictrix",
    "pipeline",
    "rootDetector",
    "routewindow",
    "running",
    "sops",
    "challenge",
    "lisp",
    "engineering",
    "lua",
    "functional",
    "ml",
    "fun",
    "hyprland",
    "neorg",
    "shell",
    "semantics",
    "practicalLiving",
    "zen",
    "interactive",
    "institution",
    "commercial",
    "nixEli5",
    "analysis",
    "scripting",
    "personalSite",
    "electronics",
    "tech",
    "ui",
])

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
    s = json.dumps(notes, ensure_ascii=False).replace("}, {", "},\n{")
    return s
    



for p in files:
    print(p)
    with open(p) as f:
        notes = json.load(f)

    notes = list(map(lint_note, notes))
    note_string = format_notes(notes)

    with open(p, "w") as f:
        f.write(note_string)





