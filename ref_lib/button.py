#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

btn = Button()

# Do something when state of any button changes:

def left(state):
    if state:
        print('Left button pressed')
    else:
        print('Left button released')

def right(state):  # neater use of 'if' follows:
    print('Right button pressed' if state else 'Right button released')

def up(state):
    print('Up button pressed' if state else 'Up button released')

def down(state):
    print('Down button pressed' if state else 'Down button released')

def enter(state):
    print('Enter button pressed' if state else 'Enter button released')

def backspace(state):
    print('Backspace button pressed' if state else 'Backspace button released')

btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
btn.on_backspace = backspace

while True:  # This loop checks buttons state continuously,
             # calls appropriate event handlers
    btn.process() # Check for currently pressed buttons.
    # If the new state differs from the old state,
    # call the appropriate button event handlers.
    sleep(0.01)  # buttons state will be checked every 0.01 second

# If running this script via SSH, press Ctrl+C to quit
# if running this script from Brickman, long-press backspace button to quit