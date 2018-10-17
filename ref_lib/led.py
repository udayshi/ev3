from ev3dev.ev3 import *
from time import sleep

Leds.set_color(Leds.LEFT,  Leds.ORANGE)
sleep(0.01)
Leds.set_color(Leds.RIGHT, Leds.ORANGE)
sleep(0.01)
Leds.set(Leds.LEFT, brightness_pct=0.5, trigger='timer')
Leds.set(Leds.LEFT, delay_on=3000, delay_off=500)
Leds.set_color(Leds.LEFT, Leds.GREEN)
#Turn off all leds
Leds.all_off()