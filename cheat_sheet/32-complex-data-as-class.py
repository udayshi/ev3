#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

class LSValues(object):
    left = 0
    right = 0

ev3.Sound.beep().wait()

GLSLeft = ev3.ColorSensor('in1')
GLSLeft.mode= 'COL-REFLECT'

GLSRight = ev3.ColorSensor('in2')
GLSRight.mode= 'COL-REFLECT'

def readLightSensorValues(ALSValues):
  ALSValues.left = GLSLeft.value();
  ALSValues.right = GLSRight.value();
  
while True:
  LLSValues = LSValues()
  readLightSensorValues(LLSValues)
  print(LLSValues.left, LLSValues.right)
  time.sleep(0.5)
  