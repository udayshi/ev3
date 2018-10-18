#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

lcd = ev3.Screen()
lcd.draw.ellipse(( 20, 20,  60, 60))
lcd.draw.ellipse((118, 20, 158, 60))
lcd.draw.arc((20, 80, 158, 100), 0, 180)
lcd.update()
time.sleep(5)