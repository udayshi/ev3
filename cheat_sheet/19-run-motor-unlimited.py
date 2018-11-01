#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

ev3.Sound.beep().wait()

m = ev3.LargeMotor('outA')

m.run_forever(speed_sp=450)   # equivalent to power=50 in EV3-G
while True:
    time.sleep(0.01)


#!/usr/bin/env python3

#!/usr/bin/env python3

import samsungctl
import time

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.0.10",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
    for i in range(10):
        remote.control("KEY_MENU")
        time.sleep(0.5)#!/usr/bin/env python3
'''
KEY_POWEROFF	Power off
KEY_UP	Up
KEY_DOWN	Down
KEY_LEFT	Left
KEY_RIGHT	Right
KEY_CHUP	P Up
KEY_CHDOWN	P Down
KEY_ENTER	Enter
KEY_RETURN	Return
KEY_CH_LIST	Channel List
KEY_MENU	Menu
KEY_SOURCE	Source
KEY_GUIDE	Guide
KEY_TOOLS	Tools
KEY_INFO	Info
KEY_RED	A / Red
KEY_GREEN	B / Green
KEY_YELLOW	C / Yellow
KEY_BLUE	D / Blue
KEY_PANNEL_CHDOWN	3D
KEY_VOLUP	Volume Up
KEY_VOLDOWN	Volume Down
KEY_MUTE	Mute
KEY_0	0
KEY_1	1
KEY_2	2
KEY_3	3
KEY_4	4
KEY_5	5
KEY_6	6
KEY_7	7
KEY_8	8
KEY_9	9
KEY_DTV	TV Source
KEY_HDMI	HDMI Source
KEY_CONTENTS	SmartHub
'''