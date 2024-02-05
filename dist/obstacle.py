import pygame
from random import randint
from load_image import load_image
from sprites import AnimatedSprite
from settings import *
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()


        self.data = type
        if type == bat:
            y_pos = 600
        elif type == bat_high:
            y_pos = 540
        elif type == bird:
            y_pos = 400
        elif type == lower_bird:
            y_pos = 540
        elif type == wolf:
            y_pos = 600
        elif type == pig:
            y_pos = 600
        elif type == horse:
            y_pos = 560

        elif type == white_bird:
            y_pos = 550

        else:
            snail_1 = pygame.image.load('graphics/diplom.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/diplom.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 600


        self.image = self.data.frames[self.data.cur_frame]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.image = self.data.frames[self.data.cur_frame]

    def update(self):
        self.animation_state()
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()