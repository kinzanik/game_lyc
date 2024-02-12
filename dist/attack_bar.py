import pygame

class AttackBar(pygame.sprite.Sprite):
    def __init__(self, group, x=335, y=530):
        super().__init__(group)
        self.image = pygame.image.load('data1/trash.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y