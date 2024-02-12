import pygame
from load_image import load_image
from bool import *
class Player(pygame.sprite.Sprite):
    def __init__(self, skin):
        super().__init__()
        self.skin = skin
        self.image = skin[0].frames[skin[0].cur_frame]
        self.player_jump = skin[1].frames[skin[0].cur_frame]
        self.rect = self.image.get_rect(midbottom=(200, 570))
        self.gravity = 0


     #   self.jump_sound = pygame.mixer.Sound('music/menu_music.mp3')
     #   self.jump_sound.set_volume(0.5)


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 570:
            self.gravity = -21.5

       #     self.jump_sound.play()

    def board_player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 340:
            self.gravity = -17
      #      self.jump_sound.play()

    def board_up_player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 90:
            self.gravity = -13
     #       self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 570:
            sett.board = False
            self.rect.bottom = 570

    def board_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 350:
            self.rect.bottom = 350

    def board_up_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 100:
            self.rect.bottom = 100


    def animation_state(self):

        if self.rect.bottom < 570:
            self.image = self.skin[1].frames[self.skin[0].cur_frame]
        else:
           self.image = self.skin[0].frames[self.skin[0].cur_frame]

    def board_animation_state(self):
        if self.rect.bottom == 350:
            self.image = self.skin[0].frames[self.skin[0].cur_frame]
        else:
            self.image = self.skin[1].frames[self.skin[0].cur_frame]

    def board_up_animation_state(self):
        if self.rect.bottom < 100:
            self.image = self.skin[1].frames[self.skin[0].cur_frame]
        else:
            self.image = self.skin[0].frames[self.skin[0].cur_frame]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

    def update_board(self):
        sett.board = True
        if self.rect.y < 380:
            self.board_player_input()
            self.board_gravity()
            self.board_animation_state()
        else:
            self.rect.y = 410

    def update_board_up(self):
        self.board_up_player_input()
        self.board_up_gravity()
        self.board_up_animation_state()