#### 1. Initialising the game ##################################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from marble_maze_lib import MarbleMaze
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
game = MarbleMaze(sense) # Initializes the game.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.
sense.set_imu_config(False, True, False) # Enable the gyroscope

#### 1.3 Set up the game variables

game.setBallPosition(0, 0) # Set starting ball position
game.ballColour = [0, 0, 0] # The ball colour
game.wallColour = [0, 0, 0] # The wall block colour
game.holeColour = [0, 0, 0] # The hole block colour
game.goalColour = [0, 0, 0] # The goal block colour

#### 1.4 Create the maze!

#### 2. Main game code #########################################################

while True:

  #### 2.1 Make the ball move



  #### 2.2 Draw the walls, holes, goals and the ball



  #### 2.3 Update the game



  #### 2.4 Check if the player has won or lost
