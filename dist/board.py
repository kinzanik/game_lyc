import pygame
from random import randint
from settings import *
class Board(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.y_pos = 400


        if type == board:
            self.y_pos = 400
        elif type == grass:
            self.y_pos = 800
        self.animation_index = 0
        self.image = self.type = type
        if type == grass:
            self.rect = self.image.get_rect(midbottom=(0, self.y_pos))
        else:
            self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.y_pos))

    def animation_state(self):
        pass


    def update(self):
        self.animation_state()

        self.rect.x -= 6
        self.destroy()

    def destroy(self):

        if self.rect.x <= -100:
            self.kill()