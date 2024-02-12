import pygame

class AttackLine(pygame.sprite.Sprite):
    def __init__(self, group, x=335, y=530):
        super().__init__(group)
        self.image = pygame.image.load('data1/line.png')
        self.rect = self.image.get_rect()
        self.default_x = x
        self.rect.x, self.rect.y = x, y
        self.vx = 3

    def update(self):
        self.rect.x += self.vx

    def reset(self):
        self.rect.x = self.default_x

    def get_x(self):
        return self.rect.x