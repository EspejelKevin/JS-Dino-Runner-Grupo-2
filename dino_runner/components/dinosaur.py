from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import RUNNING
import pygame


class Dinosaur(Sprite):

    Y_POS = 310
    X_POS = 80
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.is_running = True
        self.is_jumping = False


    def update(self, key_pressed):
        if self.is_running:
            self.run()
        elif self.is_jumping:
            self.jump()

        if key_pressed[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.is_running = False
        elif not self.is_jumping:
            self.is_jumping = False
            self.is_running = True
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
            self.is_jumping = False