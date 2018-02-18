import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
# from My_RPiFiles.g4cSense.skeleton.snakes_ladders_lib_multi import *
# from My_RPiFiles.g4cSense.skeleton.senselib import *
# from My_RPiFiles.g4cSense.graphics.senseGraphics import *
from senseGraphics import *
from snakes_ladders_lib_multi import *
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
##Player Variables
game.addPlayer(0,7)
game.addPlayer(0,7)

game.setBoard()


snakes = game.getSnakes()
ladders = game.getLadders()
players = game.getPlayers()


##Cursor
cursorPositionX = 0
cursorPositionY = 7
cursorColour = [255,255,255]

##Main Loop

while True:
    for player in players:

        turnPlayed = False
        image = sense.get_pixels()

        while not turnPlayed:
            for event in sense.stick.get_events():
                ##Add cursor
                sense.set_pixels(image)
                sense.set_pixel(cursorPositionX, cursorPositionY, cursorColour)

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
                        player.setPlayerPosition(cursorPositionX,cursorPositionY)
                        game.setBoard()
                        image = sense.get_pixels()

                        turnPlayed = True



        ### Check if player is on a snake head
        checkingSnakes = True
        while checkingSnakes:

            for snake in snakes:
                snakeHead = snake.getHead()
                snakeTail = snake.getTail()

                if player.positionX == snakeHead[0] and player.positionY == snakeHead[1]:
                    player.positionX = snakeTail[0]
                    player.positionY = snakeTail[1]

                    game.setBoard()
                    image = sense.get_pixels()
                    checkingSnakes = True
                    break
                else:
                    checkingSnakes = False



        checkingLadders = True
        while checkingLadders:

            for ladder in ladders:
                ladderTop = ladder.getTop()
                ladderFoot = ladder.getFoot()

                if player.positionX == ladderFoot[0] and player.positionY == ladderFoot[1]:
                    player.positionX = ladderTop[0]
                    player.positionY = ladderTop[1]


                    game.setBoard()
                    image = sense.get_pixels()
                    checkingLadders = True
                    break
                else:
                    checkingLadders = False


