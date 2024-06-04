# Nebokrai Discussion on Discord

* [link to dicsussion on Discord](https://discord.com/channels/834325286664929280/877666474888675368/1222613062796705862)

Can I workshop an idea with you people? Seems like as good a place as any

Vhyrro: yeah sure why not

yelircaasi: The basic idea, one I have sloppily prototyped in Python and am now re-writing in Haskell (because of course), is "pure functional personal planning and scheduling"

Declare a calendar with ad hoc entries and (the interesting part) roadmaps consisting of projects consisting in turn of tasks. Then the program derives a plan (mapping task -> day) and from there a schedule (mapping task -> entry -> time) according to parameters declared, such as priority, blockers, and estimated min/normal/max time per task, fixedness/flexness etc.

This will be compatible with existing tools like neorg::gtd, taskwarrior, xit, etc. But the mechanism for enforcing coherence between long-term goals and day-to-day plans is something I haven't found elsewhere. And for a certain personality type (mine, but presumably not uncommon among programmers) this sort of thing helps a lot with motivation

Vhyrro: Lowkey sounds like something I've also been conjuring up :kek:

The initial idea was to be able to specify an estimated time for each task, and allow a system to sort and organize based on time taken

with the idea of it also being able to adapt to certain behaviours to be more accurate

yelircaasi: I had looked around extensively and not found anythng that solves this problem. It's important to me not to needlessly duplicated existing work, but this really seems to be a gap that needs filling

pysan3: Is this talking about team task or personal tasks?

Vhyrro: both honestly

yelircaasi: I'm focused on individual tasks, but I'm sure the principle could be applied to teams as well

Vhyrro: Just like the link integrity, I was thinking of some foundation for linking between atomic data like tasks

projects are just groups of tasks with an optional title

I'll not be working on that for a long while though, so let your ideas run wild. If you figure out anything groundbreaking we could adopt it for sure!

pysan3: Am I correct imaging the output to be something similar to a gantt chart?

yelircaasi: the canonical example for me is, say you have 20 books you want to read in the next two years. Certain books are more important, certain should be read before others (the blocker principle I mentioned). And it would be nice to have a tool to automatically create this

Vhyrro: In my case I was thinking of a multidimensional calendar (<https://julian.digital/2023/07/06/multi-layered-calendars/>)

julian.digital

julian

Multi-layered calendars

Calendars cover the entire spectrum of time. Past, present and future. They are the closest thing we have to a time machine. Calendars allow us to travel forward in time and see the future. More importantly, they allow us to change the future.

Multi-layered calendars

yelircaasi: Yes, that's actually how this started. At sone point, Gantt charts were too inflexible, and having to push everything back by hand grew tiresome (because as we know, pufe happens)

Vhyrro: multi layered calendars are also a super cool concept which Sevoris pointed me at

yet again, an idea I had but just much more rigorously planned out by this lad before me :kek:

yelircaasi: That's really cool, definitely in the same vein.

My hope is to have the project sketched out in generously-commented haskell in the next few weeks, so that the logic of planning and scheduling is easy to read and  reason about

Vhyrro: your idea sounds super cool so yeah do it man

pysan3: This is cool. I mean I always wanted the BLOCK feature to accommodate the travel time and didn’t find anything useful

pysan3: Very interesting

Vhyrro: It gets cooler the more you think about it :kek:

yelircaasi: I had it working in python, then changed too much, got tired of the million tests Python requires and decided to switch. After all, if I'm trying to present a project claiming to provide pure functional planning and scheduling, the first question is always going to be "You did this is Python???"

pysan3: Umm, tho I think writing in rust gets you the most contributors :kek:

Vhyrro: haskell is useful in the sense that you can guarantee it's purely functional

when it comes to fundamental building blocks and algorithms being able to represent them in this way is generally good

@yelircaasi make in ocaml for 🐐 points :kek:

yelircaasi: Tbh, I thought a lot about this. But with my background, having written more Nix than C/C++ ir anything Rust-like, the jump to Haskell seems easier. And Haskell is a very natural choice for this project

b4mbus: Nahh we got 8d calendars before gta6

Vhyrro: for real ☠️

b4mbus: Haskell's syntax and semantics are nowhere near Nix'es tho

yelircaasi: But I certainly have Rust on my radar and hope to release a Rust project sooner or later, stay tuned. But this project, preliminarily named Nebokrai, is my first love, so I want to focus as much as possible

Vhyrro: 👏 make 👏 in 👏 ocaml

b4mbus: Do you know any already? If no, then I can point you at some banger resources

pysan3: At some point you’d want to manually reorder tasks regardless of what the program recommends, and pure functional langs will be kinda pain to keep these in track?

yelircaasi: but the general logic is there. I see a lot that reminds me of Nix, and the general mindset and reasoning are similar. It feels comfortable.

b4mbus: .. why?

Vhyrro: imo what's most important is the fundamental algorithm, not the reordering part

the reording part is a layer on top of the algorithm, not the algo itself

b4mbus: Reordering stuff is the runtime, the behaviour of the program

Yeah

Vhyrro: data goes in, sorted list goes out. whatever you do with that data afterwards is up to you :D

yelircaasi: I think this is a feature of the approach, at least for me. You pass in your json (dhall, kdl, nickel, potentially whatever sexy config language you like) and you get the output as a direct result of your priorities, available time, and temporal dependencies. To change the output, change the input

Or, if you must, edit the output schedule, in txt or tex or whatever

yelircaasi: yeah, I can get behind this. After all, user knows best. At the same time, if you follow the generated schedule, you know your actions are in accordance with yur long-term goals, according to the criteria you yourself specified

pysan3: Well, theories aside, I once made my task app and miserably failed with ocaml :PepeHands:

The more features I added, the more nested if-else and it was more hassle than benefit to use functional language…

I definitely think you guys are better programmers lol

Vhyrro: functional languages don't scale well for very large apps

but are perfect for smaller things like this which need to be solid and basically unbreakable

yelircaasi: I'm not a phenomenal programmer. If you read my Python code, you'll see ut's shit. And I made too many changes, it doesn't even run

Vhyrro: functional languages force you to break down the problem into its smallest constituent parts

yelircaasi: But that's what I love about Haskell, it forces you to be a good programmer, like it or not :kek:

pysan3: And the lack of libraries was also a pain. I don’t regret using python-poetry all the time now lol

yelircaasi: and this is perfect for the kinds of ordering and scheduling algorithms I am writing. I really think Haskell is a good choice. But maybe I'll be back in a month to announce the RiR :kekw:
