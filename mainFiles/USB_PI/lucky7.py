########################
#                      #
#     Lucky 7          #
#                      #
########################




"""

In this game of chance, the dice Raspberry Pi randomly displays a number between 1 and 12.
Players guess whether the number will be below 7, above 7 or 7.

If a player correctly calls if the number will be below 7 or above 7 they get 20 points.
If they correctly guess the number to be 7, they get 70 points!

But if they guess wrongly, they lose 20 points!

Players start with 100 points

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

sense = SenseHat()
initialise(sense)
yellow = (255, 255, 0)
blue = (0, 0, 255)


#################################
# Initialise the game variables #
#################################

# Create a list of numbers to randomly pick from
numbers = list(range(1,13))

# Define a variable that stores the players points and initialise it
points = 100


# This variable sets the state of the game.
# If it is True the game will run, if it is False the game won't run.
runGame = True

# The while loop below runs as long as the state of the game is True.
while runGame:


    ##Get players choice##
    sense.set_pixels(seven())
    playerChoice = ''
    playerDeciding = True


    # Asks user to make a guess.
    # This loop will keep running until the user makes a choice.
    while playerDeciding:

        event = sense.stick.wait_for_event(emptybuffer=True)
        if event.direction == 'left':
            ##Moving the joystick down, selects below 7 as the guess

            playerChoice = 'below'
            playerDeciding = False

        elif event.direction == 'middle':
            ##clicking the middle, selects 7 as the guess

            playerChoice = 'seven'
            playerDeciding = False
        elif event.direction == 'right':

            ##Moving the joystick up, selects above 7 as the guess

            playerChoice = 'above'
            playerDeciding = False
        else:
            ##If the player moves the joystick up or down the game won't proceed.
            ##The loop will run again.

            continue

    # Checks the time at the start
    start = time.time()
    wait = 0 #Sets the intial wait between switching numbers to zero.

    while wait < 1:

        ###############
        displayNumber = (random.choice(numbers)) #Randomly pick a number from the list.
        show_numbers(displayNumber,text_colour=randomColour()) #Show that letter in a random colour

        ###############
        #Needs changes#
        t = time.time() - start
        time.sleep(wait)
        wait = 0.1 * (1 + np.exp(t - 6) ** 4)
        #####################

    ##Show the final number##
    show_numbers(displayNumber,text_colour=yellow)

    time.sleep(2)
    ##Allocate points##

    displayNumber = int(displayNumber) # converting the number to an integer so it can be compared to 7

    ## If the players choice matches what happened, they win.
    ## Each scenario allocates points and sets the message to be shown.

    if displayNumber>7 and playerChoice == 'above':
        message = "Correct! 20 points"
        points += 20

    elif displayNumber < 7 and playerChoice == 'below':
        message ="Correct! 20 points"
        points += 20

    elif displayNumber == 7 and playerChoice == 'seven':
        message = "Lucky 7! 70 points!! "
        points += 70

    else:
        message = "No luck!"
        points -= 20

    ##Show messages in random colours
    sense.show_message(message, text_colour= randomColour())
    pointMessage = "Total: " + str(points)

    sense.show_message(pointMessage,text_colour=randomColour())

    # Sets the state of the restart menu
    checkRestart = True

    #Loop runs while the resart menu is active
    while checkRestart:
        sense.set_pixels(upArrow())
        time.sleep(1)
        sense.show_message("OR")
        sense.set_pixels(downArrow())

        event = sense.stick.wait_for_event(emptybuffer=True)

        # If the player moves the joystick up the game keeps running
        if event.direction == 'up' and event.action == 'pressed':
            sense.set_pixels(seven())
            checkRestart = False
            runGame = True

        # If the player moves the joystick down the game quits
        elif event.direction == 'down' and event.action == 'pressed':
            checkRestart = False
            sense.show_message("Points: "+str(points))
            runGame = False
        # If the joystick is moved in any other direction the game asks again.
        else:
            pass


