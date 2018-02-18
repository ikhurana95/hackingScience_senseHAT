########################
#                      #
#     Party Lights     #
#                      #
########################




"""

Let's use the SenseHat's LEDs to make some party lighting.

"""


import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from sense_hat import SenseHat
from senseGraphics import *
from senselib import *
import random
import time
import numpy as np

sense = SenseHat()
def singleColour(colour):

    c = colour

    pixels = [
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
    ]

    return pixels

def glitter(colour):

    pixel = []

    for i in range(8):

        for j in range(8):

            if colour == 'yellow':
                c = randomYellow()
            elif colour == 'red':
                c = randomRed()
            elif colour == 'blue':
                c = randomBlue()
            elif colour == 'green':
                c = randomGreen()
            pixel.append(c)

    return pixel

colours = ['yellow','blue','red','green']
endTime = time.time() + 3
glitterColour = random.choice(colours)

while endTime> time.time():
    sense.set_pixels(glitter(glitterColour))
    time.sleep(0.2)



sense.show_message("Select file to run" , text_colour = randomColour())



