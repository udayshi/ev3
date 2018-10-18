#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
  
ev3.Sound.beep().wait()
  
cl = ev3.ColorSensor('in1')

# Put the color sensor into RGB-RAW mode
# Will return three values for RGB
cl.mode='RGB-RAW'

while True:
    red = cl.value(0)
    green=cl.value(1)
    blue=cl.value(2)
    print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
    time.sleep(0.5) 