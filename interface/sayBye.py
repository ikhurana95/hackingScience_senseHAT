import sys
from sense_hat import SenseHat
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')

from senseGraphics import *
sense = SenseHat()

red = colour('pastel_red')

sense.show_message("Main Menu", scroll_speed=0.08,text_colour=red)

