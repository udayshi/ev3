#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

m = ev3.LargeMotor('outA')

# Run ten rotations (360 * 10) at a speed of 430 deg per second, then brake
m.run_to_rel_pos(position_sp=3600, speed_sp=430, stop_action='brake')
while any(m.state):
    time.sleep(0.1)
    
ev3.Sound.beep().wait()