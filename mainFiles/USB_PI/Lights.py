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

from collections import deque



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
sense.low_light = True
while True:


    for colour in colours:
        endTime = time.time() + 3
        while time.time() < endTime:
            sense.set_pixels(glitter(colour))
            time.sleep(0.2)

# while True:
#
#     sense.set_pixels(mosaicGlitter())
#     time.sleep(0.1)


# sense.set_pixels(ticTacToeBoard())