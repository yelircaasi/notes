# Nebokrai Scheduling Notes

## Scheduling

From the plan, the next step is to create a schedule. Algorithmically, this turns out to be more
involved - see [this](...) for details and discussion. The general process is as follows:

1. Entries are defined in the calendar or created from tasks in the plan.
2. Entries are added to days in order of priority such that all constraints are satisfied.
3. Entry times are adjusted such that they partition the available time.

Constraint types include:

* blocks and categories: entries may have block or category names specified, such as 'work' or
  'transit', where an entry can be scheduled within another entry, such as work-related tasks (i.e.
  tasks bearing the 'work' category tag) being scheduled inside an entry with the block tag 'work',
  which is a nebokrai-specific way of saying that work-related activities are scheduled during
  work hours
* categories can be binding or non-binding, where binding categories may be scheduled _exclusively_
  inside entries with the corresponding block tag, whereas a non-binding category allows scheduling
  inside or outside such entries
* entries can be fixed or movable (i.e. fixed start, fixed end), as can start and end times
* entries have an `order` attribute between 0 and 100, where 0 means 'put me as early as possible
  and 100 says 'put me as late as possible'. The numbers are purely relative; their absolute
  magnitude has no meaning.
* entries may have earliest/latest start/end times (4 combinations)

The scheduler acts as a sort of temporal constraint solver to find the optimal schedule satisfying
the declaration and (more immediately) the plan.

One of the major benefits of planning in this way is the built-in-by-design requirement that
priorities are respected when planning. For example, routines can be declared in their own section
of the declaration, referenced on relevant days in the calendar, and then included in planning and
scheduling. To borrow yet another phrase from computer science, this is a sort of ahead-of-time
compilation, which makes possible a high degree of optimization.

## Implementation Details

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
  2. From planning (typically quarterly and weekly), non-recurring 'big rock' activities are added, each with a priority level that determines which takes precedence among a set of items competing for the same time.
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

## Scheduling ========================================================================

Scheduling takes into account what is already scheduled and fixed, as well as
what can be added to what. For flex entries (and among subtasks in the same
block), ordering is determined by:

* priority (optionally omitted in favor of goodness and badness)
* dread
* strenuousness
* normaltime
* idealtime
* mintime
* maxtime
*

This allows me to conform to the principle 'eat your frogs first', i.e. get unpleasant
important tasks out of the way first to avoid procrastination.

## Entry Adding

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

## Scratch

Add property `fuidity` to determine which entries to split up first (0, 1, 2, 3, 4) or (1, 2, 3, 4, 5)

Scheduling:

1. Start with CalDay: all fixed appointments
2. Sort entries according to config, e.g.: f(priority, dread)
3. Assert that time entries fit
4. Add entries one-by-one, finding first suitable slot
   * first search available blocks, then unblocked
   * first search slots that don't require splitting

```haskell
FreeSlots :: map BlockName Int

getFreeSlots :: CalDay -> FreeSlots

getFirstSlot :: FreeSlots -> TimeSlot

addEntries :: Schedule -> [Entry] -> Schedule
addEntries initialEntries entries = foldl addEntry initialSchedule entries

getOverlapping :: Span -> [Span] -> [Span]

addEntry schedule entry = ...
```

Cases:

1. Entry fits in block: add to block
2. Get all candidates (based on earliest & latest) -> see getOverlapping
3. Add according to orderScore (derivedOrder), and return (newSchedule, remainingEntries) if entry fits; otherwise select most fluid entry
4. Repeat until full
5. Optimize schedule: make small adjustments to improve certain desirable metrics (qualities of the schedule)
