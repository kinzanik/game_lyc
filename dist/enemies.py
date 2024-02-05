import random as r
from settings import *
from attacks import Attack1, Attack2, Attack3, Attack4
from empty_enemy import EmptyEnemy

class Enemy1(EmptyEnemy):
    def __init__(self):
        super().__init__()
        self.name = 'Nerdlin'

    def attack01(self):
        if self.a == 0:
            for i in range(4, 6):
                Attack4(attack1, box_x + 2, box_y + 1, i, 0)
            Attack4(attack1, box_x + 2, box_y + 1, 4, 1)
        if self.a == 5:
            for i in range(3):
                Attack4(attack1, box_x + 2, box_y + 1, i, 0)
            Attack4(attack1, box_x + 2, box_y + 1, 0, 1)
        if self.a == 10:
            Attack4(attack1, box_x + 2, box_y + 1, 3, 0)
            for i in range(1, 4):
                Attack4(attack1, box_x + 2, box_y + 1, i, 1)
        if self.a == 15:
            for i in range(4):
                Attack4(attack1, box_x + 2, box_y + 1, i, 2)
        if self.a == 20:
            for i in range(6, 8):
                Attack4(attack1, box_x + 2, box_y + 1, i, 0)
            for i in range(5, 7):
                Attack4(attack1, box_x + 2, box_y + 1, i, 1)
        if self.a == 25:
            for i in range(8, 10):
                Attack4(attack1, box_x + 2, box_y + 1, i, 0)
            for i in range(7, 9):
                Attack4(attack1, box_x + 2, box_y + 1, i, 1)
        if self.a == 30:
            Attack4(attack1, box_x + 2, box_y + 1, 9, 1)
            for i in range(7, 10):
                Attack4(attack1, box_x + 2, box_y + 1, i, 2)
        if self.a == 35:
            for i in range(4, 7):
                Attack4(attack1, box_x + 2, box_y + 1, i, 2)
        if self.a >= 43 and self.a % 2 == 0:
            for i in attack1:
                if i.get_name() == 'block':
                    i.blink()
        if self.a >= 54:
            self.end_attack()
        self.a += 1

    def attack02(self):
        move_list = ['up', 'down', 'left', 'right']
        if self.a <= 16:
            Attack1(attack1, r.choice(move_list))
            self.a += 1
        if len(attack1) == 0:
            self.end_attack()


class Enemy2(EmptyEnemy):
    def __init__(self):
        super().__init__()
        self.name = 'Ghost'

    def attack01(self):
        if self.a <= 16 and self.a % 2 == 0:
            Attack2(attack1)
        self.a += 1
        if len(attack1) == 0:
            self.end_attack()

    def attack02(self):
        if self.a <= 16 and self.a % 2 == 0:
            pos = r.randint(110, 250)
            Attack3(attack1, pos, 'left')
            Attack3(attack1, pos + 230, 'left')
        self.a += 1
        if len(attack1) == 0:
            self.end_attack()