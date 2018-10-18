#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import threading
import time

ev3.Sound.beep().wait()

cl = ev3.ColorSensor('in1')
GLightSensorValue = ''

# Define a function for the thread
# Some sensors are very slow to return a value 
# (like the NXT US sensor) so reading them is best
# done in a seperate thread.
def readSlowSensor():
  global GLightSensorValue
  while True:
    GLightSensorValue = cl.value()
    time.sleep(0.01)
  
threading.Thread(target=readSlowSensor).start()

while True:
  print(str(GLightSensorValue))
  time.sleep(0.1)
 