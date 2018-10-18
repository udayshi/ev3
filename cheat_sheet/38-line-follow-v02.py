#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

btn = ev3.Button()

GLightLeft = ev3.ColorSensor('in1')
GLightLeft.mode='COL-REFLECT'

GLightRight = ev3.ColorSensor('in4')
GLightRight.mode='COL-REFLECT'

GMotorLeft = ev3.Motor()
GMotorLeft = ev3.LargeMotor('outD')
GMotorRight = ev3.Motor()
GMotorRight = ev3.LargeMotor('outA')

GThresholdLeft = 40
GThresholdRight = 40
GSpeedOutside = 350
GSpeedInside = -150

while not btn.backspace:
    LLeft = GLightLeft.value()
    LRight = GLightRight.value()
       # Light                    Light - Go straight
    if LLeft > GThresholdLeft and LRight > GThresholdRight:
        GMotorLeft.run_forever(speed_sp=GSpeedOutside)
        GMotorRight.run_forever(speed_sp=GSpeedOutside)
        # Light                    Dark - Turn Right
    elif LLeft > GThresholdLeft and LRight < GThresholdRight:
        GMotorRight.run_forever(speed_sp=GSpeedOutside)
        GMotorLeft.run_forever(speed_sp=GSpeedInside)
        #GMotorLeft.stop(stop_action='brake')
        # Dark                     Light - Turn Left
    elif LLeft < GThresholdLeft and LRight > GThresholdRight:
        GMotorLeft.run_forever(speed_sp=GSpeedOutside)
        GMotorRight.run_forever(speed_sp=GSpeedInside)
        # GMotorRight.stop(stop_action='brake')
    # Dark                     Dark - Stop both
    else:
        GMotorLeft.stop(stop_action='brake')
        GMotorRight.stop(stop_action='brake')
    time.sleep(0.01)