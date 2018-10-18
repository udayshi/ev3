#!/usr/bin/env python3
import ev3dev.ev3 as ev3

ev3.Sound.beep().wait()

f = open('data.txt', 'w') 
f.write('This is line #1\n')
f.write('This is line #2\n')
f.write('This is line #3\n')
f.close()

ev3.Sound.beep().wait()