import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/graphics')
from sense_hat import SenseHat
# from My_RPiFiles.g4cSense.graphics.senseGraphics import *

from senseGraphics import *
from senselib import *
from copy import deepcopy
import random
import time
import numpy as np

reds = getColour('red')
random.shuffle(reds)
blues = getColour('blue')
green = [0,200,0]

class snakesLadders():
    """
    Creates the board and holds variables that control the game.
    """

    def __init__(self, sense):
        self.board = []
        self.snakes = []
        self.ladders = []
        self.players = []

        self.sense = sense
        self.sense.clear()
        self.boardColour = [0,0,0]
    def setBoardColour(self,colour):
        self.boardColour = colour

    ###Adding snakes ladders and players

    def addSnake(self,headX,headY,tailX,tailY):

        self.snakes.append(snake(headX,headY,tailX,tailY))

    def addLadder(self,headX,headY,tailX,tailY):
        self.ladders.append(ladder(headX,headY,tailX,tailY))


    def addPlayer(self,player):
        self.players.append(player)


    ## Getter methods

    def getPlayers(self):

        return self.players

    def getSnakes(self):

        return deepcopy(self.snakes)


    def getLadders(self):
        return deepcopy(self.ladders)



    def setBoard(self):
        """
        Function called when a new snake or ladder
        :return:
        """
        newBoard = []

        for j in range(8):
            for i in range(8):
                snakeFound = False
                ladderFound = False

                for snake in self.snakes:
                    snakeHead = snake.getHead()
                    snakeTail = snake.getTail()

                    if i == snakeHead[0] and j == snakeHead[1]:
                        newBoard.append(snake.colour)
                        snakeFound = True
                        break


                    elif i == snakeTail[0] and j == snakeTail[1]:
                        newBoard.append(snake.colour)
                        snakeFound = True
                        break



                if not snakeFound:
                    for ladder in self.ladders:

                        ladderHead = ladder.getTop()
                        ladderTail = ladder.getFoot()

                        if i == ladderHead[0] and j == ladderHead[1]:
                            newBoard.append(ladder.colour)
                            ladderFound = True
                            break

                        elif i == ladderTail[0] and j == ladderTail[1]:
                            newBoard.append(ladder.colour)
                            ladderFound = True
                            break


                if not ladderFound and not snakeFound:
                    newBoard.append(self.boardColour)




        self.board = newBoard
        self.sense.set_pixels(self.board)

        for j in range(8):
            for i in range(8):

                for player in self.players:
                    if i == player.positionX and j == player.positionY:
                        print("setting player with colour", player.pieceColour)
                        self.sense.set_pixel(i, j, [0,0,0])
                        self.sense.set_pixel(i,j,player.pieceColour)




class snake():

    snakeNumber = 0

    def __init__(self, headX,headY,tailX,tailY):

        self.head = [headX,headY]
        self.tail = [tailX,tailY]
        self.colour = reds[snake.snakeNumber]
        # self.colour = [255,0,0]
        snake.snakeNumber +=1

    def getTail(self):
        return deepcopy(self.tail)


    def getHead(self):
        return deepcopy(self.head)


class ladder():

    ladderNumber = 0
    def __init__(self, headX,headY,tailX,tailY):
        global ladderNumber
        self.head = [headX,headY]
        self.tail = [tailX,tailY]
        self.colour = blues[ladder.ladderNumber]
        # self.colour = [0,0,255]
        ladder.ladderNumber +=1

    def getFoot(self):
        return deepcopy(self.tail)


    def getTop(self):
        return deepcopy(self.head)


class player():

    def __init__(self, colour = None):

        self.positionX = 0
        self.positionY = 7
        if colour == None:
            randomGreenColour = randomGreen()
            print(type(randomGreenColour))
            self.pieceColour = randomGreenColour
        else:
            self.pieceColour = colour

    def setPlayerPosition(self,xPosition,yPosition):

        self.positionY = yPosition
        self.positionX = xPosition

    def getPlayerPositionX(self):

        return deepcopy(self.positionX)


    def getPlayerPositionY(self):

        return deepcopy(self.positionY)

