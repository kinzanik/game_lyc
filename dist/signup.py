from PyQt5.QtCore import Qt, QPoint
from math import cos, sin, pi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from bool import sett
import sys
import sqlite3
from PyQt5 import uic

class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('des1.ui', self)
        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()

        self.next_Button.clicked.connect(self.next)

    def next(self):
        self.users = []
        self.username = self.cur.execute(f"""SELECT username FROM login
                                                     """).fetchall()

        for el in self.username:
            self.users.append(el[0])

        if self.user_lineEdit.text() == '' or self.passw_lineEdit.text() == '':

            self.res_label.setText('Вы ничего не ввели')
        elif self.user_lineEdit.text() in self.users:
            self.res_label.setText('Пользователь с таким именем уже существует')
        else:
            self.cur.execute(f'''INSERT INTO login VALUES('{self.user_lineEdit.text()}',
'{self.passw_lineEdit.text()}', 0, 0, 0, 0, 1)''')
            self.con.commit()
            self.res_label.setText('Вы зарегистрировалась, можете закрыть <br>это окно и войти в свой аккаунт</br>')

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Информация',
            'Вы уверены, что хотите закрыть окно?',
            QMessageBox.Yes,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()





