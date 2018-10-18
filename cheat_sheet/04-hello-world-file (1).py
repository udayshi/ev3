#!/usr/bin/env python3

File = open('hello.txt', 'w')
File.truncate()
File.write('Hello from EV3Dev in Python!')
File.close()