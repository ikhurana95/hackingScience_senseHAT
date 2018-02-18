import random

class Snake:

    def __init__(self, position):
        self.body = [position]
        self.will_grow = False
        self.direction = 0 # 0 up, 1 right, 2 down, 3 left
        self.moves = [ [0, -1], [1, 0], [0, 1], [-1, 0] ]
        self.game_size = [8,8]

    def grow(self):
        """Makes the snake larger"""
        self.will_grow = True

    def move_forward(self):
        """Moves the snake and its body parts one step forward"""
        new = [0, 0]
        new[0] =  (self.body[0][0] + self.moves[self.direction][0]) % self.game_size[0]
        new[1] = (self.body[0][1] + self.moves[self.direction][1]) % self.game_size[1]

        self.body.insert(0, new)

        if self.will_grow:
            self.will_grow = False
        else:
            self.body.pop()

    def turn_up(self):
        """Points the snake upwards"""
        self.direction = 0

    def turn_right(self):
        """Points the snake to the right"""
        self.direction = 1

    def turn_down(self):
        """Points the snake downwards"""
        self.direction = 2

    def turn_left(self):
        """Points the snake to the left"""
        self.direction = 3

    def get_position(self):
        """Returns the position of the snake's head"""
        return self.body[0]

    def has_collided_with_self(self):
        """Checks if the snake has collided with itself"""
        collided = False

        for i in range(len(self.body)):
            for j in range(i+1, len(self.body)):
                if self.body[i][0] == self.body[j][0] and self.body[i][1] == self.body[j][1]:
                    collided = True

        return collided

    def get_body(self):
        """Returns a list containing the position of the snake's body parts."""
        return self.body[:]

    def get_new_apple_position(self):
        """Returns a new position that the apple could be placed at"""
        apple_position = [random.randint(0, self.game_size[0]-1), random.randint(0, self.game_size[1]-1)]

        valid = False
        while not valid:

            valid = True
            for b in self.body:
                if b[0] == apple_position[0] and b[1] == apple_position[1]:
                    apple_position = [random.randint(0, self.game_size[0]-1), random.randint(0, self.game_size[1]-1)]
                    valid = False

        return apple_position

    def reset(self):
        """Resets the snake so that it only consists of its head"""
        self.body = [self.body[0]]
