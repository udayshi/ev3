#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

# Connect ultrasonic and touch sensors to any sensor port
# and check they are connected.
us = UltrasonicSensor()
assert us.connected, "Connect a single US sensor to any sensor port"
ts = TouchSensor();    assert ts.connected, "Connect a touch sensor to any port"
# can have 2 statements on same line if use semi colon

# Put the US sensor into distance mode.
us.mode='US-DIST-CM'

units = us.units
# reports 'cm' even though the sensor measures 'mm'

while not ts.value():    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    distance = us.value()/10  # convert mm to cm
    print(str(distance) + " " + units)

    if distance < 60:  #This is an inconveniently large distance
        Leds.set_color(Leds.LEFT, Leds.RED)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
