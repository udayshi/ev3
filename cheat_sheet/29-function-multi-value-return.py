#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()
cl = ev3.ColorSensor('in1')
cl.mode='RGB-RAW'

def readAverageLightRGB(ACount):
  LRSum = 0
  LGSum = 0
  LBSum = 0
  for i in range(0, ACount-1):
    LRSum += cl.value(0)
    LGSum += cl.value(1)
    LBSum += cl.value(2)
    time.sleep(0.1)
  return LRSum / ACount, LGSum / ACount, LBSum / ACount
  
while True:
  LR, LG, LB = readAverageLightRGB(10)
  print(LR, LG, LB)
  time.sleep(1)
 