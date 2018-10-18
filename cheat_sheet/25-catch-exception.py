#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

try:
    # Put the code that may fail inside a try / except block
    n = 1 / 0
except:
    # You can recover from the exception here
    n = 0

# This line execute because the exception was handled
ev3.Sound.beep().wait()
print(str(n))
time.sleep(5)