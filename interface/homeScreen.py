import os, sys, glob
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')

from senseGraphics import *
from sense_hat import SenseHat
from time import sleep
##Library with functions for graphcis compatible with the SenseHat

#import senseGraphics as sg

sense = SenseHat()
red = colour('pastel_red')
turquoise = colour('medium_turquoise')
fileColour = randomColour()
globSearch = '/home/pi/Go4Code/mainFiles/USB_PI/*.py'

files = glob.glob(globSearch)

menu = True
fileIndex = 0

def checkReset(sense):
    killFile = '/home/pi/Go4Code/interface/reset.sh'
    events = sense.stick.get_events()
    exit = False
    if len(events)>0:
      if events[0].direction == "down" and events[0].action == "held":
        sleep(2)

        events = sense.stick.get_events()

        
        if len(events)>0:
          if events[0].direction == "down" and events[0].action == "held":
          
            exit = True

    if exit:
        os.popen('sudo bash '+killFile)

        


while True:


    while menu:

        if len(files) == 0:
            textColour = red
            currentFile = "No Python Files :("
        else:
            textColour = fileColour
            currentFile = os.path.split(files[fileIndex])[1][:-3]

        sense.show_message(currentFile,text_colour=textColour)

        for event in sense.stick.get_events():

            ## Moving to next file
            if event.direction == "right" and event.action == "pressed":

                if fileIndex<len(files)-1:
                    fileIndex+=1
                else:
                    fileIndex = 0
                    continue
            ## Going one file back
            elif event.direction == "left" and event.action == "pressed":
                if fileIndex>0:
                    fileIndex -= 1
                else:
                    fileIndex = len(files)-1
                continue

            ## Selecting File
            elif event.direction == "middle" and event.action == "pressed":
                menu = False
                sense.clear()
                os.popen('python '+files[fileIndex]+'&')
                continue



    checkReset(sense)
            
        
    

