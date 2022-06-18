# CTFUpChecker
A simple Python health check, designed for active monitoring of CTF assets

## Setup
THIS WILL FAIL if you run it as-is.  Setup is required.

1. Determine what online assets you want to check, what command you'll use, and what expected output is
2. Put entries into _checks.json_ for each asset you're checking:
  - _name_ should be something descriptive or meaningful to you
  - _cmd_ is the command that Python will `subprocess.check_output()`
  - _expect_ is a string that should come out of the _cmd_ to STDOUT when the asset is healthy
3. Ensure any PEM or other files needed for checks are in the working directory of _rctfok.py_

## Running
`python3 rctfok.py` and watch for red output

```
  _____     _____ _______ ______    ____  _  _____  
 |  __ \   / ____|__   __|  ____|  / __ \| |/ /__ \ 
 | |__) | | |       | |  | |__    | |  | | ' /   ) |
 |  _  /  | |       | |  |  __|   | |  | |  <   / / 
 | | \ \  | |____   | |  | |      | |__| | . \ |_|  
 |_|  \_\  \_____|  |_|  |_|       \____/|_|\_\(_)  
```
