#!/usr/bin/env python3

import json
import subprocess
from time import sleep

# colorize output
OR = '\x1b[0;34m' # routine
OG = '\x1b[0;32m' # good
OB = '\x1b[1;31m' # bad
OM = '\x1b[0m'    # mischief managed

# read JSON file of checks
fin = open("./checks.json","r")
checks = json.loads(fin.read())
print(f"{OR}{checks}{OM}")

while True: # run FOREVER
    for check in checks: # one check at a time
        command = check["cmd"].split(" ") # subprocess takes commands and arguments [in, a, list]
        try:
            response = (subprocess.check_output(command)).decode("UTF") # turn bytes response to string
            print(f"{OR}{check['name']} check:{OM}")
            if check["expect"] in response:
                print(f"{OG}{check['expect']}{OM}") # matches what's expected - yay!
            else:
                print(f"{OB}*** {response} ***{OM}") # came back with something sad )-:
        except Exception as ex:
            print(f"{OB}*** Check {check['name']} failed ***{OM}")
            print(f"{OB}Exception:\n{ex}{OM}")
    sleep(5)
