#!/usr/bin/env python3

# To test this script, make sure the file packagesimple.py is
# also uploaded.

import ev3dev.ev3 as ev3
import packagesimple

ev3.Sound.beep().wait()

packagesimple.sayHello()