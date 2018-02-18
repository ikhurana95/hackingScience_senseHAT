###### 1. Initialising the program #############################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from senselib import *
import random

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
sense.clear() # Clears all pixels on the screen.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions

###### 2. Draw the picture #####################################################
