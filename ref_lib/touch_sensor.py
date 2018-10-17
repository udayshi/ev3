#!/usr/bin/env python3
# Above line is needed so program can be run from Brickman

# Plug a touch sensor into any sensor port
from ev3dev.ev3 import *
ts = TouchSensor()

while True:
    if ts.value()==1:   #touch sensor pressed
        Leds.set_color(Leds.LEFT, Leds.RED)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)