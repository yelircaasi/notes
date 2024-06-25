# Nebokrai Tracking

## Tracking

To understand what is working and what is not, it is important to have a clear record of what
actually happened. As psychological studies have shown, memory is often unreliable and deceptive.
Without data, I can easily overestimate the extent to which I have eaten healthily or the amount of
time I spent actually working on projects (with my brain engaged, not just sitting in the right
chair). Activity tracking is the antidote to these problems.

On the other hand, tracking is tedious, and in many forms it is quite burdensome. Any system
attempting to facilitate tracking needs to mitigate this. An easy interactive CLI and a mobile
interface via the Signal app (and later others) are two approaches that make tracking if not
outright enjoyable, at least more pleasant and less of a chore.

## Details

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

## Tracking ==========================================================================

Currently, the tracking is fully defined from primitives in the declaration. This has
the advantage of generality, but it is probably worth adding some classes to the source
for complex and idiosynchratic tracking tasks: WorkoutTracker, NutritionTracker,
FinanceTracker (?), TimeTracker (?) (for general time tracking), especially
where these might need to interact with the derivation to access goals from the plan.

## Full List (in progress)

* Morning Routine
* Midday Routine
* Evening Routine
* Subjective Evaluation (per hour or k key points throughout the day) -> integrate with character attributes
* food and drink
* physical activity
* number of messages sent by platform
* financial activity (integrate with hledger)
