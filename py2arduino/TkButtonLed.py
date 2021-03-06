# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:20:26 2016
GUI with Button to set LED on pin 7 ON
@author: PePo
"""

# zet LED op pin 7 aan of uit met een Button widget
import tkinter
import pyfirmata
from time import sleep

# port Arduino, ls /dev/cu*
port = '/dev/cu.usbmodem1A1221' 
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:7:o') #led: pin 7, output

#init Main window
top = tkinter.Tk()
top.title("Blink LED using Button")
top.minsize(300, 30)

def onStartButtonPress():
    startButton.config(state=tkinter.DISABLED)
    ledPin.write(1)
    sleep(5)
    ledPin.write(0)
    startButton.config(state=tkinter.NORMAL) # tkinter state
    
    

#button
startButton = tkinter.Button(top, 
                             text="Start", 
                             command=onStartButtonPress)
startButton.pack()

#start and open the window
top.mainloop()


