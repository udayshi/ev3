#!/usr/bin/env python3
import ev3dev.ev3 as ev3

ev3.Sound.beep().wait()

f = open('data.txt', 'r') 
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()

print(line1)
print(line2)
print(line3)

ev3.Sound.beep().wait()