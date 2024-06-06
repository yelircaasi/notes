# Nebokrai Planning Notes

## Planning

In keeping with the principle 'Begin with the end in mind' - it is beneficial to set long-term
goals, as it guides short- and medium-term action. To this end, nebokrai specifies a hierarchy of
units:

* roadmaps consist of projects
* projects consist of tasks
* tasks are self.contained atomic units

Conversely, each task belongs to a project, which in turn belongs to a roadmap. This child-parent
relationship ensures context, which is useful in keeping an overview of the system as a whole.

Each unit has a number of properties (more on this later). Every child unit
inherits by default from its parent. For example, unless otherwise specified in the declaration,
a task has the same priority as the project to which it belongs.

Roadmaps as well as projects can specify attributes relating to timing, such as start time, end
time, cluster size (how many tasks from the given project to group together as a single unit),
desired interval, etc. Of course, only a subset of all possible combinations are valid.
Based on the declaration provided, including configuration parameters and the calendar ('big rock'
entries such as work or ad hoc appointments, routines, and other attributes relevant to planning
and scheduling), the algorithm then assigns each task to a day. This is good
for Gantt-style visualization, for example:

{example here}

Planning in this way is also a good way to make sure that the long-term objectives are realistic
within the constraints provided. If the total duration of all tasks is simply too great, the
declaration will fail. This is desirable: early failure during compilation is always preferrable
to failure later during  deployment.

This implies an iterative planning process. I declare roadmaps, projects, and tasks along with a
calendar and configuration parameters. Then nebokrai either allocates tasks to days, or informs
me that I cannot and provides helpful information as to why the declaration was impossible to
realize. I then remedy the offending parts of the declaration and repeat the process until I have a
feasible plan.

## Specific Details

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

FIXME#### Dependency Sorting

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

FIXME#### Further Reading

* [Topological Sort in Haskell](https://stackoverflow.com/questions/21675925/topological-sort-in-haskell)

## Planning ========================================================================

For flex entries, planning should take into account some combination of:

* priority
* goodness
* badness (or simply derive priority from goodness and badness?)
* normal time
* ideal time
* min time
* max time
* dependencies (rename to blockers?)
* composability of entries to add subtasks to blocks

Potential other features:

* earliest date
* latest date
* dread (i.e. opposite of how fun it is)
* strain/strenuousness,

It may also make sense to add more complex planning modules, for things like meal
planning and workout planning.

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
