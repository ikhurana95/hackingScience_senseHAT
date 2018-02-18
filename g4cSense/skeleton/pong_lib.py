import random

class Pong:
    """Stores the game variables, and helps control the game."""

    def __init__(self, sense):
        self.sense = sense

        self.player1size = 3
        self.player1pos = 1
        self.player1colour = (0, 0, 255)

        self.player2size = 3
        self.player2pos = 3
        self.player2pos_float = 3
        self.player2pos_speed = 0.6
        self.player2colour = (255, 0, 0)

        self.ballX = 3
        self.ballY = 5
        self.ballvx = random.choice([-1, 1])
        self.ballvy = random.choice([-1, 1])
        self.ballColour = (0, 255, 0)

    def updatePlayer2(self):
        """Controls player 2"""
        if self.ballY < self.player2pos:
            self.player2pos_float -= self.player2pos_speed
            self.player2pos = int(self.player2pos_float)
        elif self.ballY >= (self.player2pos + self.player2size):
            self.player2pos_float += self.player2pos_speed
            self.player2pos = int(self.player2pos_float)
