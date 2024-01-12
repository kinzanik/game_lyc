from PyQt5.QtCore import Qt, QPoint
from math import cos, sin, pi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QColor
from bool import sett
import sys
import sqlite3
from PyQt5 import uic
from signup import SignUp



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('des.ui', self)
        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.name = ''

        self.check_Button.clicked.connect(self.check)
        self.sign_Button.clicked.connect(self.sign)

    def check(self):
        self.dict = {}
        self.users = []
        self.passw = []
        self.username = self.cur.execute(f"""SELECT username FROM login
                                             """).fetchall()
        self.password = self.cur.execute(f"""SELECT password FROM login
                                                     """).fetchall()
        for el in self.username:
            self.users.append(el[0])
        for el in self.password:
            self.passw.append(el[0])

        for i in range (len(self.users)):
            self.dict[self.users[i]] = self.passw[i]

        print(self.dict)

        print(self.user_lineEdit.text())
        print(self.passw)
        if self.user_lineEdit.text() in self.users:
            if self.passw_lineEdit.text() == str(self.dict[self.user_lineEdit.text()]):
                self.res_Label.setText(f'Вы вошли в свой аккаунт, <br>можете закрыть окно</br>')
                self.name = self.user_lineEdit.text()
                print('вы вошли в свой аккаунт')
            else:
                self.res_Label.setText('Неверный пароль')
                print('неверный пароль')
        else:
            self.res_Label.setText('Вы не зарегестрированы')
            print('Вы не зарегестрированы')
        #    pass
        print(self.users)

    def closeEvent(self, event):
        if self.name != '':
            reply = QMessageBox.question(
                self,
                'Информация',
                'Вы уверены, что хотите закрыть окно?',
                QMessageBox.Yes,
                QMessageBox.No)
        else:
            reply = QMessageBox.question(
                self,
                'Информация',
                'Вы не можете продолжить работу, пока не войдете в свой аккаунт',
                QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            sett.info = True

        else:
            event.ignore()



    def sign(self):
        self.signup_form = SignUp()
        self.signup_form.show()
        self.con.commit()



