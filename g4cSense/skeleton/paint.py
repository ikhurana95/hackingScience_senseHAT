#### 1. Initialising the game ##################################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from sense_hat import SenseHat
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(False, False, True) # Enable accelerometer
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the variables

cursorx = 4 # The initial position of the cursor
cursory = 4

currentColour = 0 # Which colour in the list we are currently using

colours = [  ] # The different colours that we can draw in

#### 2. Main code ##############################################################

while True:

  #### 2.1 Control the paint cursor and place colours on the screen


  #### 2.2 Change colour by shaking
