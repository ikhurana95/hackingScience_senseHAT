#### 1. Initialising the game

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from marble_maze_lib import MarbleMaze
import random , time
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
game = MarbleMaze(sense) # Initializes the game.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the game variables

game.setBallPosition(0, 0) # Set starting ball position
game.ballColor = [255, 0, 0] # The ball color
game.wallColor = [255, 255, 255] # The wall block color
game.holeColor = [0, 0, 0] # The hole block color
game.goalColor = [0, 255, 0] # The goal block color

#### 1.4 Create the maze!

game.placeWall(0, 2)
game.placeWall(1, 2)
game.placeWall(2, 2)
game.placeWall(3, 2)

game.placeHole(6, 0)
game.placeHole(7, 0)
game.placeHole(6, 1)
game.placeHole(7, 1)

game.placeWall(4, 4)
game.placeWall(5, 4)
game.placeWall(6, 4)
game.placeWall(7, 4)

game.placeHole(0, 5)
game.placeHole(0, 6)
game.placeHole(0, 7)
game.placeHole(1, 5)
game.placeHole(1, 6)
game.placeHole(1, 7)

game.placeGoal(6, 6)
game.placeGoal(7, 6)
game.placeGoal(6, 7)
game.placeGoal(7, 7)

#### 2. Main game code

while True:

    #### 2.1 Make the ball move

    orientation = sense.get_orientation()

    game.moveBallHorizontally( orientation["pitch"] )
    game.moveBallVertically( orientation["roll"] )
    print(orientation)
    print("Velocity " , game.ballvx)
    
    #### 2.2 Draw the walls, holes, goals and the ball

    sense.clear(0, 0, 50)

    game.drawWalls()
    game.drawHoles()
    game.drawGoals()

    sense.set_pixel(game.getBallX(), game.getBallY(), game.ballColor [0], game.ballColor[1], game.ballColor[2])

    #### 2.3 Make things happen

    game.update()

    #### 2.4 Check if the player has won or lost

    if game.isHole(game.getBallX(), game.getBallY()):
        game.setBallPosition(0, 0)

    if game.isGoal(game.getBallX(), game.getBallY()):
        game.setBallPosition(0, 0)
