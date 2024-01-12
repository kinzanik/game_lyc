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


        self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
        self.photo_label.setPixmap(self.pixmap)

        self.record = self.cur.execute(f"""SELECT record FROM login
                                             WHERE username = '{self.name}'""").fetchone()[0]
        self.record_label.setText(f'Record:  {self.record}')

        self.start_Button.clicked.connect(self.start)
        self.choose_Button.clicked.connect(self.choose)





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
        if sett.score > int(self.record):
            self.record = sett.score
            self.cur.execute(f"""UPDATE login
                             SET record = '{self.record}'
                            WHERE username = '{self.name}'""")
            self.con.commit()
            self.record_label.setText(f'Record:  {self.record}')

    def mousePressEvent(self, event):
        x = int(str(event.pos()).split('(')[1].split(',')[0])
        beta_y = str(event.pos()).split('(')[1].split(',')[1]
        y = ''
        for el in beta_y:
            if el.isdigit():
                y += el
        y = int(y)
        if 280 <= x <= 351 and 270 <= y <= 341:
            if self.skin_index != len(all_skins) - 1:
                self.skin_index += 1
                self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
                self.photo_label.setPixmap(self.pixmap)
            else:
                self.skin_index = 0
                self.pixmap = QPixmap(f"graphics/{all_skins[self.skin_index]}/2.png")
                self.photo_label.setPixmap(self.pixmap)

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











