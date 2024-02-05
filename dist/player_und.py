import pygame
from settings import *
from load_image import load_image

class Player_Und(pygame.sprite.Sprite):
    default_heart = pygame.image.load('data1/heart.png')
    immortal_heart = pygame.image.load('data1/immortal_heart.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Player_Und.default_heart
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = box_x + (box_width // 2) - 5, box_y + (box_height // 2) - 5
        self.immortal = False
        self.immortal_timer = None
        self.immortal_duration = 2000
        self.hp = 5

    def update(self, move):
        if move == 'left':
            self.rect = self.rect.move(-4, 0)
        if move == 'right':
            self.rect = self.rect.move(4, 0)
        if move == 'down':
            self.rect = self.rect.move(0, 4)
        if move == 'up':
            self.rect = self.rect.move(0, -4)

    def heat(self):
        if pygame.sprite.spritecollideany(self, attack1) and not self.immortal:
            self.immortal = True
            self.immortal_timer = pygame.time.get_ticks()
            self.image = Player_Und.immortal_heart
            heat_sound.play()
            if self.hp != 0:
                self.hp -= 1
            else:
                self.hp = 5
                sett.running = False

        if self.immortal:
            current_time = pygame.time.get_ticks()
            if current_time - self.immortal_timer >= self.immortal_duration:
                self.immortal = False
                self.image = Player_Und.default_heart

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_x(self, move):
        self.rect.x = move

    def set_y(self, move):
        self.rect.y = move

    def get_hp(self):
        return self.hp