#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time
import sys

# Output the result of this program to output.txt so it is easy to read
sys.stdout = open('output.txt', 'w')

ev3.Sound.beep().wait()

GValue = 10
UValue = 20

def doStuff(AValue):
  # Make the variable GValue visible and writable inside doStuff()  
  global GValue
  
  # Print AValue (3)
  print(str(AValue))
  
  # Add 1 to AValue (making it 4)
  AValue = AValue + 1
  
  # Print AValue (4)
  print(str(AValue))
  
  
  print(str(GValue))
  GValue = GValue + 1
  print(str(GValue))

  # print(str(UValue))
  # The line above would have failed to execute as UValue, while declared 
  # outside the procedure doStuff() is not visible inside doStuff()
  
print(str(GValue)) 
# 10 Will have been printed

print(str(UValue)) 
# 20 Will have been printed

LValue = 3
doStuff(LValue)
# 3, 4, 10, 11 (each on their own line) will have been printed

print(str(LValue))
# 3 Will be printed. Although doStuff() has changed LVariable, the 
# change is only visible inside the scope of doStuff(). The original
# value will be preserved here

print(str(GValue))
# 11 Will have been printed. GValue has been changed by doStuff()

print(str(UValue))
#20 Will have been printed. UValue has not been changed by doStuff()