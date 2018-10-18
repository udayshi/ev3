#!/usr/bin/env python3
# Before running this program, you must install some
# fonts. With a putty session open, install the MS
# core fonts package:
#   sudo apt-get install ttf-mscorefonts-installer
# Then run this to see what fonts have been installed:
#   ls /usr/share/fonts/truetype/msttcorefonts/


import ev3dev.ev3 as ev3
from PIL import ImageFont # PIL = Python Image Library
import time

ev3.Sound.beep().wait()
lcd = ev3.Screen()
f = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 16)
btn = ev3.Button()

GLightLeft = ev3.ColorSensor('in1')
GLightLeft.mode='COL-REFLECT'
GLightRight = ev3.ColorSensor('in4')
GLightRight.mode='COL-REFLECT'

while not btn.backspace:
    lcd.clear()
    lcd.draw.text((10, 30), 'Left: ' + str(GLightLeft.value()), font=f)
    lcd.draw.text((10, 80), 'Right: ' + str(GLightRight.value()), font=f)
    lcd.update()
    time.sleep(0.1)
