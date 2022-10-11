from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING
import pygame


class Dinosaur(Sprite):

    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.step_index = 0
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_velocity = self.JUMP_VELOCITY
        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False


    def update(self, key_pressed):
        if self.is_ducking:
            self.duck()
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if key_pressed[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.is_ducking = False
            self.is_running = False
        elif key_pressed[pygame.K_DOWN] and not self.is_jumping:
            self.is_ducking = True
            self.is_running = False
            self.is_jumping = False
        elif not (self.is_jumping or key_pressed[pygame.K_DOWN]):
            self.is_running = True
            self.is_jumping = False
            self.is_ducking = False
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    
    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.is_jumping = False

    
    def duck(self):
        self.image = DUCKING[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1