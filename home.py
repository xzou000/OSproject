# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from user_home import Ui_user_home
from set_up import Ui_set_up
from visit_browse import Ui_Buypage
from visit_rent import Ui_rent

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

class Ui_home(object):
    def setbox(self, title, message):
        box = QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()


    def login_check(self):
        username=self.ID.text()
        password=self.Password.text()
        connection=sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ? AND MONEY=0 AND ACTIVATE=1 AND FLAG=0", (username, password))
        if(len(result.fetchall()) > 0):
            self.setbox('Information','User found! Go to personal page')
            self.userwindow = QtGui.QMainWindow()
            self.userpage = Ui_user_home()
            self.userpage.setupUi(self.userwindow)
            self.userwindow.show()
        else:
            self.setbox('Warning','User not found, please try again')
        connection.close()
    def go_to_account(self):
        self.createwindow=QtGui.QMainWindow()
        self.create=Ui_set_up()
        self.create.setupUi(self.createwindow)
        self.createwindow.show()

    def visit_buy(self):
        self.create_vbuy = QtGui.QMainWindow()
        self.create=Ui_Buypage()
        self.create.setupUi(self.create_vbuy)
        self.create_vbuy.show()
    def visit_rent(self):
        self.create_vrent = QtGui.QMainWindow()
        self.create=Ui_rent()
        self.create.setupUi(self.create_vrent)
        self.create_vrent.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(12, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ID = QtGui.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(520, 40, 121, 31))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.Password = QtGui.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(660, 40, 121, 31))
        self.Password.setObjectName(_fromUtf8("Password"))
        self.ID_2 = QtGui.QLabel(self.centralwidget)
        self.ID_2.setGeometry(QtCore.QRect(520, 20, 46, 13))
        self.ID_2.setObjectName(_fromUtf8("ID_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 311, 101))
        self.label_2.setBaseSize(QtCore.QSize(123, 123))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(520, 80, 75, 31))
        self.login.setObjectName(_fromUtf8("login"))

        self.login.clicked.connect(self.login_check)

        self.setup = QtGui.QPushButton(self.centralwidget)
        self.setup.setGeometry(QtCore.QRect(660, 80, 75, 31))
        self.setup.setObjectName(_fromUtf8("setup"))
        self.setup.clicked.connect(self.go_to_account)
        self.buy = QtGui.QPushButton(self.centralwidget)
        self.buy.setGeometry(QtCore.QRect(90, 230, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buy.setFont(font)
        self.buy.setObjectName(_fromUtf8("buy"))
        self.buy.clicked.connect(self.visit_buy)

        self.rent = QtGui.QPushButton(self.centralwidget)
        self.rent.setGeometry(QtCore.QRect(440, 230, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rent.setFont(font)
        self.rent.setObjectName(_fromUtf8("rent"))
        self.rent.clicked.connect(self.visit_rent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Homepage", None))
        self.ID_2.setText(_translate("MainWindow", "ID", None))
        self.label.setText(_translate("MainWindow", "Password", None))
        self.label_2.setText(_translate("MainWindow", "Market", None))
        self.login.setText(_translate("MainWindow", "Log in", None))
        self.setup.setText(_translate("MainWindow", "set up", None))
        self.buy.setText(_translate("MainWindow", "BUY", None))
        self.rent.setText(_translate("MainWindow", "RENT", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
