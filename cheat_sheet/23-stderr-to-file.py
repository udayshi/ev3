#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import sys

ev3.Sound.beep().wait()
sys.stderr = open('error.txt', 'w')

# This will fail with divide by zero error
n = 1 / 0

# This line should never execute
ev3.Sound.beep().wait()