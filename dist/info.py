from PyQt5.QtCore import Qt, QPoint
from math import cos, sin, pi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from bool import sett
from settings import *
import sys
from bool import *
from player import Player
import sqlite3
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from settings import *
import pygame
import common

class Info(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('des2.ui', self)
        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()

        self.skin_index = 0
        self.skin = first_skin

        self.name = name
        self.hello_label.setText(f'Hello, {self.name}')

        self.level = self.cur.execute(f"""SELECT level FROM login
                                                    WHERE username = '{self.name}'""").fetchone()[0]

     #   self.level = list(self.level)
        if self.level == 1:
            self.level = ['1']
        else:
            print(self.level)
            self.level = self.level.split(',')
            print(self.level)


        print(type(self.level))
    #    print(self.level)
        self.level_label.setText(f'Levels: {len(self.level)}')
        self.all_levels_count = len(self.level)

        sett.file = open(f'levels/{self.all_levels_count}.txt', mode='r')
        sett.lev = sett.file.readlines()
        sett.level = []
        for el in sett.lev:
            res = ''
            for elem in el:
                if elem == '\n' or elem == '':
                    pass
                else:
                    res += elem
            sett.level.append(res)


        self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
        self.photo_label.setPixmap(self.pixmap)


        self.background_pixmap = QPixmap(f"graphics/background/{sett.background_count}/sky_back.jpg")
        self.back_label.setPixmap(self.background_pixmap)

        self.record = self.cur.execute(f"""SELECT record FROM login
                                             WHERE username = '{self.name}'""").fetchone()[0]
        self.record_label.setText(f'Record:  {self.record}')

        self.coins = self.cur.execute(f"""SELECT coins FROM login
                                             WHERE username = '{self.name}'""").fetchone()[0]
        self.coins_label.setText(f'Coins:  {self.coins}')

        sett.count_coins = int(self.coins)

        self.sky_surface = load_image(f'graphics/background/{sett.background_count}/sky.jpg')
        self.ground_surface = load_image(f'graphics/background/{sett.background_count}/grass.png')

        self.start_Button.clicked.connect(self.start)
        self.choose_Button.clicked.connect(self.choose)
        self.next_Button.clicked.connect(self.next)
        self.back_Button.clicked.connect(self.back)
        self.morecoins_Button.clicked.connect(self.more_coins)





    def closeEvent(self, event):
            event.accept()

    def start(self):
        obstacle_group.empty()
        player.empty()
        sett.pl = Player(self.skin)
        player.add(sett.pl)
        sett.count_level = 0
        sett.game_active = True
        sett.start_time = int(pygame.time.get_ticks() / 1000)


    def update(self):
        if sett.score > int(self.record) and not sett.mini_game:
            self.record = sett.score
            self.cur.execute(f"""UPDATE login
                             SET record = '{self.record}'
                            WHERE username = '{self.name}'""")
            self.con.commit()
            self.record_label.setText(f'Record:  {self.record}')
            self.coins = str(sett.count_coins)
            self.coins_label.setText(f'Coins:  {self.coins}')
            self.cur.execute(f"""UPDATE login
                                         SET coins = '{self.coins}'
                                        WHERE username = '{self.name}'""")

        if sett.all_levels_count < len(self.level):
           sett.all_levels_count = len(self.level)
           self.cur.execute(f"""UPDATE login
                                        SET level = '{','.join(self.level)}'
                                        WHERE username = '{self.name}'""")


        elif sett.mini_game:
            print(int(self.coins))
            print(int(sett.score_coins))
            self.coins = int(self.coins)
            self.coins += int(sett.score_coins)
            self.coins = str(self.coins)
            self.coins_label.setText(f'Coins:  {self.coins}')
            self.cur.execute(f"""UPDATE login
                                                SET coins = '{self.coins}'
                                               WHERE username = '{self.name}'""")
            sett.mini_game = False

        self.con.commit()




    def mousePressEvent(self, event):
        x = int(str(event.pos()).split('(')[1].split(',')[0])
        beta_y = str(event.pos()).split('(')[1].split(',')[1]
        y = ''
        for el in beta_y:
            if el.isdigit():
                y += el
        y = int(y)
        if 270 <= x <= 341 and 210 <= y <= 281:
            if self.skin_index != len(all_skins) - 1:
                self.skin_index += 1
                self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
                self.photo_label.setPixmap(self.pixmap)
            else:
                self.skin_index = 0
                self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
                self.photo_label.setPixmap(self.pixmap)
        elif 260 <= x <= 601 and 320 <= y <= 451:
            if sett.background_count != len(sett.background_note):
                sett.background_count += 1
                self.background_pixmap = QPixmap(f"graphics/background/{sett.background_count}/sky_back.jpg")
                self.back_label.setPixmap(self.background_pixmap)
                self.sky_surface = load_image(f'graphics/background/{sett.background_count}/sky.jpg')
                self.ground_surface = load_image(f'graphics/background/{sett.background_count}/grass.png')
            else:
                sett.background_count = 1
                self.background_pixmap = QPixmap(f"graphics/background/{sett.background_count}/sky_back.jpg")
                self.back_label.setPixmap(self.background_pixmap)
                self.sky_surface = load_image(f'graphics/background/{sett.background_count}/sky.jpg')
                self.ground_surface = load_image(f'graphics/background/{sett.background_count}/grass.png')




    def choose(self):
        if self.skin_index == 0:
            print('ssssss')
            self.skin = first_skin
        if self.skin_index == 1:
            print('oooooooooo')
            self.skin = second_skin
        if self.skin_index == 2:
            print('oooooooooo')
            self.skin = third_skin
        obstacle_group.empty()
        player.empty()
        sett.pl = Player(self.skin)
        player.add(sett.pl)

    def next(self):
        sett.first = True
        print(self.all_levels_count)
        if self.all_levels_count != len(self.level):
            self.all_levels_count = self.all_levels_count + 1
            self.level_label.setText(f'Levels: {self.all_levels_count}')
            sett.file = open(f'levels/{self.all_levels_count}.txt', mode='r')
            sett.lev = sett.file.readlines()
            sett.level = []
            for el in sett.lev:
                res = ''
                for elem in el:
                    if elem == '\n' or elem == '':
                        pass
                    else:
                        res += elem
                sett.level.append(res)
        else:
            pass

    def back(self):
        sett.first = False
        print(self.all_levels_count)
        if self.all_levels_count != 1:
            self.all_levels_count = self.all_levels_count - 1
            self.level_label.setText(f'Levels: {self.all_levels_count}')
            sett.file = open(f'levels/{self.all_levels_count}.txt', mode='r')
            sett.lev = sett.file.readlines()
            sett.level = []
            for el in sett.lev:
                res = ''
                for elem in el:
                    if elem == '\n' or elem == '':
                        pass
                    else:
                        res += elem
                sett.level.append(res)
        else:
            pass

    def more_coins(self):
        common.function()
        sett.mini_game = True















