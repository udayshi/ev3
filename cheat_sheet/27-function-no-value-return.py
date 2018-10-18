#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()
cl = ev3.ColorSensor('in1')
cl.mode='COL-REFLECT'

def printLightSensorValue():
  print(str(cl.value()))
  
while True:
  printLightSensorValue()
  time.sleep(1)
 