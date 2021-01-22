import numpy as np


class Player:
    def __init__(self, height=5, max_width=10, width=2,
                 x=0, y=0, speed=2):
        self.height = height
        self.max_width = max_width
        self.width = width
        self.x = x
        self.y = y
        self.speed = speed
        self.body_unit = 2
        self.body = np.ones(shape=(self.height, self.width))*self.body_unit
        self.stamina = 20
        self.max_stamina = 20

    def move(self, field, direction=0):
        '''
        Moves the player :
         - No change          = 0
         - left, if direction  = 1
         - right, if direction = 2
        '''
        val2dir = {0: 0, 1: -1, 2: 1}
        direction = val2dir[direction]
        next_x = (self.x + self.speed*direction)
        if not (next_x + self.width > field.width or next_x < 0):
            self.x += self.speed*direction
            self.stamina -= 1

    def change_width(self, action=0):
        '''
        Change the player's width:
         - No change          = 0
         - narrow by one unit = 3
         - widen by one unit  = 4
        '''
        val2act = {0: 0, 3: -1, 4: 1}
        action = val2act[action]
        new_width = self.width+action
        player_end = self.x + new_width
        if new_width <= self.max_width and new_width > 0 and player_end <= self.max_width:
            self.width = new_width
            self.body = np.ones(shape=(self.height, self.width))*self.body_unit
