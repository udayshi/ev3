#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
  
btn = ev3.Button()

def waitForEnter():
  while not btn.enter:
    time.sleep(0.05)
  while btn.enter:
    time.sleep(0.05)

ev3.Sound.beep().wait() 

print('Press <Enter> to continue')
waitForEnter()
ev3.Sound.beep().wait() 
print('<Enter> was pressed')