#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

m = ev3.LargeMotor('outA')

m.run_forever(speed_sp=450)   # equivalent to power=50 in EV3-G
while True:
    time.sleep(0.01)
