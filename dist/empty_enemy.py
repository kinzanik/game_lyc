from bool import sett
class EmptyEnemy:
    def __init__(self):
        self.a = 0
        self.is_attacking = False
        self.name = ''
        self.hp = 20

    def attack01(self):
        pass

    def attack02(self):
        pass

    def end_attack(self):
        self.a = 0
        self.is_attacking = False

    def get_is_attacking(self):
        return self.is_attacking

    def set_is_attacking(self, new):
        self.is_attacking = new

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def set_hp(self, new):
        if new > 0:
            self.hp = new
        else:
            sett.running = False
            sett.game_active = True
            self.hp = 20