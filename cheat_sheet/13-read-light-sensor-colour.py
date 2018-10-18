#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
  
ev3.Sound.beep().wait()
  
cl = ev3.ColorSensor('in1')

# Put the color sensor into COL-COLOR mode
# Will return an integer 0..7
cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

while True:
    print(str(cl.value()) + ' | ' + colors[cl.value()])
    time.sleep(0.5) 