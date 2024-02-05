import pygame
from random import randint
from load_image import load_image
from sprites import AnimatedSprite
from settings import *
class Coins(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()


        self.data = type
        if type == coin:
            y_pos = randint(400, 600)


        elif type == white_bird:
            y_pos = 350

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