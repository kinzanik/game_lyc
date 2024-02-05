import pygame
from settings import *

class DrawEnemy(pygame.sprite.Sprite):
    def __init__(self, group, name, x=(box_x + box_width // 2 - 90), y=100):
        super().__init__(group)
        self.a = 1
        self.name = name
        self.count_frames = 2
        if self.name.lower() == 'nerdlin':
            self.image_text = 'data1/Nerdlin'
            self.image = pygame.image.load(f'{self.image_text}{self.count_frames}.png')
        elif self.name.lower() == 'ghost':
            self.image_text = 'data1/ghost1'
            self.image = pygame.image.load(f'{self.image_text}.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        if self.name.lower() == 'ghost':
            return
        if self.a % 30 == 0 and self.count_frames == 1:
            self.count_frames = 2
        elif self.a % 30 == 0 and self.count_frames == 2:
            self.count_frames = 1
        path = f'{self.image_text}{self.count_frames}.png'
        self.image = pygame.image.load(path)
        self.a += 1