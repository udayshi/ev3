#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

ir = ev3.InfraredSensor('in1') 
ir.mode = 'IR-PROX'
lcd = ev3.Screen()

while True:
    lcd.clear()
    lcd.draw.text((48,60),str(ir.value()))
    lcd.update()
    time.sleep(0.01)    
