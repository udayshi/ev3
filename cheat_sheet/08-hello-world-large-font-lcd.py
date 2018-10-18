#!/usr/bin/env python3

# Before running this program, you must install some
# fonts. With a putty session open, install the MS 
# core fonts package:
#   sudo apt-get update
#   sudo apt-get install ttf-mscorefonts-installer
# Then run this to see what fonts have been installed:
#   ls /usr/share/fonts/truetype/msttcorefonts/

import ev3dev.ev3 as ev3
from PIL import ImageFont # PIL = Python Image Library
import time

ev3.Sound.beep().wait()

lcd = ev3.Screen()
f = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 16)
lcd.draw.text((50, 60), 'Hello world', font=f)
lcd.update()
time.sleep(7)

