# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from buy_page import Ui_buy_page
from rent_page import Ui_rent_page
from person import Ui_person
import sqlite3
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_user_home(object):
    def __init__(self,username,money,rating,suspend,rflag,isvip):
        self.name=username
        self.balance=money
        self.rate=rating
        self.suspended=suspend
        self.flag=rflag
        self.vip=isvip

    def personpage(self):
        self.create_wind = QtGui.QMainWindow()
        self.update_balance()
        self.ui = Ui_person(self.name,self.balance, self.rate, self.suspended, self.flag, self.vip)
        self.ui.setupUi(self.create_wind)
        self.create_wind.show()

    def update_balance(self):
        connection = sqlite3.connect('login.db')
        result = connection.execute("SELECT * FROM USERS")
        for data in result:
            if(data[0]==self.name):
                self.balance=data[2]


    def buypage(self):
        self.create_wind = QtGui.QMainWindow()
        self.update_balance()
        self.ui = Ui_buy_page(self.name, self.balance)
        self.ui.setupUi(self.create_wind)
        self.create_wind.show()

    def rentpage(self):
        self.create_wind = QtGui.QMainWindow()
        self.update_balance()
        self.ui = Ui_rent_page(self.name, self.balance)
        self.ui.setupUi(self.create_wind)
        self.create_wind.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(12, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 311, 101))
        self.label_2.setBaseSize(QtCore.QSize(123, 123))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.buy = QtGui.QPushButton(self.centralwidget)
        self.buy.setGeometry(QtCore.QRect(90, 230, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buy.setFont(font)
        self.buy.setObjectName(_fromUtf8("buy"))
        ###buy botton connect
        self.buy.clicked.connect(self.buypage)


        self.rent = QtGui.QPushButton(self.centralwidget)
        self.rent.setGeometry(QtCore.QRect(440, 230, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rent.setFont(font)
        self.rent.setObjectName(_fromUtf8("rent"))
        ###rent button connection
        self.rent.clicked.connect(self.rentpage)

        self.welcome_label = QtGui.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(420, 40, 211, 61))
        self.welcome_label.setBaseSize(QtCore.QSize(123, 123))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName(_fromUtf8("label1"))
        self.welcome_label.setText("Welcome, ")

        self.user_label = QtGui.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(550, 40, 211, 61))
        self.user_label.setBaseSize(QtCore.QSize(123, 123))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_label.setFont(font)
        self.user_label.setObjectName(_fromUtf8("label3"))
        connection = sqlite3.connect('login.db')
       # "result = connection.execute("SELECT * FROM ITEMS WHERE USERNAME = ?",)"


        self.user_label.setText(self.name)

        self.information = QtGui.QPushButton(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(450, 110, 211, 31))
        self.information.setObjectName(_fromUtf8("information"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.information.clicked.connect(self.personpage)


        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "User Homepage", None))
        self.label_2.setText(_translate("MainWindow", "Market", None))
        self.buy.setText(_translate("MainWindow", "BUY", None))
        self.rent.setText(_translate("MainWindow", "RENT", None))
        self.information.setText(_translate("MainWindow", "User Information", None))


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_user_home('super',1000000,3,1,1,1)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())