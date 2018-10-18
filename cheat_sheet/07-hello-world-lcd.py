#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

lcd = ev3.Screen()
lcd.draw.text((48,60),'Hello world!')
lcd.update()
time.sleep(5)