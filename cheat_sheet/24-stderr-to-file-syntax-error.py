#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

ev3.Sound.beep().wait()
sys.stderr = open('error.txt', 'w')

# This will fail with a python langauge error
# because the indentation of time.sleep() is wrong.
# However, nothing will be written to error.txt because
# the parse failed, hence the program did not run at all.
# To examine this kind of error, use the _run script that 
# calls the program, then redirects the stderror
while True:
time.sleep(1)