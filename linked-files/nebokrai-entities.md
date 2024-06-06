# Entities

* old: Entity Types
  * roadmap: a 'master plan' for some area such as 'Rust programing language' or 'muscular flexibility' involving multiple steps or projects
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

## Tasks

* Task definition entry points:
  * nvim
  * command line
  * Notion (check API and pull following trigger)
  * Task definition types:
  * from project creation
  * from project editing
  * manual add
