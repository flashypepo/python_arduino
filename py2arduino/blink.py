# -*- coding: utf-8 -*-
"""
Spyder Editor

Blink a LED on pin 'pin'.
"""

import serial
import pyfirmata

pin = 7  #13
port = '/dev/cu.usbmodem1A1221' # 2016_0423 updated
board = pyfirmata.Arduino(port)

# TODO: maak een loopje
board.digital[pin].write(0)   # LED on
board.pass_time(2)            #wait 5 seconds
board.digital[pin].write(1)   # LED off

