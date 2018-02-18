#### 1. Initialising the game

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
from sense_hat import SenseHat
from senselib import *
import math

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the variables

posx = 4
posy = 4
posvx = 0.5
posvy = 0.5
rot = 0.1

fade_factor = 0.9
screen = sense.get_pixels()

#### 2. Main game code

while True:

    posvx = posvx*math.cos(rot) - posvy*math.sin(rot)
    posvy = posvx*math.sin(rot) + posvy*math.cos(rot)

    posx += posvx
    posy += posvy

    ix = int(posx % 8)
    iy = int(posy % 8)

    #sense.set_pixel(0, 1, 255, 255, 255 )
    #print(sense.get_pixels())
    screen = map(lambda c: map(lambda d: d*fade_factor, c), screen)
    pixels = map(lambda c: map(int, c), screen)
    sense.set_pixels(pixels)
    sense.set_pixel(ix, iy, 255, 255, 255)
    screen[iy*8 + ix] = [255, 255, 255]
