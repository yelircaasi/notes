# Server, Sync, Multi-Device, Etc

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

FIXME### Signal Integration TODO: CLEANUP

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
