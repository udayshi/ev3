#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
while True:
  ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
  ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
  time.sleep(0.33)
  ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
  ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
  time.sleep(0.33)
  ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
  ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
  time.sleep(0.33)