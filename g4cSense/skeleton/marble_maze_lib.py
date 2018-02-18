import random
import math
import time

class MarbleMaze:
    """Stores the game variables, and helps control the game."""

    def __init__(self, sense):
        self.sense = sense
        self.sense.set_imu_config(False, True, False)

        self.maze = []
        for i in range(8):
            self.maze.append([0]*8)

        self.FLOOR = 0
        self.WALL = 1
        self.HOLE = 2
        self.GOAL = 3

        self.ballx = 0
        self.bally = 0

        self.ballvx = 0
        self.ballvx_max = 1
        self.ballvy = 0
        self.ballvy_max = 1

        self.gravity = 0.1
        self.friction = 0.03

        self.wallColour = (255, 255, 255)
        self.holeColour = (0, 0, 0)
        self.goalColour = (0, 255, 0)

    def setBallPosition(self, x, y):
        self.ballx = x
        self.bally = y
        self.ballvx = 0
        self.ballvy = 0


    def placeFloor(self, x, y):
        self.maze[x][y] = self.FLOOR

    def placeWall(self, x, y):
        self.maze[x][y] = self.WALL

    def placeHole(self, x, y):
        self.maze[x][y] = self.HOLE

    def placeGoal(self, x, y):
        self.maze[x][y] = self.GOAL

    def isHole(self, x, y):
        return self.maze[x][y] == self.HOLE

    def isGoal(self, x, y):
        return self.maze[x][y] == self.GOAL

    def isWall(self, x, y):
        return self.maze[x][y] == self.WALL

    def isFloor(self, x, y):
        return self.maze[x][y] == self.FLOOR

    def moveBallHorizontally(self, degs):
        self.ballvx -= math.sin(2 * math.pi * (degs/360.0) )*self.gravity

        if self.ballvx > 0:
            self.ballvx = min(self.ballvx, self.ballvx_max)
        else:
            self.ballvx = max(self.ballvx, -self.ballvx_max)

    def moveBallVertically(self, degs):
        self.ballvy += math.sin(2 * math.pi * (degs/360.0) )*self.gravity

        if self.ballvy > 0:
            self.ballvy = min(self.ballvy, self.ballvy_max)
        else:
            self.ballvy = max(self.ballvy, -self.ballvy_max)

    def drawWalls(self):
        for x in range(8):
            for y in range(8):
                if self.maze[x][y] == self.WALL:
                    self.sense.set_pixel(x, y, self.wallColour[0], self.wallColour[1], self.wallColour[2])

    def drawHoles(self):
        for x in range(8):
            for y in range(8):
                if self.maze[x][y] == self.HOLE:
                    self.sense.set_pixel(x, y, self.holeColour[0], self.holeColour[1], self.holeColour[2])

    def drawGoals(self):
        for x in range(8):
            for y in range(8):
                if self.maze[x][y] == self.GOAL:
                    self.sense.set_pixel(x, y, self.goalColour[0], self.goalColour[1], self.goalColour[2])

    def getBallX(self):
        return int(math.floor(self.ballx))

    def getBallY(self):
        return int(math.floor(self.bally))

    def update(self):

        ### Apply friction

        if self.ballvx != 0:
            f=0
            if self.friction <= abs(self.ballvx):
                f = self.friction
            else:
                f = abs(self.ballvx)
            self.ballvx += -f * ( self.ballvx / abs(self.ballvx) )

        if self.ballvy != 0:
            f=0
            if self.friction <= abs(self.ballvy):
                f = self.friction
            else:
                f = abs(self.ballvy)
            self.ballvy += -f * ( self.ballvy / abs(self.ballvy) )

        ### Update ball position

        newballx = self.ballx + self.ballvx
        newbally = self.bally + self.ballvy

        ### Check for wall collision

        ix = int(math.floor(newballx))
        iy = int(math.floor(newbally))

        cantmovex = False
        cantmovey = False

        if not(ix >= 0 and ix < 8):
            cantmovex = True
            ix = self.getBallX()

        if not(iy >= 0 and iy < 8):
            cantmovey = True
            iy = self.getBallY()

        if self.maze[ix][iy] == self.WALL:
            dp = (ix - self.ballx, iy - self.bally)

            # Coming from left
            if dp == (1, 0) or dp == (-1, 0):
                cantmovex = True
            elif dp == (0, 1) or dp == (0, -1):
                cantmovey = True
            else:
                self.ballvx = 0
                self.ballvy = 0
                cantmovex = True
                cantmovey = True

        if cantmovex:
            self.ballvx = 0
        else:
            self.ballx = newballx

        if cantmovey:
            self.ballvy = 0
        else:
            self.bally = newbally
