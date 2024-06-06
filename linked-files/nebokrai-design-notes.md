# Nebokrai Design Philosophy

Tool for planning, prioritizing, scheduling, and tracking. Designed by me for me to be an
all-in-one way to stay organized and motivated by keeping short-term goals and plans aligned with
long-term goals.

Still unstable and in undergoing rapid development. Currently written in the Python standard
library (no other dependencies), but liable to be re-written in another better-suited (perhaps
more attractive?) language. The README may describe some not-yet-implemented features, as I am
giving
['readme-driven development'](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
a try.

nebokrai is informed by a set of guiding principles, a few of which will likely sound familiar to
anyone who has spent time in or around software development:

* **declarativeness**: what we want is clearly specified in one place and the program is tasked with
  implementing said specification, as opposed to the user having to manually spell out every step -
  more on this in the [detailed design notes](...)
* **purity**: no side effects
  * i.e. what is planned and scheduled follows directly and deterministically from the declaration
  * purity in this context brings with it a striking number of benefits:
    * **transparent relationship** between all components of the system, from long-terms plans and
      goals down to short-term schedules and to-do lists - this hints at the possibility of
      something analogous to backpropagation, but that is not yet on the horizon (cross-lingual
      pun not intended)
    * **attribution**, i.e. low-level details like a daily schedule have their roots in what I
      really want in the long run and if I don't like or understand something, I can trace it back
      to the  declaration to understand why the program planned / scheduled it that way - in other
      words, nothing is random and everything has a discoverable cause
* **resilience**: known to nerds as 'fault tolerance'
  * life happens, and the ability to adjust a plan following failures  and setbacks is essential
  * plans and goals without resilience are simply too brittle and are too likely to be abandoned in
    frustration
* **observability and traceability via logging**: the practice and paradigm of keeping detailed
  notes on what happened and how and why is that we can look at what went wrong and, conversely,
  what went well
  * this brings with it accountability, which it turns out is important for humans for a number of
    reasons
  * prevents self-deception
  * opens the door to (teaser alert!) cool dashboards and visualizations
* **modularity**: the system consists of smaller parts, which in turn consist of smaller parts,
  and while they interact seamlessly, each is as coherent and self-contained as possible

## Coming Soon

* something akin to GTD (Getting Things Done)
* Taskwarrior and Timewarrior integration
* integration with Neorg
* TUI, including Gantt and calendar views and vim keybindings and color customizations
* native Android app / Linux mobile / etc

## Miscellaneous

Switch fom Roadmaps::Project::Task hierarchy to Project::Task; use tags for organizing projects and tasks.

### Android App

* Design: to-do list with routine lists, scheduler, and corresponding notifications

### Page structure

* Day
  * Morning Routine
  * Evening Routine
  * Roadmap Items
* Week
  * Recurring
  * Roadmap Items
* Month
  * Recurring
  * Roadmap Items
* Year
  * Recurring
  * Roadmap Items
* Planner
* Record of accomplishments

FIXME### Operations

* Schedule Item → add to Planner
* Move Item | Year to quarter | Quarter to month | Month to Week | Month to Day | Week to Day | 
* Change time: push back in time | pull forward in time | switch items | 

## Dev Notes

Nebokrai considerations:

functions should be composable and, as much as posssible, do exactly one thing.
This will make testing easier, as well as adding new functionalities.

## Nebokrai Feature Ideas

* ( ) Gantt chart (from Roadmaps spreadsheet)
* ( ) support for different roadmaps, zipped together
* ( ) support for adding a project (e.g. book) with a list/range of sub-projects (e.g. chapters)
* ( ) even: evenly spaced until end date
* ( ) fixed: fixed spacing
* ( ) easy-to-use calendar data structure
* ( ) load-balancing by day:
* ( ) make small adjustments to move some tasks (sub-projects) from one
* ( ) day types (intense, light, etc)
* ( ) time estimation of task (optional upper/lower bounds)
* ( ) priority of task
* ( ) big rocks first - scheduled time blocks, around which everything else must fit
* ( ) Daily scheduler - algorithm to do it automatically using estimated duration and priority levels (both urgency and importance)
* ( ) Ability to navigate in all 4 directions
* ( ) switch to daily slice
* ( ) sortable by tags incl. priority and est. duration
* ( ) different adjustment modes when I fall behind or get ahead:
* ( ) rigid: push all bask by k days, with exceptions for locked elements
* ( ) compress: squish all items evenly together
* ( ) rollover: what is unfinished today gets added to tomorrow
* ( ) → default mode for each project
* ( ) vim-based navigation in the terminal
* ( ) common vim keybindings to move around TUI
* ( ) shortcuts to navigate to links → open new terminal tab with book / notes editor, switch to new pre-configured workspace (rofi integration?)
* ( ) syncing and integration with Github / Nextcloud / Drive
* ( ) Calendar
* ( ) Correspondence between all components

## Features - Other Notes

* Notifications
  * start/stop
  * n-minute warning
  * n-minute interval
* Schedule Item Stopwatch
* Daily Score
* Weekly Score
* Statistics
  * score over time
  * statistics for routine items

## Nebokrai Overview

* make signal-based or matrix-based apps for sending links to myself without email or notion → or use email client? XMPP, Matrix, SMTP, POP3, IMAP, IRC
* CLI “Digital Assistant”
* Design Goals: Create a system that takes into account all obligations, goals, and values to optimally allocate time. Most importantly, this system should be:
  * purely functional: the same inputs will always result in the same outputs, with no side-effects
  * declarative: the entities.base (tasks, etc.) and settings declared provide a complete specification of my system; I say 'what' and the software tells me 'when'.
  * simple and intuitive to use
  * robust: when circumstances change, I can adjust the plans via the interface provided (as opposed to internal hacking) and carry on without problems
  * integrated: planager provides an all-encompassing system to keep all aspects of my life in order
  * simplifying: this tool should save me time and reduce my cognitive load, not become a distraction or an obstacle
* Additionally, my system must be:
  * reproducible - installable via Nix
  * all-encompassing
  * cross-device
  * self-syncing
  * well-defined
  * robust (able to deal dynamically with unforeseen circumstances)
  * hierarchical (goal broken into tasks, each of which can be recursively broken into tasks)
  * keyboard-driven
  * aesthetically pleasing
  * in keeping with the Second Brain framework
* integrated and internally consistent
* End result:
  * phone app (android or linux mobile) → Notion or Appflowy
  * phone notifications: from app or via Telegram or other
  * frontend in neovim using neorg.nvim
  * automatic (hook-driven) and encrypted sync between devices, sync server
  * features:
  * built on the .norg file format
  * basic tack tracking, functionality from taskwarrior → probably replicate without
  * roadmap-based task scheduling and adjustment, as supplied by ganttouchthis
  * automatic, configurable, and manually adjustable planning (15-minute blocks with sufficient flex time)
  * recurring tasks and routines (as given by current Telegram bot)
  * performance analytics and summaries
* Consituents
  * planager-core → divide into scheduling and tracking? implement in Rust, Haskell, Ocaml, Idris, Agda, or Purescript
  * planager-backend - serves -flutter, -frontend, -signal, -nvim?, -tui? → IHP, Obelisk, Yesod, or Warp?
  * planager-flutter - for Android app → alternative like Kivy or cross-platform Rust toolkit [dioxus](https://dioxuslabs.com/), or Flutter Rust bridge?
  * planager-frontend
  * planager-signal → semaphore of signal-cli or signal-api-rest-api or signal-bot (java) or libsignal or signal-server?
  * requirements
    1. notify of start/end of schedule entries
    2. record (as response to prompts) status of tasks, including sub-items of routines
    3.
  * planager.nvim - from nvim with Neorg, or as neorg module?
  * planager-tui - bubbletea, rich, textual, or Ratatui?
  * planager-django - prototying for backend → alternatives: flask, cherry-py, fastapi?
  * planager-sync
  * Old: Overall Project Structure
  * Databases - synced across server, phone, and desktop (backed up on Github/Google Drive/NextCloud?)
    * TW database
    * GTT JSON data
  * Hosted VM server Linode, Heroku, Digital Ocean, Replit…?)
    * GTT Engine
    * Scheduler (merge into GTT → planager - or include GTT as a dependency?)
    * recurring tasks and set routines
    * Tracker - food, fitness, etc.
      * combining with scheduler and GTT into controller app?
    * Telegram Bot (or over way to send notifications)
    * Weekly Email Report
    * Sync between taskwarrior, GTT
  * Zapier Hooks?
  * Desktop GTT TUI
    * communication with server
  * (inthe.am, Foreground App)
  * Taskwarrior
    * TUI: Vit / taskwarrior-tui
    * taskw for interaction with Python packages
  * Timewarrior
  * AppFlowy → accessible from Android and Linux
  * [appflowy](https://appflowy.io/) - just needs cloud setup, vim keybindings, and customizable colors → on the way? [shortcuts](https://docs.appflowy.io/docs/appflowy/community/appflowy-mentorship-program/mentorship-2022/mentee-projects/shortcuts-and-customized-hotkeys-for-appflowy) and [color themes](https://docs.appflowy.io/docs/appflowy/community/appflowy-mentorship-program/mentorship-2022/mentee-projects/custom-themes) - shortcuts may require further hacking, or maybe just a kanata/other layer on top [...](https://blog.appflowy.io/appflowy-2nd-anniversary-and-2023-roundup/)
* ( ) get Android build for AppFlowy working → [appflowy-io/appflowy/actions/runs/4582846778/jobs/8093324716](https://github.com/AppFlowy-IO/AppFlowy/actions/runs/4582846778/jobs/8093324716)
* ( ) [docs.flutter.dev/deployment/android](https://docs.flutter.dev/deployment/android)
* ( ) [appflowy-io projects](https://github.com/orgs/AppFlowy-IO/projects)
* ( ) eventually add vim keybindings (<https://appflowy.gitbook.io/docs/essential-documentation/shortcuts>)
* ChatGPT on hosting

* add/edit projects & tasks in popup, in command line, or in .norg file
* input → output principle:
* routines, projects, and settings as input, schedule & summary statistics as output
* schedule + tracking as input → log and performance metrics as output

## Miscellaneous Ideas, Brainstorming

* read [this](https://cf020031308.github.io/blog/a-brief-history-of-my-task-management/)

* deadlines in different levels: dream | want| should | must -> severity/goodness
* nebokrai: add subcommands: track, blame (tool to show origin of some aspect of derived result), edit, add (interactive), sync, dashboard, dryrun {subcommand}, revert -> make (where appropriate) CLI and TUI (= interactive) versions of subcommands
* nebokrai idea: 'sacred' time blocks for flow
* self-daily: presentation about yesterday and plans for today
* make a habit-building subapp in the scheduling app
* use the concept of satisfiability -> [libsolv](https://github.com/openSUSE/libsolv)
* → make nebokrai usable as a plugin/integration for smos?
* how to integrate appflowy into a system with taskwarrior, ganttouchthis, timewarrior, telegram, etc?
* Add daily (yesterday) review to tracking feature → circular feedback, as review requires editing declaration, but thisis a feature, rather than a bug or compromise
* Include commands such as `nebokrai check` to ensure inputs and outputs are in a consistent state → add optimizations such as caching and using time last edited → make certain files read-only by all except nebokrai user
* GTT: tui with typer? which dependencies? pure stdlib? -> integration with vit / taskw / taskwarrior -> later: rewrite in Rust?
* Twilio → SMS?
* Zapier?
* IRC?
* learn about plugin architecture - neovim, qutebrowser, anki, qtile, xplr, emacs, awesome, hilbish, vim, wezterm, kitty, other lua-configurable apps, etc

## System Bridge

Write CLI/TUI, probably in Rust, to connect all tools I use as part of my personal organization system.

Name ideas:

* org
* pm ('personal management')
* sys
* glue
* sb ('system bridge')
* system
* (subcomponent) pomodorrior
* notekeeper, notehoarder, notewarrior

Maybe prototype in Bash, Python, or Julia.

## Ganttouchthis / Ganttstop

* change GTT to write only changed tasks / projects / days, but keep in-memory for speed (except backlog and done; unnecessary)
  * crystalize gtt API, database format, object API
  * GTT functionality: add project, edit project, edit task -> done to done DB, project from backlog, add to backlog, adjust task distribution: balanced|rollover|rigid, edit backlog item, project from backlog item, check validity & check data consistency (in memory & in database & between memory and database), exact & fuzzy search, TUI, export as SVG

## Kanban View

* can a Kanban board be combined with my system -> integrate as a view of the tasks
* Personal Kanban
