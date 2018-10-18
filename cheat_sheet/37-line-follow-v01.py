#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

btn = ev3.Button()

GLightRight = ev3.ColorSensor('in4')
GLightRight.mode='COL-REFLECT'

GMotorLeft = ev3.Motor()
GMotorLeft = ev3.LargeMotor('outD')
GMotorRight = ev3.Motor()
GMotorRight = ev3.LargeMotor('outA')

while not btn.backspace:
    if GLightRight.value() > 40:
        GMotorLeft.run_forever(speed_sp=450)  # equivalent to power=20 in EV3-G
        GMotorRight.stop(stop_action='brake')
    else:
        GMotorRight.run_forever(speed_sp=450)  # equivalent to power=20 in EV3-G
        GMotorLeft.stop(stop_action='brake')
    time.sleep(0.01)