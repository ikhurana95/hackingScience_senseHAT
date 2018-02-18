###### 1. Initialising the game ################################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from snake_lib import Snake
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the game variables

applePosition = [1, 1] # Set the starting position of the apple
snake = Snake([3,3]) # Creates the snake, and sets its starting position

snakeColour = [0, 255, 0] # Colour of the snake
appleColour = [255, 0, 0] # Colour of the apple

###### 2. Main game code #######################################################

while True:

    #### 2.1 Let the user control the snake


    #### 2.2 Draw the snake and the apple


    #### 2.3 Move the snake



    #### 2.4 Check if apple ate an apple



    #### 2.5 Check if snake has collided with itself



    #### 2.6 Add some delay
