from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from bool import sett

class WouldYou(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('des3.ui', self)
        self.yes_Button.clicked.connect(self.yes)
        self.no_Button.clicked.connect(self.no)

    def yes(self):
        sett.running = True
        sett.perehod = False
        self.hide()



    def no(self):
        sett.form1.show()
        sett.perehod = False
        self.hide()


