import json


import json
import re
import sys
from pathlib import Path
import random
import string
import os


directory = Path("json-notes")
files = [sys.argv[1]] if sys.argv[1:] else [directory / f for f in os.listdir(directory)]

KEYS = ["note", "id", "type", "subtype", "tags", "subtags", "status", "dateCreated", "dateModified", "extra", "sorter"]
DEFAULT = {
    "note": "",
    "id": None,
    "type": "UNSPECIFIED",
    "subtype": "",
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
    "cli"
    "cli",
    "clock",
    "clojure",
    "cloud",
    "cloudResource",
    "clustering",
    "codeAnalysis",
    "codeImage",
    "codeRunning",
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
    "embedded"
    "embedded",
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
])

TOFIX = set([
        "filetype:PDF",
        "language:AR-LV",
        "language:AR",
        "language:AS",
        "language:CZ",
        "language:DA",
        "language:DE",
        "language:EL",
        "language:EN",
        "language:EO",
        "language:ES",
        "language:FA",
        "language:FI",
        "language:FR",
        "subtag:dataMining",
        "language:GRC",
        "language:HE",
        "language:HR",
        "language:IN",
        "language:IT",
        "language:JA",
        "language:KO",
        "language:LA",
        "language:LA/GRC",
        "language:MULTI",
        "language:NL",
        "language:NO",
        "language:OTHER",
        "language:PL",
        "language:PT",
        "language:QU",
        "language:RU",
        "language:SA",
        "language:SV",
        "language:SW",
        "language:UK",
        "language:ZH",
        "logit/softmax",
        "rating:highPriority"
        "rating:excellent",
        "rating:exemplary",
        "rating:phenomenal",
        "status:current",
        "status:later",
        "status:maybeLater",
        "status:nah",
        "status:nahReference",
        "status:rejected",
        "subtag:2sls",
        "subtag:advanced",
        "subtag:awesomewm",
        "subtag:babylonian",
        "subtag:base",
        "subtag:behavioral",
        "subtag:bellman",
        "subtag:blue",
        "subtag:bluish",
        "subtag:boilerplate",
        "subtag:bspwm",
        "subtag:cityBuildingSimulation",
        "subtag:classical",
        "subtag:comparison",
        "subtag:confucian",
        "subtag:cornwall",
        "subtag:criticism",
        "subtag:deepRl",
        "subtag:disentanglement",
        "subtag:django",
        "subtag:dotProduct",
        "subtag:dwl",
        "subtag:dwm",
        "subtag:errorClustering",
        "subtag:example",
        "subtag:fixedEffects",
        "subtag:foilArmsAndHog",
        "subtag:fontSize",
        "subtag:framework",
        "subtag:fromPicture",
        "subtag:fullstack",
        "subtag:fundamental",
        "subtag:gnostic",
        "subtag:graphing",
        "subtag:harmonizing",
        "subtag:heterodox",
        "subtag:inference",
        "subtag:installation",
        "subtag:instrumentalVariables",
        "subtag:internals",
        "subtag:interpretable",
        "subtag:introduction",
        "subtag:ip",
        "subtag:jain",
        "subtag:jekyll",
        "subtag:jimmyCarr",
        "subtag:joshJohnson",
        "subtag:kivy",
        "subtag:knn",
        "subtag:large",
        "subtag:light",
        "subtag:macos",
        "subtag:macro",
        "subtag:manx",
        "subtag:meta",
        "subtag:micro",
        "subtag:mitchellAndWebb",
        "subtag:mysql",
        "subtag:nextSteps",
        "subtag:other",
        "subtag:otherWm",
        "subtag:personal",
        "subtag:plotting",
        "subtag:probitLogitTobit",
        "subtag:prolog",
        "subtag:purple",
        "subtag:qtile",
        "subtag:rachelParris",
        "subtag:rain",
        "subtag:rasa",
        "subtag:react",
        "subtag:readingRoadmap",
        "subtag:recent",
        "subtag:ricingTool",
        "subtag:river",
        "subtag:scalp",
        "subtag:reference",
        "subtag:nextStep",
        "subtag:scotland",
        "subtag:atom",
        "subtag:screencasting",
        "subtag:celtic"
        "subtag:semisupervised",
        "subtag:pgm",
        "subtag:customLinuxKernel",
        "subtag:dataMining",
        "type:media",
        "subtype:newsletter",
        "subtag:sigmaOs",
        "subtag:singleApp",
        "subtag:snl",
        "subtype:toContributeTo",
        "subtag:specificApps",
        "subtag:specificTopics",
        "subtag:starter",
        "subtag:studioC",
        "subtag:knowledgeDiscovery",
        "subtag:sublimeText",
        "subtag:summary",
        "subtag:svd",
        "subtag:sway",
        "subtag:tda",
        "subtag:tensor",
        "subtag:tensorNetwork",
        "subtag:bioinformatics",
        "subtag:theory",
        "subtag:treatmentEffects",
        "subtag:trick",
        "subtag:wayfire",
        "subtag:welsh",
        "subtag:x86",
        "subtag:xmonad",
        "subtag:zoology",
        "subtype:article",
        "subtype:blog",
        "subtype:blogPost",
        "subtype:cookbook",
        "subtype:dictionary",
        "subtype:educational",
        "subtype:handbook",
        "subtype:longCourse",
        "subtype:educational",
        "subtype:short",
        "subtype:ytchannel",
        "type:course",
        "type:course",
        "type:course", 
        "type:course/tutorial",
        "type:curation",
        "type:foodItem",
        "type:guide",
        "type:idea",
        "type:book",
        "subtags:engine",
        "type:instruction",
        "type:lectureNotes",
        "type:listeningAtom",
        "type:paper",
        "type:periodical",
        "type:readingAtom",
        "type:reference",
        "type:resource",
        "type:resourceList",
        "type:route",
        "type:talk",
        "type:tutorial",
        "type:videoAtom",
        "type:vocabword",
        "subtag:engine",
        "type:cheatSheet",
        "rating:highPriority",
        "subtype:theme",
        "subtag:semisupervised",
        "rating:excellent",
        "subtag:miscellaneous",
        "type:tool",
        "subtag:dataMining",
        "subtag:nextStep"
        
    ])

ALLOWED = TAGS | TOFIX
FORBIDDEN = set([])

def lint_note(note: dict) -> dict:
    note = DEFAULT | note
    tags = [t for t in note["tags"]]
    for t in tags:
        if not t in TAGS:
            FORBIDDEN.add(t)
        if t.startswith("rating:"):
            rating = t.split(":")[-1]
            print("rating:", rating)
            note["extra"].update({"rating": rating})
            note["tags"].remove(t)
        elif t.startswith("type:"):
            typ = t.split(":")[-1]
            print("type:",typ)
            if note["type"]:
                print("old type", note["type"])
            note["type"] = typ
            note["tags"].remove(t)
        elif t.startswith("subtype:"):
            subtype = t.split(":")[-1]
            print("subtype:", subtype)
            if note["subtype"]:
                print("old subtype", note["subtype"])
            note["subtype"] = subtype
            note["tags"].remove(t)
        elif t.startswith("subtag:"):
            subtag = t.split(":")[-1]
            print("subtag:", subtag)
            if not subtag in note["subtags"]:
                note["subtags"].append(subtag)
            note["tags"].remove(t)
        elif t.startswith("language:"):
            language = t.split(":")[-1]
            print("language:", language)
            note["extra"].update({"language": language})
            note["tags"].remove(t)
        elif t.startswith("status:"):
            status = t.split(":")[-1]
            print("status:", status)
            note["status"] = status
            note["tags"].remove(t)
        
        elif t.startswith("filetype:"):
            filetype = t.split(":")[-1].lower()
            print("filetype:", filetype)
            note["extra"].update({"filetype": filetype})
            note["tags"].remove(t)
        
        

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


print(FORBIDDEN)


