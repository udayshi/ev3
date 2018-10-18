#!/usr/bin/env python3

# To test this script, make sure the folder packagecompount is
# also uploaded.

import ev3dev.ev3 as ev3

# These 5 lines will work showing one technique of calling import
import packagecompound.sound as sound
import packagecompound.text as text
ev3.Sound.beep().wait()
sound.beep()
text.sayHello()

# These 4 lines will work showing one technique of calling import
#from packagecompound import sound, text
#ev3.Sound.beep().wait()
#sound.beep()
#text.sayHello()