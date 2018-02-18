#### 1. Initialising the game ##################################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
from sense_hat import SenseHat
from pong_lib import Pong
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
pong = Pong(sense) # Initializes the game.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions

sense.clear() # Clears all pixels on the screen.
sense.show_message("PONG!", 0.03) # Display an intro message for the viewer.

#### 1.3 Set up the game variables

pong.player1size = 0 # Size of the player 1 paddle
pong.player1pos = 0 # Vertical position of the player 1 paddle
pong.player1colour = [0, 0, 0] # Colour of player 1 paddle
pong.player1score = 0 # Score of player 1

pong.player2size = 0 # Size of the player 2 paddle
pong.player2pos = 0 # Vertical position of the player 2 paddle
pong.player2colour = [0, 0, 0] # Colour of player 2 paddle
pong.player2score = 0 # Score of player 2

pong.ballX = 0 # Horizontal position of the ball
pong.ballY = 0 # Vertical position of the ball
pong.ballVelocityX = random.choice([-1, 1]) # Randomizes the vertical velocity of the ball.
pong.ballVelocityY = random.choice([-1, 1]) # Randomizes the horizontal velocity of the ball.
pong.ballColour = [0, 0, 0] # Colour of the ball

#### 2. Main game code #########################################################

while True:

  #### 2.1 Check for player1 movement (joystick)



  #### 2.2 Let computer control player2



  #### 2.3 Calculate new ball position



  #### 2.4 Check if new ball position has hit the player paddles



  #### 2.5 Check if new ball position is in goal



  #### 2.6 Check if new ball position has collided with the top or bottom walls



  #### 2.7 Update ball position



  #### 2.8 Clear screen



  #### 2.9 Draw player1 and player2



  #### 2.10 Draw ball



  #### 2.11 Wait a little bit before the next frame
