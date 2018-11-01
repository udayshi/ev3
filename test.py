from lib.BusTimes import BusTimes

speech_text = ''
msg = '96 towards plumstead arrival time: ... ... '
bus_stop = '490014654N'
speech_text += BusTimes.getBusInfo(msg, bus_stop)
print(speech_text)