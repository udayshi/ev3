#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB')
assert m.connected
m.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
sleep(5)   # Give the motor time to move


m.run_timed(time_sp=3000, speed_sp=-750).wait()
print("set speed (speed_sp) = " + str(m.speed_sp))
sleep(1)  # it takes a moment for the motor to start moving
print("actual speed = " + str(m.speed))
sleep(4)


m.run_forever(speed_sp=900)
sleep(5)
m.stop(stop_action="hold")
sleep(5)


m.run_timed(time_sp=3000, speed_sp=-750, stop_action='brake')
m.wait_while('running')
Sound.beep()

#Making sure its stopped.
m.run_forever(speed_sp=0)
m.stop()
