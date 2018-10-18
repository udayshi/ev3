#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

# Connect an EV3 Touch Sensor to Port 1
ts1 = ev3.TouchSensor('in1') 

while True:
    if ts1.value() == 0:
      ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
      ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    else:
      ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
      ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
