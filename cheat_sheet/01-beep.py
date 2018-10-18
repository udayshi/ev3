#!/usr/bin/env python3
import ev3dev.ev3 as ev3

for x in range(0, 3):
  ev3.Sound.beep().wait()