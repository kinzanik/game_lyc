from load_image import load_image
import pygame
#from settings import *
class Bool:
    def __init__(self):
        self.game_active = False
        self.log_in = False
        self.info = False
        self.board = False
        self.start_time = 0
        self.score = 0
        self.pl = ''
        self.count_level = 0
        self.count_coins = 0
        self.all_levels_count = 1
        self.background_count = 1
        self.background_note = [1, 2, 3]
        self.file = open(f'levels/{self.all_levels_count}.txt', mode='r')
        self.lev = self.file.readlines()
        self.level = []
        self.first = True
        for el in self.lev:
            res = ''
            for elem in el:
                if elem == '\n' or elem == '':
                    pass
                else:
                    res += elem
            self.level.append(res)
        self.activate_levels = 1
        self.running = False

        self.screen = pygame.display.set_mode((1200, 800))


    def update(self):
        if self.running:
            pass

        if self.game_active:
            self.screen = pygame.display.set_mode((1200, 800))
        else:
            self.screen = pygame.display.set_mode((1200, 800))


sett = Bool()