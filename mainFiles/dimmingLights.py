from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
s.set_imu_config(True, True, True)

r = 255
g = 255
rgbColour = [r,g,100]
def colour(rgb):
    return [rgb[0],rgb[1],rgb[2]]
    
while True:
    
    image = [colour(rgbColour) for i in range(64)]
    
    time.sleep(0.1)
    
    for event in s.stick.get_events():
      if event.action == "held":
        
        if event.direction == "left":
          if r > 5:
            r = r -5
        elif event.direction == "right":
          if r<250:
            r = r+5
        if event.direction == "down":
          if g > 5:
            g = g -5
        elif event.direction == "up":
          if g<250:
            g = g+5    
        
         
    s.set_pixels(image)
    ac = s.get_accelerometer_raw()
    x = ac["x"]
    y = ac["y"]
    z = ac["z"]
    shake = x*x + y*y + z*z
    
    if shake > 5.0:
        print(shake)
        print(colour)
        random.shuffle(rgbColour)

