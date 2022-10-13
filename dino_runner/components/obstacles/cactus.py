from .obstacle import Obstacle
import random


class Cactus(Obstacle):

    def __init__(self, images, value_y):
        self.type = random.randint(0, 2)
        super().__init__(images, self.type)
        self.rect.y = value_y #325 small cactus -- 300 large cactus