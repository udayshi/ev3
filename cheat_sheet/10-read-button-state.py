#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
  
ev3.Sound.beep().wait() 

btn = ev3.Button()

while True:
    if btn.backspace:
      print('Backspace pressed')
    elif btn.left:
      print('Left pressed')
    elif btn.right:
      print('Right pressed')
    elif btn.enter:
      print('Enter pressed')
    elif btn.up:
      print('Up pressed')
    elif btn.down:
      print('Down pressed')
    else:
      time.sleep(0.05)