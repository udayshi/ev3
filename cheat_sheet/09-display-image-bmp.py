#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import PIL
  
ev3.Sound.beep().wait()
  
lcd = ev3.Screen()
logo = PIL.Image.open('club-engineer.bmp')
lcd.image.paste(logo, (0,0))
lcd.update()
time.sleep(5)