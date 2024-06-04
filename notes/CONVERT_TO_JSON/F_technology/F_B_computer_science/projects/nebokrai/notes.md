# Nebokrai Notes

https://github.com/phase1geo/Minder
https://rednotebook.app/
https://github.com/pimterry/notes
https://github.com/dj8yfo/meudeus $$$$$
https://github.com/saccarosium/shell-velocity
https://github.com/hovancik/stretchly (glean)
https://tetr.app/

## General

Ideal system:

* robust home server
* frequent (daily) external backups to an external device (gitlab, thumb drive/passport, proton drive/mega/etc)
* accessible from phone (android or linux) app, desktop gui, cli
* automatic (from declaration input) generation of plan, daily schedule, clothes, recipes, shopping lists
* simple tracking of metrics and goals
* all notes connected and in a structure that optimizes searchability and analysis
* easy to add new notes
* good way to share links, esp from my phone
* well-defined and easy-to-work-with data formats
* resilience: allowance for "shit happens" -> contingency
* minimal cognitive overhead -> maximal focus and flow
* informative feedback via diffs: planned|scheduled vs actual, prior plan vs updated plan, goal vs actual, goal vs updated goal

### System Bridge

Write CLI/TUI, probably in Rust, to connect all tools I use as part of my personal organization system.

Name ideas:

* org
* pm ("personal management")
* sys
* glue
* sb ("system bridge")
* system
* (subcomponent) pomodorrior
* notekeeper, notehoarder, notewarrior

Maybe prototype in Bash, Python, or Julia.

### Nebokrai Overview

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

### Miscellaneous Ideas, Brainstorming

* read [this](https://cf020031308.github.io/blog/a-brief-history-of-my-task-management/)

* deadlines in different levels: dream | want| should | must -> severity/goodness
* nebokrai: add subcommands: track, blame (tool to show origin of some aspect of derived result), edit, add (interactive), sync, dashboard, dryrun {subcommand}, revert -> make (where appropriate) CLI and TUI (= interactive) versions of subcommands
* nebokrai idea: "sacred" time blocks for flow
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

#### Feature Ideas

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

### Theory and Best Practices

* CODE Framework
  * C (Capture)
  * O (Organise)
  * D (Distill)
  * E (Express)

```txt
General advice

Here are some best practices for planning, organizing, and tracking your time:

1. Create a daily and/or weekly schedule: Make a list of tasks or activities that you need to complete for each day or week. Prioritize the most important tasks and schedule them during your most productive time of the day.
2. Use a task management system: Choose a task management tool that works for you, such as a to-do list app or a project management tool. This will help you keep track of your tasks and ensure you don't miss any deadlines.
3. Block out time for focused work: Schedule uninterrupted time for work that requires your full concentration. Use this time to complete tasks that require your full attention, and avoid distractions like social media and email.
4. Take regular breaks: Taking breaks helps you recharge and stay focused. Try the Pomodoro technique, which involves working for 25 minutes and taking a 5-minute break, then repeating this cycle.
5. Use a time tracker: Track your time to see where you're spending it. This will help you identify time-wasting activities and areas where you can improve your productivity.
6. Review your progress regularly: Take time at the end of each day or week to review your progress. Celebrate your successes, identify areas for improvement, and adjust your schedule and tasks as necessary.
7. Be flexible: No matter how well you plan, unexpected things will always come up. Be flexible and willing to adjust your schedule and tasks as needed to accommodate these changes.

Remember, finding a system that works for you may take some trial and error. Experiment with different tools and techniques until you find what works best for you.
```

### Naming Ideas

* ganttstopme
* ganttstopmenow
* planalyzer
* taskifist
* consilium
* nebokrai
* haskwarrior
* horizon
* [consilium](https://en.wiktionary.org/wiki/consilium)
* ganttouchthis
* roadmapper
* scrumbag

## Entities

* old: Entity Types
  * roadmap: a 'master plan' for some area such as "Rust programing language" or "muscular flexibility" involving multiple steps or projects
  * project: a self-contained unit of work that can be broken down into smaller parts, such as a book to read or a coding project
  * task: a small, atomic unit of work, ideally one that can be completed in less than 120 minutes; can be recurring or one-time
  * sequences: an alias for a list of tasks which are always to be performed together (typically sequentially), such as a morning or evening routine; handled identically to a task
  * option set: a group of alternatives, from which I select one (or more); handled identically to a task
  * (old) adjustment types

```python

class AdjustmentType(Enum):
    AUTO = 0  # methods figure it out, based on priority and properties TODO: CLEANUP
    CLIP = 1  # higher-priority entry takes precedence and lower-priority activity makes way TODO: CLEANUP
    SHIFT = 2  #
    COMPRESS = 3  #
    COMPROMISE = 4  #
    DISPLACE = 5  #
```

### Approach to Hierarchical Organization

Switch fom Roadmaps::Project::Task hierarchy to Project::Task; use tags for organizing projects and tasks.

### Tasks

* Task definition entry points:
  * nvim
  * command line
  * Notion (check API and pull following trigger)
  * Task definition types:
  * from project creation
  * from project editing
  * manual add

### Entries

* Ways to add an entry
        1. from calendar
        2. from plan via explicit declaration (project file)
        3. from plan, without explicit declaration (roadmap file)
        4. from ad hoc
        5. from routines
* Entry Adding: An Entry object can be added to a Schedule object from one of 5 origins:
  * from Calendar (base schedules)
  * from plan via explicit declaration in project file
  * from plan via project expansion from roadmap file
  * from AdHoc, from adhoc file
  * from Routines, from routines file

## Planning and Scheduling (shared)

* Project and Task Dependency Logic
  * use only `.after` attribute; `.before` superfluous
  * add `.tmpdate` (or maybe `.placeholder_date`) attribute to tasks for sorting; default NullDate to allow for easy complex comparisons
  * 2-pass approach for planning: first regular planning to assign tmpdate, then adjust for dependencies
  * use special sorting (`__gt__ , __lt__, __ge__, __le__`) that first looks at `.after`, then at `.tmpdate`

  * Extension: Norg links allow me to specify sequential dependency relationships between tasks

  * Blocking Logic
  * blocks like 'work' that other smaller, more specific tasks can be scheduled on top of
  * blocks come from Calendar, AdHoc, Routines
  * potentially also from regular (roadmap-originating) tasks
  * used to 'collapse' durations together for planning and scheduling
  * Task 'Stacking'
  * combining tasks that can be done simultaneously, such as listening to a podcast on the way home
  * also allows 'time collapsing' during planning, scheduling with require something new and custom
  * Cases:
* ( ) plan overfull (error)
* ( ) plan fits exactly
* ( ) plan underfull
* ( ) rollover required (with priorities)
* ( ) with dependencies

### Solver Software

https://github.com/i-am-tom/holmes/
https://hackage.haskell.org/package/toysolver
https://hackage.haskell.org/package/datafix
https://github.com/McMasterU/HashedExpression
https://github.com/TOTBWF/clphs
https://www.swi-prolog.org/man/clpfd.html
https://github.com/travitch/ifscs
https://www.mattkeeter.com/projects/constraints/ $$$
https://github.com/ChrisPenner/mad-props
https://www.cs.yale.edu/homes/piskac/papers/2019HallahanETALquasiquoter.pdf
https://github.com/BillHallahan/G2Q
https://www.tweag.io/blog/2023-02-14-smtlib-backends/
Introducing Constraint Functional Logic Programming
https://en.wikipedia.org/wiki/Constraint_programming
https://timefold.ai/alternatives/gurobi-versus-timefold-comparison
https://timefold.ai/alternatives/google-or-tools-versus-timefold-comparison
https://developers.google.com/optimization/introduction
https://www.reddit.com/r/optimization/comments/13mrkr6/what_software_is_used_in_the_field_these_days/
https://news.ycombinator.com/item?id=31099186
https://jump.dev/JuMP.jl/stable/
https://github.com/TimefoldAI/timefold-solver

#### Solvers - ChatGPT Assistance

I want to write a Haskell problem that assigns tasks to times subject to a set of constraints and so as to optimize some metric. Can you name appropriate Haskell libraries for this purpose?

When writing a Haskell program to assign tasks to times subject to constraints and optimizing some metric, you are essentially dealing with a constraint satisfaction problem (CSP) or a constraint optimization problem (COP). Several libraries in Haskell can help you with this task. Here are some appropriate libraries:

SBV (SMT Based Verification):

SBV allows you to solve CSPs and optimization problems using SMT (Satisfiability Modulo Theories) solvers.
It's well-suited for problems where you have logical constraints and need to find satisfying assignments.
Documentation: SBV on Hackage

Example:

```haskell
import Data.SBV

taskAssignment :: IO AllSatResult
taskAssignment = allSat $ do
    -- Define your variables and constraints here
    return ()
```

Z3:

Z3 is an SMT solver from Microsoft Research that can be used through Haskell bindings.
It's powerful for both solving constraints and optimization problems.
Documentation: z3 Haskell bindings on Hackage

Example:

```haskell
import Z3.Monad

taskAssignment :: Z3 (Result, Model)
taskAssignment = evalZ3 $ do
    -- Define your variables and constraints here
    return ()
```

glpk-hs:

GLPK (GNU Linear Programming Kit) provides tools for solving linear programming and mixed integer programming problems.
Useful if your constraints and optimization metric can be expressed in linear form.
Documentation: glpk-hs on Hackage

Example:

```haskell
import Numeric.LinearProgramming

taskAssignment :: IO (OptSolution Double)
taskAssignment = do
    -- Define your problem here
    return ()
```

Monadic Constraint Programming (monadiccp):

This library provides monadic constructs for constraint programming.
Suitable for problems where you need more flexible and expressive constraints.
Documentation: monadiccp on Hackage

Example:

```haskell
import Control.CP.FD

taskAssignment :: IO ()
taskAssignment = runCP $ do
    -- Define your constraints and search strategy here
    return ()
```

Haskell-CAS (Constraint and Search):

A general-purpose library for constraint programming.
Provides various constraint solvers and search strategies.
Documentation: haskell-cas on Hackage

Example:

```haskell
import CAS

taskAssignment :: IO ()
taskAssignment = do
    -- Define your problem here
    return ()
```

Each of these libraries has its strengths and is suited for different kinds of problems. Choose the one that best matches the nature of your constraints and optimization metric. If your problem involves complex constraints and you need robust solving capabilities, using an SMT solver like SBV or Z3 might be the best choice. If your constraints are linear, then glpk-hs could be more appropriate. For more general and flexible constraint programming, monadiccp or haskell-cas can be very useful.

### Planning

* [WBS](https://en.wikipedia.org/wiki/Work_breakdown_structure)
* Planning Features
  * day maximum (from calendar) and rollover when this max is exceeded
  * use of priority
  * respecting precedence requirements (dependency of one task on another)
  * Planning Algorithm (Vanilla):
    1. get all tasks (via roadmaps)
    2. construct dependency tree of tasks
    3. get available time per day from calendar
    4. add tasks to day until the day is full

* distinguish between naive plan and calendar-adjusted plan
* Add desirability -> eating frogs idea
* Fix planning to have completed tasks have zero time where appropriate and actual time where appropriate.
* Add extra catch-all roadmap
* Sort projects in dependency order -> dependency tree structure
* Support earliest and latest dates, dependencies between tasks/projects/roadmaps -> raise error when declaration is impossible

#### Dependency Sorting

* need to write function `dependencySort` to put list of tasks in an order satisfying dependency constraints, raising an informative error if dependency constraints are irresoluble
* need to do a literature/code search to find relevant algorithms, implementations, and resources
* requires dependency graph data structure

To solve the task scheduling problem with dependencies, you can represent the tasks and their dependencies using a directed graph (digraph). In this graph, nodes represent tasks, and directed edges represent dependencies between tasks. The problem then becomes one of topological sorting, where you need to order the tasks such that for every directed edge \( A \rightarrow B \), task \( A \) comes before task \( B \).

If the graph has cycles, it means there are contradictory dependencies, and topological sorting will fail.

Here's a complete Haskell solution using the `containers` library to represent the graph and `topSort` from `Data.Graph` to perform the topological sort. If the graph has cycles, `topSort` will throw an exception.

First, you need to add the `containers` package to your project. You can do this by adding `containers` to your `.cabal` file under `build-depends` or by running `cabal install containers`.

```haskell
import Data.Graph
import Data.Array
import Data.Maybe (fromMaybe)
import Data.List (nub)

-- Define a type for tasks
type Task = String
type Dependency = (Task, Task)

-- Create a graph from tasks and their dependencies
buildGraph :: [Task] -> [Dependency] -> (Graph, Vertex -> (Task, Task, [Task]), Task -> Maybe Vertex)
buildGraph tasks deps =
    let
        -- Create a list of (task, task, [dependent tasks]) tuples
        taskTuples = [(task, task, dependents task) | task <- tasks]
        
        -- Find all tasks that depend on a given task
        dependents task = [b | (a, b) <- deps, a == task]
    in
        graphFromEdges taskTuples

-- Topologically sort tasks
topologicalSort :: [Task] -> [Dependency] -> Either String [Task]
topologicalSort tasks deps =
    let
        (graph, nodeFromVertex, vertexFromKey) = buildGraph tasks deps
    in
        case topSort graph of
            [] -> Left "There is a cycle in the task dependencies."
            sortedVertices -> Right $ map (\v -> let (key, _, _) = nodeFromVertex v in key) sortedVertices

main :: IO ()
main = do
    let tasks = ["task1", "task2", "task3", "task4"]
    let dependencies = [("task1", "task2"), ("task2", "task3"), ("task1", "task3"), ("task3", "task4")]
    
    case topologicalSort tasks dependencies of
        Left err -> putStrLn $ "Error: " ++ err
        Right sortedTasks -> putStrLn $ "Sorted tasks: " ++ show sortedTasks
```

Explanation

1. **Task and Dependency Types**:
   * Define `Task` as a type alias for `String` to represent tasks.
   * Define `Dependency` as a type alias for a tuple `(Task, Task)` to represent dependencies between tasks.

2. **Building the Graph**:
   * `buildGraph` takes a list of tasks and a list of dependencies and returns a graph representation along with helper functions.
   * `taskTuples` is a list of tuples where each tuple contains a task, the task itself (as a key), and a list of dependent tasks.
   * `dependents` is a helper function that finds all tasks that depend on a given task.
   * `graphFromEdges` is used to create the graph, which is represented internally as an array of vertices.

3. **Topological Sort**:
   * `topologicalSort` takes a list of tasks and dependencies and attempts to topologically sort them.
   * It calls `topSort` on the graph, which returns a list of vertices in topological order.
   * If `topSort` returns an empty list, it indicates a cycle in the graph.
   * Otherwise, it maps the sorted vertices back to their corresponding tasks.

4. **Main Function**:
   * The `main` function defines a list of tasks and their dependencies.
   * It calls `topologicalSort` and prints either an error message (if there's a cycle) or the sorted list of tasks.

Notes:

* This solution assumes that all tasks are listed in the `tasks` list and that all dependencies are provided in the `dependencies` list.
* The `topSort` function from `Data.Graph` is used to perform the topological sort, and it throws an exception if the graph contains a cycle. The error handling in this example catches this case and returns an appropriate error message.

To extend the previous solution to sort tasks based on additional attributes such as priority and dread (both in descending order), while ensuring that dependency constraints take precedence, we can use a combination of topological sorting and stable sorting by these attributes.

First, let's define the Task type to include priority and dread. Then, we'll modify the topologicalSort function to first perform the topological sort based on dependencies and subsequently sort the tasks within the topological order based on the attributes.

Here's how you can achieve this:

```haskell
{-# LANGUAGE OverloadedStrings #-}

import Data.Graph
import Data.Array
import Data.List (sortBy)
import Data.Maybe (fromMaybe)
import Data.Ord (comparing)

-- Define a type for tasks
data Task = Task
    { name :: String
    , priority :: Int
    , dread :: Int
    } deriving (Eq, Show)

type Dependency = (String, String)

-- Create a graph from tasks and their dependencies
buildGraph :: [Task] -> [Dependency] -> (Graph, Vertex -> (String, Task, [String]), String -> Maybe Vertex)
buildGraph tasks deps =
    let
        taskTuples = [(name task, task, dependents (name task)) | task <- tasks]
        dependents taskName = [b | (a, b) <- deps, a == taskName]
    in
        graphFromEdges taskTuples

-- Topologically sort tasks while respecting dependency constraints
topologicalSort :: [Task] -> [Dependency] -> Either String [Task]
topologicalSort tasks deps =
    let
        (graph, nodeFromVertex, vertexFromKey) = buildGraph tasks deps
        sortedVertices = topSort graph
        sortedTasks = map (\v -> let (_, task, _) = nodeFromVertex v in task) sortedVertices
    in
        if null sortedVertices
        then Left "There is a cycle in the task dependencies."
        else Right sortedTasks

-- Stable sort tasks by priority and dread in descending order
sortByAttributes :: [Task] -> [Task]
sortByAttributes = sortBy (comparing (negate . priority) <> comparing (negate . dread))

main :: IO ()
main = do
    let tasks =
            [ Task "task1" 3 2
            , Task "task2" 1 5
            , Task "task3" 2 3
            , Task "task4" 2 4
            ]
    let dependencies = [("task1", "task2"), ("task2", "task3"), ("task1", "task3"), ("task3", "task4")]

    case topologicalSort tasks dependencies of
        Left err -> putStrLn $ "Error: " ++ err
        Right sortedTasks -> do
            let finalSortedTasks = sortByAttributes sortedTasks
            putStrLn "Sorted tasks by dependencies, then by priority and dread:"
            mapM_ print finalSortedTasks
```

Explanation:

1 - Task Definition:

Define the Task type with fields for name, priority, and dread.

2 - Building the Graph:

buildGraph remains similar to the previous implementation but now works with the Task type that includes additional attributes.

3 - Topological Sort:

topologicalSort function performs the topological sort based on the dependencies. It returns a list of tasks in topological order.

4 - Sorting by Attributes:

sortByAttributes function sorts the list of tasks by priority and dread in descending order using comparing and negate to achieve the desired order.

5 - Main Function:

* The main function defines a list of tasks and dependencies.
* It first calls topologicalSort to get the tasks in topological order.
* Then it calls sortByAttributes to sort the tasks within the topological order by priority and * dread.
* Finally, it prints the sorted tasks.

Notes:

* The use of comparing (negate . priority) <> comparing (negate . dread) in sortByAttributes ensures that the tasks are sorted in descending order of priority and dread.
* This approach respects the dependency constraints by ensuring that the topological sort is performed first, and then stable sorting is used for priority and dread without breaking the topological order.
* This code ensures that dependency constraints have the highest precedence, while within those constraints, tasks are ordered by priority and dread in descending order.

Me: The problem with the above approach is that it would simply re-sort the list without regard to dependency constraints. I need to first sort on priority and dread, and then do a topological sort on dependencies in a way that would preserve the original sorting everywhere except where dependencies dictate otherwise.

To address the requirement of sorting by priority and dread while preserving the dependency constraints, we need to use a custom topological sorting approach that respects the initial sorting order as much as possible. Here's how you can achieve this:

1. Sort the tasks initially by priority and dread.
2. Perform a topological sort, using the initial sorted order to break ties.

This way, the initial sort order is preserved everywhere except where dependencies dictate otherwise.

Here's the implementation:

``` haskell
{-# LANGUAGE OverloadedStrings #-}

import Data.Graph
import Data.Array
import Data.List (sortBy, nub, partition)
import Data.Maybe (fromMaybe)
import Data.Ord (comparing)
import qualified Data.Map.Strict as Map
import qualified Data.Set as Set

-- Define a type for tasks
data Task = Task
    { name :: String
    , priority :: Int
    , dread :: Int
    } deriving (Eq, Show)

type Dependency = (String, String)

-- Function to build a graph from tasks and dependencies
buildGraph :: [Task] -> [Dependency] -> (Graph, Vertex -> (String, Task, [String]), String -> Maybe Vertex)
buildGraph tasks deps =
    let
        taskTuples = [(name task, task, dependents (name task)) | task <- tasks]
        dependents taskName = [b | (a, b) <- deps, a == taskName]
    in
        graphFromEdges taskTuples

-- Custom topological sort that respects the initial order for tie-breaking
customTopologicalSort :: [Task] -> [Dependency] -> Either String [Task]
customTopologicalSort tasks deps =
    let
        (graph, nodeFromVertex, vertexFromKey) = buildGraph tasks deps
        initialOrder = Map.fromList (zip (map name tasks) [0..])
        sortVertices vs = sortBy (comparing (\v -> Map.findWithDefault maxBound (vertexToName v) initialOrder)) vs
        vertexToName v = let (name, _, _) = nodeFromVertex v in name
        sortedVertices = topSort' graph sortVertices
        sortedTasks = map (\v -> let (_, task, _) = nodeFromVertex v in task) sortedVertices
    in
        if null sortedVertices
        then Left "There is a cycle in the task dependencies."
        else Right sortedTasks

-- Custom topological sort function with tie-breaking
topSort' :: Graph -> ([Vertex] -> [Vertex]) -> [Vertex]
topSort' g sortVertices = go [] (Set.fromList [v | v <- vertices g, indegree g ! v == 0])
  where
    go acc sources
        | Set.null sources = reverse acc
        | otherwise =
            let (v, sources') = pickSource sources
                newSources = foldr (\w -> Set.insert w . Set.delete w) sources' (g!v)
            in go (v : acc) newSources

    pickSource sources =
        let sortedSources = sortVertices (Set.toList sources)
        in (head sortedSources, Set.delete (head sortedSources) sources)

main :: IO ()
main = do
    let tasks =
            [ Task "task1" 3 2
            , Task "task2" 1 5
            , Task "task3" 2 3
            , Task "task4" 2 4
            ]
    let dependencies = [("task1", "task2"), ("task2", "task3"), ("task1", "task3"), ("task3", "task4")]

    case customTopologicalSort (sortByAttributes tasks) dependencies of
        Left err -> putStrLn $ "Error: " ++ err
        Right sortedTasks -> do
            putStrLn "Sorted tasks by dependencies, then by priority and dread:"
            mapM_ print sortedTasks

-- Stable sort tasks by priority and dread in descending order
sortByAttributes :: [Task] -> [Task]
sortByAttributes = sortBy (comparing (negate . priority) <> comparing (negate . dread))
```

Explanation:

1. Task Definition:
   * The Task type includes name, priority, and dread.

2. Initial Sorting:
   * The sortByAttributes function sorts tasks by priority and dread in descending order.

3. Graph Construction:
   * The buildGraph function constructs the graph from tasks and dependencies.

4. Custom Topological Sort:
   * The customTopologicalSort function performs a topological sort that respects the initial sorted order.
   * sortVertices is a function that sorts vertices based on their initial order.
   * topSort' is a modified version of the topological sort that uses sortVertices to break ties when selecting the next vertex.

5. Main Function:
   * The main function defines tasks and dependencies, sorts tasks by attributes, and then performs the custom topological sort. It prints the sorted tasks.

Notes:

* This approach first sorts the tasks by priority and dread.
* During the topological sort, it respects the initial order to break ties, ensuring that dependencies are satisfied while maintaining the order as much as possible.
* This method avoids re-sorting the entire list without regard to dependencies, preserving the initial sorting where possible.

#### Further Reading

* [Topological Sort in Haskell](https://stackoverflow.com/questions/21675925/topological-sort-in-haskell)

### Scheduling

Possibly use Prolog/Datalog for constraint solving and schedule finding?

calendar is direct parent of schedules, containing appointments and day parameters -> calendar folder containing a file for each day

calendar is counterpart to plan, containing tasks (but one-off, non-derivable) -> adhoc folder containing a file for each day

* Scheduling Features
  * fixed entries (x.ismovable)
  * ordering of entries (x.order)
  * iterative compression according to priority
  * category blocks and entry categories:
  * strict: work task only during blocked work hours
  * non-strict: work task goes to work if available, otherwise scheduled as a normal task
  * rewrite ad hoc file format to allow task specification by names (or other attribute, perhaps) → include fuzzy search with minimum string similarity (?) for name & other attributes
  * TODO: make it so that fixed events can also be resized
  * use name optionally instead of .block attribute?
  * fix entry adding to allow for ‘flow’ around fixed items
  * implement ‘snapping’ logic when the gap between tasks is small
  * how to measure performance and execution time, visualizing each function call?
  * move some functions from …algorithms.scheduling into the Schedule class ✓

  * fixed entries: `e.ismutable == False`

* Scheduling and prioritization
  * blocks added automatically: routines and recurring tasks
  * blocks added manually (weekly and daily planning)
  * automatic filling in of tasks according to algorithm
  * manual editing of task schedulng
  * Scheduling Algorithm (Vanilla)

* High-level description:

  1. A base schedule is specified in the calendar, which contains default recurring activities.
  2. From planning (typically quarterly and weekly), non-recurring "big rock" activities are added, each with a priority level that determines which takes precedence among a set of items competing for the same time.
  3. From the store of long-term roadmaps and projects and their corresponding tasks, tasks are assigned according to schedule and priority.
  4. When there are conflicts or too many tasks to fit in the available time, these are to be resolved first automatically according to the settings.

    The irresoluble conflicts or overloads are then resolved manually, but only by editing the declarations, upon which the schedule is recomputed.

* Low-level description of scheduling algorithm:

    1. check whether the entries fit in a day
    2. get the compression factor, i.e. how much, on average, the entries need to be compacted in order to fit
    3. separate entries into fixed (immovable) and flex (movable)
    4. add the fixed entried to the schedule
    5. identify the gaps
    6. fill in the gaps with the flex items TODO
    7. resize between fixed points to remove small empty patches (where possible)

TODO: add `alignend` functionality (but first get it working without)

* ( ) [medium.com/@thegapfill/productivity-article-eb1df36d4dbf](https://medium.com/@thegapfill/productivity-article-eb1df36d4dbf) 
* ( ) [researchgate.net/publication/341780522_task_scheduling_in_cloud_computing_a_survey/link/5f37b224458515b729221960/download](https://www.researchgate.net/publication/341780522_Task_Scheduling_in_Cloud_Computing_A_Survey/link/5f37b224458515b729221960/download)
* ( ) [algorithms for scheduling problems](http://library.lol/main/5E75C506698832A19DCF51915EA014A4)
* ( ) [researchgate.net/publication/337148981_planning_and_scheduling_problems_of_production_systems_review_classification_and_opportunities](https://www.researchgate.net/publication/337148981_Planning_and_scheduling_problems_of_production_systems_review_classification_and_opportunities) → file:///home/isaac/Downloads/R5_IJPQM_05November19_IBNMAJDOUZINEB_PlanningandschedulingproblemsofproductionsystemsReview.pdf
* ( ) [tutorialspoint.com/operating_system/os_process_scheduling_algorithms.htm](https://www.tutorialspoint.com/operating_system/os_process_scheduling_algorithms.htm)
* ( ) [academia.edu/6718638/scheduling_problems_an_overview](https://www.academia.edu/6718638/Scheduling_problems_An_overview)
* ( ) [types of task scheduling algorithms in cloud computing environment](https://www.intechopen.com/chapters/71902)
* ( ) [natural intelligence for scheduling, planning and packing problems *[1 ed.]](http://libgen.rs/book/index.php?md5=9BC05329D09109CF82B0FB7386889764)*
* ( ) [decision analysis, location models, and scheduling problems *[1 ed.]*](http://libgen.rs/book/index.php?md5=805513A81A24B94975F802FE4F3C2ECF)
* ( ) [constraint-based scheduling: applying constraint programming to scheduling problems *[1 ed.]*](http://libgen.rs/book/index.php?md5=9D333284F1AF9D661620AD274CF113B7)
* ( ) [web-static.stern.nyu.edu/om/faculty/pinedo/scheduling/sched.pdf](https://web-static.stern.nyu.edu/om/faculty/pinedo/scheduling/sched.pdf)
* ( ) [javatpoint.com/activity-or-task-scheduling-problem](https://www.javatpoint.com/activity-or-task-scheduling-problem)
* ( ) [teamdoapp.com/inspiration/increase-productivity-with-effective-task-scheduling](https://teamdoapp.com/inspiration/increase-productivity-with-effective-task-scheduling/)
* ( ) [machine learning and optimization for production rescheduling in industry 4.0](https://link.springer.com/article/10.1007/s00170-020-05850-5)

#### Entry Adding Cases

* ( ) empty
* ( ) adding movable over empty
* ( ) adding immovable over empty
* ( ) add movable over empty, near other task, forcing snap: movable before movable,
* ( ) add movable over empty, near other task, forcing snap: movable after movable
* ( ) add movable over empty, near other task, forcing snap: movable on movable
* ( ) add movable over empty, near other task, forcing snap: immovable before movable
* ( ) add movable over empty, near other task, forcing snap: immovable after movable
* ( ) add movable over empty, near other task, forcing snap: immovable on movable
* ( ) add immovable over empty, near other task, forcing snap: movable before movable,
* ( ) add immovable over empty, near other task, forcing snap: movable after movable
* ( ) add immovable over empty, near other task, forcing snap: movable on movable
* ( ) add immovable over empty, near other task, forcing snap: immovable before movable
* ( ) add immovable over empty, near other task, forcing snap: immovable after movable
* ( ) add immovable over empty, near other task, forcing snap: immovable on movable
* ( ) add movable over empty, near other task, forcing no snap: movable before movable,
* ( ) add movable over empty, near other task, forcing no snap: movable after movable
* ( ) add movable over empty, near other task, forcing no snap: movable on movable
* ( ) add movable over empty, near other task, forcing no snap: immovable before movable
* ( ) add movable over empty, near other task, forcing no snap: immovable after movable
* ( ) add movable over empty, near other task, forcing no snap: immovable on movable
* ( ) add immovable over empty, near other task, forcing no snap: movable before movable,
* ( ) add immovable over empty, near other task, forcing no snap: movable after movable
* ( ) add immovable over empty, near other task, forcing no snap: movable on movable
* ( ) add immovable over empty, near other task, forcing no snap: immovable before movable
* ( ) add immovable over empty, near other task, forcing no snap: immovable after movable
* ( ) add immovable over empty, near other task, forcing no snap: immovable on movable
* ( ) add movable over movable, near other task, forcing snap: movable before movable,
* ( ) add movable over movable near other task, forcing snap: movable after movable
* ( ) add movable over movable near other task, forcing snap: movable on movable
* ( ) add movable over movable near other task, forcing snap: immovable before movable
* ( ) add movable over movable near other task, forcing snap: immovable after movable
* ( ) add movable over movable near other task, forcing snap: immovable on movable
* ( ) add immovable over movable near other task, forcing snap: movable before movable,
* ( ) add immovable over movable near other task, forcing snap: movable after movable
* ( ) add immovable over movable near other task, forcing snap: movable on movable
* ( ) add immovable over movable near other task, forcing snap: immovable before movable
* ( ) add immovable over movable near other task, forcing snap: immovable after movable
* ( ) add immovable over movable near other task, forcing snap: immovable on movable
* ( ) add movable over movable near other task, forcing no snap: movable before movable,
* ( ) add movable over movable near other task, forcing no snap: movable after movable
* ( ) add movable over movable near other task, forcing no snap: movable on movable
* ( ) add movable over movable near other task, forcing no snap: immovable before movable
* ( ) add movable over movable near other task, forcing no snap: immovable after movable
* ( ) add movable over movable near other task, forcing no snap: immovable on movable
* ( ) add immovable over movable near other task, forcing no snap: movable before movable,
* ( ) add immovable over movable near other task, forcing no snap: movable after movable
* ( ) add immovable over movable near other task, forcing no snap: movable on movable
* ( ) add immovable over movable near other task, forcing no snap: immovable before movable
* ( ) add immovable over movable near other task, forcing no snap: immovable after movable
* ( ) add immovable over movable near other task, forcing no snap: immovable on movable
* ( ) add movable over immovable, near other task, forcing snap: movable before movable,
* ( ) add movable over immovable near other task, forcing snap: movable after movable
* ( ) add movable over immovable near other task, forcing snap: movable on movable
* ( ) add movable over immovable near other task, forcing snap: immovable before movable
* ( ) add movable over immovable near other task, forcing snap: immovable after movable
* ( ) add movable over immovable near other task, forcing snap: immovable on movable
* ( ) add immovable over immovable near other task, forcing snap: movable before movable,
* ( ) add immovable over immovable near other task, forcing snap: movable after movable
* ( ) add immovable over immovable near other task, forcing snap: movable on movable
* ( ) add immovable over immovable near other task, forcing snap: immovable before movable
* ( ) add immovable over immovable near other task, forcing snap: immovable after movable
* ( ) add immovable over immovable near other task, forcing snap: immovable on movable
* ( ) add movable over immovable near other task, forcing no snap: movable before movable,
* ( ) add movable over immovable near other task, forcing no snap: movable after movable
* ( ) add movable over immovable near other task, forcing no snap: movable on movable
* ( ) add movable over immovable near other task, forcing no snap: immovable before movable
* ( ) add movable over immovable near other task, forcing no snap: immovable after movable
* ( ) add movable over immovable near other task, forcing no snap: immovable on movable
* ( ) add immovable over immovable near other task, forcing no snap: movable before movable,
* ( ) add immovable over immovable near other task, forcing no snap: movable after movable
* ( ) add immovable over immovable near other task, forcing no snap: movable on movable
* ( ) add immovable over immovable near other task, forcing no snap: immovable before movable
* ( ) add immovable over immovable near other task, forcing no snap: immovable after movable
* ( ) add immovable over immovable near other task, forcing no snap: immovable on movable
* ( ) impossible: any over saturated day
* ( ) impossible: any on day without enough room
* ( ) impossible: immovable on top of immovable

## Tracking

* pre-programmed (still configurable) for:
* food & drink, workout, finances (expenditures), adherence to schedule/time use
* -> need to access goals via plan
* add earliest and latest start and end for each level of the roadmap-project-task hierarchy
* tracking: collect texting statistics

* Habits to track:
  * all foods (with times)
  * time breaking fast
  * last time eating
  * bool: entirely plant-based? entirely non-processed?
  * food score
  * cold shower
  * daily walk (5x/week)
  * run (5x/week) - with recorded data
  * sets of pushups
  * sets of pullups
  * stretching
  * wisdom literature
  * last use of phone
  * number of texts sent
  * emails clean? (both) bookmarks clean?
  * journal
  * cleanliness & orderliness of apartment
  * bool: mast.
  * time doing absolutely nothing
  * quality of meditation
  * something new I learned
  * which languages I used
* Habits / metrics to track:
  * all foods (with times)
  * time breaking fast
  * last time eating
  * bool: entirely plant-based? entirely non-processed?
  * food score
  * cold shower
  * daily walk (5x/week)
  * run (5x/week) - with recorded data
  * sets of pushups
  * sets of pullups
  * stretching
  * wisdom literature
  * last use of phone
  * number of texts sent
  * emails clean? (both) bookmarks clean?
  * journal
  * cleanliness & orderliness of apartment
  * bool: mast
  * 30 minutes doing absolutely nothing
  * bool: getting lost in a good book
  * quality of meditation
  * something new I learned
  * which languages I used
* TRACKING:
 manually via neorg, or via semaphore. One file per metric for easy
* tracking; move dates more than 30 days old to the old store (more
* efficient format?)

## Apps

```txt

AppFlowy is a web application, which means that you can use it on any device that has a web browser. To host it so that you can use it on your Android device and desktop, there are a few options:

1. Host it on a server and access it through a web browser on your desktop and Android device: You can host AppFlowy on a server and access it through a web browser on your desktop or Android device. This way, you can use AppFlowy on any device that has a web browser.
2. Install a local server on your desktop and access it through a web browser on your desktop and Android device: You can install a local server on your desktop and access AppFlowy through a web browser on your desktop or Android device. This way, you can use AppFlowy on your desktop without an internet connection, and access it on your Android device through a local network.
3. Use a cloud-based service that allows you to host web applications: There are several cloud-based services, such as AWS, DigitalOcean, and Heroku, that allow you to host web applications. You can host AppFlowy on one of these services and access it through a web browser on your desktop or Android device. This way, you can use AppFlowy on any device that has a web browser, and you don't need to worry about managing a server.

Regardless of which option you choose, it's important to make sure that you keep your AppFlowy account secure by using a strong and unique password, and enabling two-factor authentication if possible.

search “hosting” [discord.com/channels/903549834160635914/903553722804748309](https://discord.com/channels/903549834160635914/903553722804748309)
```

### Android App Development

* ( ) [kivy.org/doc/stable/guide/packaging-android.html](https://kivy.org/doc/stable/guide/packaging-android.html) (also suitable for desktop)

### AppFlowy

* ( ) [appflowy-io/appflowy/issues/3125](https://github.com/AppFlowy-IO/AppFlowy/issues/3125)
* ( ) Which conversions are necessary?
* ( ) Which modules do I need to write? How can I minimize redundancies while maintaining flexibility and extensibility?
* ( ) Which off-the-shelf solutions exist already?
* ( ) rofi integration
* ( ) polybar integration
* ( ) What will be the APIs of the modules?
* ( ) Which programming languages will I use for each module?
* ( ) try to run signald in a docker container
* ( ) read semaphore docs and read through examples
* ( ) → eventually add neorg - anki interface
* ( ) Add purity checks (i.e. no side effects) to tests
* ( ) Improve serialization for copying
* ( ) a.to_{x}() and a.from_{x}() should be perfect inverses → add to tests
* ( ) figure out how to add norg support to a fork of AppFlowy
* ( ) How to connect flutter app to backend? → Look at AppFlowy & its Private Cloud when it is released soon
* ( ) How to make planager server for AppFlowy?
* ( ) Django or Flask (or FastAPI) for first iteration?
* ( ) dead tree Rust book in German → roadmaps
* ( ) → Implement scheduling module in polyglot-projects, also corresponding visualizer
* ( ) TRACKING: manually via neorg, or via semaphore. One file per metric for easy tracking; move dates more than 30 days old to the old store (more efficient format?)
* ( ) [packaging.python.org/en/latest/guides/creating-and-discovering-plugins](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)

## Server, Sync, Multi-Device, Etc

* possible to have app server and website server on same server VM?
* sync
  * preferred method: manual sync
* Features for quick updates
  * object dependency graph to only make necessary changes, depending on what has changed
  * automatic patch generation from edits → ‘reverse engineering’ of effects, almost analogous to backpropagation of desired changes
    * Use norg link structure to track which files need to be updated?
    * Declarative schedule generation:
  * directed graph for updates, acyclical for full recompute, but not necessarily acyclical for some updates: lower-level (e.g. schedule, task) edit may trigger necessary change at parent levels (tasks, projects)
* storage
  * What is stored where and in which format?
    1. taskwarrior database
    2. notion frontend
    3. ganttouchthis store - on desktop, mobile, and server, with git backup
  * consistent & readable storage format → seamless integration with .norg files
* Hooks
  * hooks to trigger updates: [neovim.io/doc/user/autocmd.html#events](https://neovim.io/doc/user/autocmd.html#events)
  * What are the hooks? I.e., which events trigger a sync from which component to which component?
        1. planning session defines projects, which are parsed into tasks and scheduled
        2. tasks are added to taskwarrior and synced to the server
        3. server sends mobile notifications according to schedule
        4. opening a relevant norg file results in pulling tasks from the taskwarrior database
        5. writing a tracked norg file results in pushing tasks back to the taskwarrior database and a sync with the server
        6. editing elsewhere triggers a sync with Notion; pulling from another app triggers a sync pulling from Notion, with optional manual trigger to sync with Notion

### Signal Integration TODO: CLEANUP

* Signal module:

    dependencies:

  * planager.tracking
  * planager.schedule
  * semaphore (Python package)
* Signal bot requirements → different chats or all-in-one?
    1. notify of start/end of schedule entries
    2. record (as response to prompts) status of tasks, incl. sub-items of routines
    3. accept request to edit declaration files, then edit & trigger recompute
    4. display (upon query) some (subset of) roadmap, plan, task, schedule, etc.
    5. show tracker information: streaks, percentage, habit strength, progress toward goals, …

### Server Books

* [Web Hosting For Dummies](http://library.lol/main/15AB02F5EE821874E1269F1C1A2C6466)
* [Linux Server Cookbook: Get Hands-on Recipes to Install, Configure, and Administer a Linux Server Effectively](http://library.lol/main/A9EC0C8B28BC4409DF0AF7BC266F92AC)
* [KISS Server Virtualization: Server Virtualization](http://library.lol/main/DEA763D00B5C1FB74043E8B792C019C9)
* [Linux-Server: Das umfassende Handbuch](http://library.lol/main/F438A58DB4F0B06E7B795598648C1F5E)
* [Mastering Ubuntu Server: Explore the versatile, powerful Linux Server distribution Ubuntu 22.04 with this comprehensive guide](http://library.lol/main/7AFB83DF3236E59C71A4F469A91CDB2B)
* [Set Up And Manage Your Virtual Private Server: Making System Administration Accessible To Professionals](http://library.lol/main/35C22818EAE9FA0FA5CA4D00C70F3262)
* [Practical Internet Server Configuration: Learn to Build a Fully Functional and Well-Secured Enterprise Class Internet Server](http://library.lol/main/6662ADAF65D4E07828DEC10CD80FD4E0)
* [Private Cloud und Home Server mit QNAP NAS Das umfassende Praxis-Handbuch](http://library.lol/main/3926305C3E5A96DCB6245A105FD9841D)
* [Common Windows, Linux and Web Server Systems Hacking Techniques](http://library.lol/main/C055ADFA562BFC22E8F23D143143957C)
* [Ansible for DevOps: Server and configuration management for humans](http://library.lol/main/F4488432BBABE7E63112A08B611E2CE0)
* [Mastering Linux security and hardening: secure your Linux server and protect it from intruders, malware attacks, and other external threats](http://library.lol/main/C835450F069C3CCB1A7EE90F765CA7EF)
* [Linux-Server Das umfassende Handbuch](http://library.lol/main/EE8242C91DF7F7CC3A836B98684BD222)
* [Linux Server Hacks, 2: Tips & Tools for Connecting, Monitoring, and Troubleshooting](http://library.lol/main/D77D0EBB208E89EBCF4C10F7FF64B35E)
* [Linux Server Linux Server Hacks: Los Mejores Trucos the Best Tricks](http://library.lol/main/D65668D1220B40901544827FC45CC753)
* [Linux Email. Set Up and Run a Small Office Email Server](http://library.lol/main/F2C6BA1A73A964710CB697A968518891)

## Ganttouchthis / Ganttstop

* change GTT to write only changed tasks / projects / days, but keep in-memory for speed (except backlog and done; unnecessary)
  * crystalize gtt API, database format, object API
  * GTT functionality: add project, edit project, edit task -> done to done DB, project from backlog, add to backlog, adjust task distribution: balanced|rollover|rigid, edit backlog item, project from backlog item, check validity & check data consistency (in memory & in database & between memory and database), exact & fuzzy search, TUI, export as SVG
  
## Kanban View

* can a Kanban board be combined with my system -> integrate as a view of the tasks
* Personal Kanban

## Data Formats

### JSON-Based

* Nebokrai declaration types:
  * config
  * roadmaps
  * routines
  * tracking (-> journaling)
  * calendar
* Nebokrai derivation types:
  * plan
  * schedule
  * journal
* [Taskwarrior JSON](https://github.com/GothenburgBitFactory/taskwarrior/blob/develop/doc/devel/rfcs/task.md)
  -> [export](https://taskwarrior.org/docs/commands/export/)

### Garmin: FIT, GPX, TCX

* [FIT](https://developer.garmin.com/fit/overview/)
* [GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format)
* [TCX](https://en.wikipedia.org/wiki/Training_Center_XML)

### Standards: WebDAV, CalDAV, iCalendar

* [vdir](https://vdirsyncer.readthedocs.io/en/latest/vdir.html)
* [CalDAV](https://en.wikipedia.org/wiki/CalDAV)
* [WebDAV](https://en.wikipedia.org/wiki/WebDAV)
* [iCalendar](https://en.wikipedia.org/wiki/ICalendar)
* [CardDAV](...)
* [vObject](...)
* [.ics](...)
* [read](https://en.wikipedia.org/wiki/Comparison_of_CalDAV_and_CardDAV_implementations)

## Data Conversion

### Converter Project

Idea: Write a Taskwarrior/Timewarrior data conversion util for conversion to and from all relevant data formats:

* JSON
* YAML
* TOML
* Markdown
* Norg
* CSV
* RON
* Dhall
* KDL
* HCL
* CalDAV
* WebDAV
* todo.txt
* \[x\]it!
* org
* LaTeX (variety of templates)
* Typst (variety of templates)
