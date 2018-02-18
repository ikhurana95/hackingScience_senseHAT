from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
v = [148,0,211]
i = [75, 0, 130]
b = [0,0,200]
g = [200,0,0]
y = [200,200,0]
o = [255, 127, 0]
r = [200,0,0]

rainbow = [
  
  v,v,v,i,b,b,g,g,
  v,v,i,b,b,g,g,y,
  v,i,b,b,g,g,y,y,
  i,b,b,g,g,y,y,o,
  b,b,g,g,y,y,o,o,
  b,g,g,y,y,o,o,o,
  g,g,y,y,o,o,o,r,
  g,y,y,o,o,o,r,r,
  
  ]

colour = []
for i in range(64):
  colour.append(r)
  
s.set_pixels(colour)

