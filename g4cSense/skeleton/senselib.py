import time,sys


sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from senseGraphics import *
import numpy as np

sense = None
events = None

def initialise(_sense):
    global sense
    sense = _sense

def drawHorizontalLine(x0, y0, size, r, g, b):
    """ Draws a horizontal line on the screen.
    Args:
    x,y  (int): The starting position of the line.
    size (int): The number of pixels on the line, can be negative size.
    r,g,b ((int, int, int)): The color of the line, in RGB.
    """

    if size < 0:
        x0 += size + 1
        size = -size

    for x in range(x0, x0+size):
        if not isCoordinateOnScreen( (x, y0) ):
            continue

    sense.set_pixel(x, y0, r, g, b)

def drawVerticalLine(x0, y0, size, r, g, b):
    """ Draws a vertical line on the screen.
    Args:
    x,y  (int): The starting position of the line.
    size (int): The number of pixels on the line, can be negative size.
    r,g,b ((int, int, int)): The color of the line, in RGB.
    """

    if size < 0:
        y0 += size + 1
        size = -size

    for y in range(y0, y0+size):
        if not isCoordinateOnScreen( (x0, y) ):
            continue
        sense.set_pixel(x0, y, r, g, b)

def isCoordinateOnScreen(c):
    """Returns true if the coordinate c (int, int) is a valid coordinate on the
    screen
    """
    x,y = c

    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    else:
        return True

def wait(seconds):
    """Waits the given amount of seconds."""
    time.sleep(seconds)

def draw_two_digit_number(num, r, g, b):
    num_pics = [
        [1,1,1,
         1,0,1,
         1,0,1,
         1,0,1,
         1,1,1],
        [0,0,1,
         0,0,1,
         0,0,1,
         0,0,1,
         0,0,1],
        [1,1,1,
         0,0,1,
         1,1,1,
         1,0,0,
         1,1,1],
        [1,1,1,
         0,0,1,
         0,1,1,
         0,0,1,
         1,1,1],
        [1,0,1,
         1,0,1,
         1,1,1,
         0,0,1,
         0,0,1],
        [1,1,1,
         1,0,0,
         1,1,1,
         0,0,1,
         1,1,1],
        [1,1,1,
         1,0,0,
         1,1,1,
         1,0,1,
         1,1,1],
        [1,1,1,
         0,0,1,
         0,0,1,
         0,0,1,
         0,0,1],
        [1,1,1,
         1,0,1,
         1,1,1,
         1,0,1,
         1,1,1],
        [1,1,1,
         1,0,1,
         1,1,1,
         0,0,1,
         0,0,1]
      ]

    numstr = str(num)
    numbers = "0123456789"



    if len(numstr) == 1:
        posx = 0 + 4
        posy = 3
    elif len(numstr) == 2:
        posx = 0
        posy = 3
    else:
        raise Exception('Wrong number size.')

    for c in numstr:
        num_img = num_pics[ numbers.index(c) ]

        for x in range(3):
            for y in range(5):
                if num_img[y*3 + x] == 1:

                    sense.set_pixel(x + posx, y + posy, r, g, b)
        posx += 4





def show_numbers(number, text_colour=None):
    """
    Sets the pixels to the number given.
    Allows display of numbers up to 12 for Lucky 7 game.

    :param number: The number to be shown
    """

    if text_colour == None:
        text_colour = [255, 255, 255]

    if number < 10:

        sense.show_letter(str(number), text_colour=text_colour)
    elif number < 13:
        if number == 10:
            sense.set_pixels(ten(text_colour))
        elif number == 11:
            sense.set_pixels(eleven(text_colour))
        elif number == 12:
            sense.set_pixels(twelve(text_colour))


def newTimeStep(run_time,time):
    return 0.1 * (1 + np.exp(time - run_time) ** 3)
