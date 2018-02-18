###### 1. Initialising the project #############################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from senselib import *
import random

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the variables

countdown = 10
number_colour = [0, 0, 0]
countdownMessage = ""

###### 2. Set the countdown clock ##############################################

#### 2.1 Create a while-loop



#### 2.2 Let the user choose the countdown time



#### Bonus: Don't let the number go under 0 or over 99



#### 2.3 Draw the current countdown time



###### 3. Count down the time ##################################################

#### 3.1 Create a for-loop



#### 3.2 Draw the countdown number



#### 3.3 Wait a second



#### 4. Clock has finished #####################################################
