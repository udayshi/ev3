#!/usr/bin/env python3

# Constants are tricky to do in Python, as they are not 
# supported by the language. # There are several 
# recognised hacks, including the use of namedtuple
import ev3dev.ev3 as ev3
import collections
import time

ev3.Sound.beep().wait()

Constants = collections.namedtuple('Constants', ['PortLSLeft', 'PortLSRight'])
GConstants = Constants('in1', 'in4')

GLSLeft = ev3.ColorSensor(GConstants.PortLSLeft)
GLSLeft.mode= 'COL-REFLECT'

GLSRight = ev3.ColorSensor(GConstants.PortLSRight)
GLSRight.mode= 'COL-REFLECT'

print(str(GLSLeft.value()))
print(str(GLSLeft.value()))
print("----------")

time.sleep(5)