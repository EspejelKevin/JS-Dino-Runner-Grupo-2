from pygame.sprite import Sprite
from dino_runner.utils.constants import FONT, SOUNDS_DIR
import pygame
import os


class Score(Sprite):

    def __init__(self):
        self.score = 0


    def update(self, game):
        self.score += 1
        if self.score % 500 == 0:
            sound_jump = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "point.ogg"))
            sound_jump.play()
            game.game_speed += 3


    def draw(self, screen):
        font = pygame.font.Font(FONT, 30)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)