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

boardColour = [150,150,0]
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

        self.sense = sense
        self.sense.clear()

    def addSnake(self,headX,headY,tailX,tailY):

        self.snakes.append(snake(headX,headY,tailX,tailY))
        self.setBoard()

    def addLadder(self,headX,headY,tailX,tailY):
        self.ladders.append(ladder(headX,headY,tailX,tailY))
        self.setBoard()


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
                        print('snakeHead')
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
                    newBoard.append(boardColour)




        self.board = newBoard
        self.sense.set_pixels(self.board)




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

