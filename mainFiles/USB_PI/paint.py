#### 1. Initialising the game

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from sense_hat import SenseHat
import random
from senselib import *
import time
#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(False, False, True) # Enable accelerometer
sense.clear() # Clears all pixels on the screen.
#### 1.3 Set up the variables

cursorx = 4 # The initial position of the cursor
cursory = 4

currentColor = 0 # Which color in the list we are currently using
colors = [randomColour() for i in range(12)] # The different colors that we can draw in

image = sense.get_pixels() # Save the sreen as it is for now

#### 2. Main game code

while True:

    #### 2.1 Control the paint cursor and place colors on the screen

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                cursory -= 1
                if cursory < 0:
                    cursory = 7
            elif event.direction == "down":
                cursory += 1
                if cursory > 7:
                    cursory = 0
            elif event.direction == "left":
                cursorx -= 1
                if cursorx < 0:
                    cursorx = 7
            elif event.direction == "right":
                cursorx += 1
                if cursorx > 7:
                    cursorx = 0

            elif event.direction == "middle":
                c = colors[currentColor]
                sense.set_pixel(cursorx, cursory, c[0], c[1], c[2])
                image = sense.get_pixels()

    #### Bonus: Add a visible cursor on the screen

    c = colors[currentColor]
    sense.set_pixels(image)
    sense.set_pixel(cursorx, cursory, c[0], c[1], c[2])


    #### 2.2 Change color by shaking

    ac = sense.get_accelerometer_raw()
    x = ac["x"]
    y = ac["y"]
    z = ac["z"]


    if x*x + y*y + z*z > 4:

        currentColor += 1


        ##Prevents flicker
        time.sleep(0.3)

        if currentColor >= len(colors):
            currentColor -= len(colors)

