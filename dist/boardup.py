import pygame
from random import randint
class BoardUp(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

        if type == 'board':
            fly_1 = pygame.image.load('graphics/board.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/board.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 110
        elif type == 'board1':
            fly1_1 = pygame.image.load('graphics/board1.png').convert_alpha()
            fly1_2 = pygame.image.load('graphics/board1.png').convert_alpha()
            self.frames = [fly1_1, fly1_2]
            y_pos = 110
        else:
            snail_1 = pygame.image.load('graphics/ground.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/ground.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 1000
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()