# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:20:26 2016
GUI: time delay entry and 
a button to set LED on pin 7 ON, and then after delay OFF
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
#ledPin = board.get_pin('d:7:o') #led: pin 7, output digital
ledPin = board.get_pin('d:3:p') #led: pin 3, output PWM


#init Main window
top = tkinter.Tk()
top.title("Change LED brightness using Scale")
top.minsize(300, 30)

#adopted to timePeriodEntry
def onStartButtonPress():
    # get value from timePeriodEntry
    timePeriod = timePeriodEntry.get()
    timePeriod = float(timePeriod)
    #brihtness
    ledBrightness = brightnessScale.get()
    ledBrightness = float(ledBrightness)
    
    startButton.config(state=tkinter.DISABLED)
    ledPin.write(ledBrightness/100.0) # ledPin.write(1)
    sleep(timePeriod)
    ledPin.write(0)
    startButton.config(state=tkinter.NORMAL) # tkinter state
    
#entry for period
timePeriodEntry = tkinter.Entry(top,
                                bd = 5,
                                width = 25) 
timePeriodEntry.pack()
timePeriodEntry.focus_set()

#scale for brightness
brightnessScale = tkinter.Scale(top,
                                from_= 0, 
                                to = 100,
                                orient=tkinter.HORIZONTAL)#.VERTICAL)
brightnessScale.pack()

#button
startButton = tkinter.Button(top, 
                             text="Start", 
                             command=onStartButtonPress)
startButton.pack()

#start and open the window
top.mainloop()


