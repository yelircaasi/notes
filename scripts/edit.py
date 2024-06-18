#!/usr/bin/env python

import time
import subprocess
import sys

file = f"/home/isaac/repos/notes/json-notes/{sys.argv[1]}.json"

print("starting")
print(f"editing {file}")
time.sleep(1.0)
subprocess.run(["nvim", file])
print("finished")
