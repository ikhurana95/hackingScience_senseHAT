import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
# from My_RPiFiles.g4cSense.skeleton.snakes_ladders_lib import *
# from My_RPiFiles.g4cSense.skeleton.senselib import *
# from My_RPiFiles.g4cSense.graphics.senseGraphics import *
from senseGraphics import *
from snakes_ladders_lib import *
from sense_hat import SenseHat

##Initialise
sense = SenseHat()
game = snakesLadders(sense)

game.setBoardColour([175,175,50])
game.addSnake(4,0,3,2)
game.addSnake(3,6,5,7)
game.addSnake(6,5,0,6)
game.addSnake(4,4,3,6)
game.addLadder(7,4,4,5)
game.addLadder(5,1,2,3)
game.addLadder(5,2,2,4)


game.setBoard()


snakes = game.getSnakes()
ladders = game.getLadders()
##Player Variables


##Player 1
playerPostionX = 0
playerPositionY = 7
playerColour = [100,255,100]

##Player 2

##Cursor
cursorPositionX = 0
cursorPositionY = 7
cursorColour = [255,255,255]


image = sense.get_pixels() # Save the sreen as it is for now
sense.set_pixel(cursorPositionX,cursorPositionY,cursorColour)
##Main Loop

while True:

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                cursorPositionY -= 1
                if cursorPositionY < 0:
                    cursorPositionY = 7
            elif event.direction == "down":
                cursorPositionY += 1
                if cursorPositionY > 7:
                    cursorPositionY = 0
            elif event.direction == "left":
                cursorPositionX -= 1
                if cursorPositionX < 0:
                    cursorPositionX = 7
            elif event.direction == "right":
                cursorPositionX += 1
                if cursorPositionX > 7:
                    cursorPositionX = 0

            elif event.direction == "middle":
                playerPostionX = cursorPositionX
                playerPositionY = cursorPositionY

                game.setBoard()
                sense.set_pixel(playerPostionX,playerPositionY,playerColour)
                image = sense.get_pixels()

        ### Check if player is on a snake head

        for snake in snakes:
            snakeHead = snake.getHead()
            snakeTail = snake.getTail()

            if playerPostionX == snakeHead[0] and playerPositionY == snakeHead[1]:
                playerPostionX = snakeTail[0]
                playerPositionY = snakeTail[1]

                game.setBoard()
                sense.set_pixel(playerPostionX,playerPositionY,playerColour)
                image = sense.get_pixels()

                break #Optional line



        for ladder in ladders:
            ladderTop = ladder.getTop()
            ladderFoot = ladder.getFoot()

            if playerPostionX == ladderFoot[0] and playerPositionY == ladderFoot[1]:
                playerPostionX = ladderTop[0]
                playerPositionY = ladderTop[1]


                game.setBoard()
                sense.set_pixel(playerPostionX, playerPositionY, playerColour)
                image = sense.get_pixels()

                break  # Optional line

        ##Add cursor
        sense.set_pixels(image)
        sense.set_pixel(cursorPositionX,cursorPositionY,cursorColour)

        ##