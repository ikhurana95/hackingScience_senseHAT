
import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from sense_hat import SenseHat
import random
from senselib import *
import numpy as np
import time
#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(False, False, True) # Enable accelerometer
sense.clear() # Clears all pixels on the screen.



def acceleration(sense):
    ac = sense.get_accelerometer_raw()
    x = ac["x"]
    y = ac["y"]
    z = ac["z"]
    accel = np.sqrt(x**2 + y**2 + z**2)
    return accel

reading = False
accel = []
green = [[0,255,0] for i in range(64)]
sense.show_message("ready")
time.sleep(0.3)
sense.set_pixels(green)

start = time.time()
end = start + 2
while time.time()<end:
    reading = False

    while acceleration(sense) > 1:
        accel.append(acceleration(sense))
        print(acceleration(sense))
        reading = True


if reading:
    meanAccel = np.mean(accel)
    sense.show_message("gravity is: " + str(meanAccel))
