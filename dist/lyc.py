import random
import sys
import pygame
import random as r
from player_und import Player_Und
from settings_und import *
from attack_bar import AttackBar
from attack_line import AttackLine
from attacks import Attack1, Attack2, Attack3, Attack4
from draw_enemy import DrawEnemy
from empty_enemy import EmptyEnemy
from enemies import Enemy1, Enemy2
from bool import *
from settings import *





heart = Player_Und(player_und)
a = 1
pike = pygame.USEREVENT
pygame.time.set_timer(pike, 200)
enemy = EmptyEnemy()
choice_attack = 0
attack_bar = AttackBar(attack_bar_group)
line = AttackLine(line_group)

enemy_text = small_font.render('', True, 'white')
big_text = big_font.render('', True, 'white')
damage_text = small_font.render('', True, 'white')
enemy_hp = small_font.render('', True, 'white')
player_und_hp = small_font.render('', True, 'white')

first_attack = False
player_und_attacking = False
draw_big_text = True
draw_attack_bar = False
enemy_attack_time = True
before_len_attack = 0


