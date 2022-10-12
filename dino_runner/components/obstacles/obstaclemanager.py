from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from .smallcactus import SmallCactus
from .largecactus import LargeCactus
from .bird import Bird
import random
import pygame


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
        colision = pygame.sprite.spritecollide(game.player, self.obstacles, False)
        if colision:
            pygame.time.delay(1000)
            game.playing = False


    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)