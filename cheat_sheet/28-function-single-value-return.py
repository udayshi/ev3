#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()
cl = ev3.ColorSensor('in1')
cl.mode='COL-REFLECT'

def readAverageLightSensorValue(ACount):
  LLightSensorValue = 0
  for i in range(0, ACount-1):
    LLightSensorValue += cl.value()
    time.sleep(0.1)
  return LLightSensorValue / ACount
  
while True:
  print(readAverageLightSensorValue(10))
  time.sleep(1)
 