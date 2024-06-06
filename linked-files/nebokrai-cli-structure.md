# Nebokrai CLI Structure

Commands are arranged hierarchically. Each command, unless run with options that specify otherwise,
and unless otherwise specified in the description, defaults to interactive and has an `interactive`
command.

For more info, consult the documentation and run `nebokrai --help`.

```txt
nebokrai               # defaults to `interactive`
 ┣━━ interactive       # enter interactive mode
 ┣━━ validate          # enter interactive validation menu
 ┃    ┣━━ all          # check JSON files in the declaratiion for validity
 ┃    ┣━━ calendar     #
 ┃    ┣━━ config       #
 ┃    ┣━━ roadmaps     #
 ┃    ┣━━ routines     #
 ┃    ┗━━ tracking     #
 ┣━━ derive            # perform derivation
 ┃    ┣━━ dryun        # perform derivation and save
 ┃    ┣━━ dryun-accept # accept the results of the last dryrun (if the last derivation was a dryrun)
 ┃    ┣━━ plan         #
 ┃    ┗━━ schedules    #
 ┣━━ track             # enter interactive tracking prompt
 ┣━━ x                 # check off a task as completed
 ┣━━ declaration       # enter interactive declaration management menu
 ┃    ┣━━ add          # add an item (project, task, calendar entry, etc) to the declaration
 ┃    ┣━━ remove       # remove an item from the declaration
 ┃    ┣━━ edit         # change an item in the declaration
 ┃    ┣━━ search       # search for some text string in the declaration
 ┃    ┗━━ export       # enter derivation export menu
 ┃         ┣━━ pdf     #
 ┃         ┣━━ txt     #
 ┃         ┣━━ jpg     #
 ┃         ┗━━ png     #
 ┣━━ derivation        # enter interactive derivation menu
 ┃    ┣━━ blame        #
 ┃    ┣━━ summarize    #
 ┃    ┣━━ search       # search for some text string in the derivation
 ┃    ┣━━ debug        #
 ┃    ┗━━ export       # enter derivation export menu
 ┃         ┣━━ pdf     #
 ┃         ┣━━ txt     #
 ┃         ┣━━ jpg     #
 ┃         ┗━━ png     #
 ┣━━ tracking          # enter the interactive tracking explorer menu
 ┃    ┗━━ search       # search for some text string in tracking
 ┣━━ sync              # enter interactive sync menu
 ┣━━ generations       # view all saved generations of the declaration and derivation
 ┣━━ revert            #
 ┗━━ dashboard         #
      ┣━━ view         # display at-a-glance overview of habits and progress
      ┣━━ debug        # enter dashboard debugging menu
      ┗━━ export       # enter dashboard export menu
           ┣━━ pdf     #
           ┣━━ txt     #
           ┣━━ jpg     #
           ┗━━ png     #
```
