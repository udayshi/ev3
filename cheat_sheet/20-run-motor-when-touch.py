#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

m = ev3.LargeMotor('outA')
ts1 = ev3.TouchSensor('in1') 

while True:
    if ts1.value() == 0:
      m.stop(stop_action="brake")
    else:
      m.run_forever(speed_sp=180)   # equivalent to power=20 in EV3-G
