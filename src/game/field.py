import numpy as np


class Field:
    def __init__(self, height=10, width=5):
        self.width = width
        self.height = height
        self.body = np.zeros(shape=(self.height, self.width))

    def update_field(self, walls, player):
        try:
            # Clear the field:
            self.body = np.zeros(shape=(self.height, self.width))
            # Put the walls on the field:
            for wall in walls:
                if not wall.out_of_range:
                    self.body[wall.y:min(
                        wall.y+wall.height, self.height), :] = wall.body

            # Put the player on the field:
            self.body[player.y:player.y+player.height,
                      player.x:player.x+player.width] += player.body
        except:
            pass
