from .obstacle import Obstacle
import random


class LargeCactus(Obstacle):

    def __init__(self, images):
        self.type = random.randint(0, 2)
        super().__init__(images, self.type)
        self.rect.y = 300