#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *


# Connect remote control
rc = RemoteControl()
assert rc.connected

# Turn leds off
Leds.all_off()

def roll(led_group, direction):
    def on_press(state):
        if state:
            # Roll when button is pressed
            Leds.set_color(led_group, direction > 0 and Leds.GREEN or Leds.RED)
        else:
            # Stop otherwise
            Leds.set(led_group, brightness_pct=0)

    return on_press

# Assign event handler to each of the remote buttons
rc.on_red_up    = roll( Leds.LEFT,   1)
rc.on_red_down  = roll( Leds.LEFT,  -1)
rc.on_blue_up   = roll( Leds.RIGHT,  1)
rc.on_blue_down = roll(Leds.RIGHT, -1)

# Enter event processing loop
#while not button.any():   #not working so commented out
while True:   #replaces previous line so use Ctrl-C to exit
    rc.process()
    sleep(0.01)

# Press Ctrl-C to exit