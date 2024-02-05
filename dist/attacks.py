import pygame
import random as r
from settings import *

class Attack1(pygame.sprite.Sprite):
    def __init__(self, group, vector):
        super().__init__(group)
        self.vector = vector
        self.name = 'peaks'
        self.image = pygame.image.load(f'data1/attack_sprite1_{vector}.png')
        self.rect = self.image.get_rect()
        if self.vector == 'down':
            self.rect.x = r.randint((width - box_width) // 2, (width - box_width) // 2 + 180)
            self.rect.y = (height - box_height) // 2 + 5
        elif self.vector == 'up':
            self.rect.x = r.randint((width - box_width) // 2, (width - box_width) // 2 + 180)
            self.rect.y = (box_height + box_y)
        elif self.vector == 'right':
            self.rect.x = box_x
            self.rect.y = r.randint(box_y, box_y + 170)
        elif self.vector == 'left':
            self.rect.x = box_x + 200 - 30
            self.rect.y = r.randint(box_y, box_y + 170)

    def update(self):
        if self.vector == 'down':
            self.rect = self.rect.move(0, 3)
        elif self.vector == 'up':
            self.rect = self.rect.move(0, -3)
        elif self.vector == 'right':
            self.rect = self.rect.move(3, 0)
        elif self.vector == 'left':
            self.rect = self.rect.move(-3, 0)

    def get_vector(self):
        return self.vector

    def get_name(self):
        return self.name

class Attack2(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.name = 'ball'
        self.image = pygame.image.load('data1/attack_sprite2.png')
        self.rect = self.image.get_rect()
        self.vx = 0
        self.touch = 0
        self.broken = 4
        while self.vx == 0:
            self.vx = r.randint(-2, 2)
        pos = r.randint(0, 1)
        if pos == 0:
            self.rect.x = r.randint(box_x + 20, box_x + box_width - 20)
            self.rect.y = box_y + 3
            self.vy = 2
        elif pos == 1:
            self.rect.x = r.randint(box_x + 20, box_x + box_width - 20)
            self.rect.y = box_y + box_height - 15
            self.vy = r.randint(-2, -1)

    def update(self):
        if self.touch >= 3:
            self.broken += 1
        if self.broken % 5 == 0:
            self.image = pygame.image.load(f'data1/broken_ball{self.broken // 5}.png')
            self.broken += 1
        if self.broken < 5:
            if self.rect.x <= box_x or self.rect.x >= box_x + box_width - 14:
                self.vx *= -1
                self.touch += 1
            elif self.rect.y <= box_y + 2 or self.rect.y >= box_y + box_height - 14:
                self.vy *= -1
                self.touch += 1
            self.rect = self.rect.move(self.vx, self.vy)

    def get_name(self):
        return self.name

    def get_touch(self):
        return self.touch

    def get_broken(self):
        return self.broken

class Attack3(pygame.sprite.Sprite):
    def __init__(self, group, y, move):
        super().__init__(group)
        self.name = 'bone'
        self.image = pygame.image.load('data1/bone.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = box_x + 200, y
        self.move = move
        if self.move == 'right':
            self.vx = 3
            self.rect.x, self.rect.y = box_x, y
        elif self.move == 'left':
            self.rect.x, self.rect.y = box_x + 200, y
            self.vx = -3

    def update(self):
        self.rect.x += self.vx

    def get_name(self):
        return self.name

    def get_vector(self):
        return self.move

class Attack4(pygame.sprite.Sprite):
    def __init__(self, group, x, y, posx, posy):
        super().__init__(group)
        self.name = 'block'
        self.image = pygame.image.load('data1/block.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x + posx * 20, y - posy * 20
        self.vy = 3
        self.posx, self.posy = posx, posy
        self.is_update = True
        self.is_blink = 1
        self.is_ban = False
        self.blink_count = 0

    def update(self):
        if not self.is_update:
            return
        block = 0
        for i in tetris:
            if i[self.posx] == 1:
                block += 1
            else:
                break
        if self.rect.y <= box_y + box_height - 23 - 20 * block:
            self.rect.y += self.vy
        else:
            tetris[self.posy][self.posx] = 1
            self.is_update = False

    def blink(self):
        if self.is_blink == 1:
            self.image = pygame.image.load('data1/empty_block.png')
            self.blink_count += 1
        else:
            self.image = pygame.image.load('data1/block.png')

        if self.blink_count == 3:
            self.is_ban = True
        self.is_blink *= -1

    def get_name(self):
        return self.name

    def get_is_ban(self):
        return self.is_ban