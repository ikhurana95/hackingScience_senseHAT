######################################
#                                    #
#    Dice for Snakes and Ladders     #
#                                    #
#                                    #
######################################


import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
# from My_RPiFiles.g4cSense.graphics.senseGraphics import *
from sense_hat import SenseHat
from senseGraphics import *
from senselib import *
import random
import time
import numpy as np

sense = SenseHat()

sense.set_imu_config(False, False, True) # Enable accelerometer
sense.clear() # Clears all pixels on the screen.
yellow = (255, 255, 0)

numbers_on_dice = [1,2,3,4,5,6]

### Main loop

while True:

    ## 1.2 Check for shake

    ac = sense.get_accelerometer_raw()
    x = ac["x"]
    y = ac["y"]
    z = ac["z"]

    if x * x + y * y + z * z > 15.0:
        time.sleep(1)
    ## If a shake is detected make screen display random numbers

        ## Set dice variables
        time_between_change = 0
        start = time.time()
        run_time = 5

        ## Loop runs until the step becomes bigger than 1
        while time_between_change<1:

            #Pick a random number and diplay
            display_number = str(random.choice(numbers_on_dice))
            sense.show_letter(display_number,text_colour=randomDarkColour(),back_colour=[30,30,30])

            #Wait till next step
            wait(time_between_change)

            ##increase time between changes
            time_difference = time.time() - start
            time_between_change = newTimeStep(run_time,time_difference)


        ## Show the final letter
        sense.show_letter(display_number, text_colour=yellow,back_colour=[30,30,30])




