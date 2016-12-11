# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_up.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from user_home import Ui_user_home

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

class Ui_set_up(object):
    def setbox(self,title, message):
        box=QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()

    def create(self):
        connect = sqlite3.connect('login.db')
        name=self.user_id.text()
        password=self.password.text()

        result = connect.execute("SELECT * FROM USERS")
        for data in result:
            user = data[0]
            word = data[1]
            if (user==name):
                self.setbox("Warning","Username already exists\nTry again")
                return
            elif(word==password):
                self.setbox("Warning", "Password already exists\nTry again")
                return
            elif(len(name)==0):
                self.setbox("Warning", "Please enter your username")
                return
            elif (len(password) == 0):
                self.setbox("Warning", "Please enter your password")
                return
        connect.execute("INSERT INTO USERS VALUES(?, ?,?,?,?)", (name, password,0,1,0))
        connect.commit()
        self.setbox("Information", "Create account successfully.\nNow go to your personal page")
        print(name, password)
        self.go_to_personal_page()

        connect.close()

    def go_to_personal_page(self):
        self.createwindow=QtGui.QMainWindow()
        self.personal=Ui_user_home()
        self.personal.setupUi(self.createwindow)
        self.createwindow.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.user_id = QtGui.QLineEdit(self.centralwidget)
        self.user_id.setGeometry(QtCore.QRect(280, 190, 291, 51))
        self.user_id.setObjectName(_fromUtf8("user_id"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(280, 270, 291, 51))
        self.password.setObjectName(_fromUtf8("password"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 480, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.enter = QtGui.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(280, 370, 151, 41))
        self.enter.setObjectName(_fromUtf8("enter"))

        self.enter.clicked.connect(self.create)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Account", None))
        self.label.setText(_translate("MainWindow", "Create your Account", None))
        self.label_2.setText(_translate("MainWindow", "User ID : ", None))
        self.label_3.setText(_translate("MainWindow", "Password : ", None))
        self.enter.setText(_translate("MainWindow", "Create", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_set_up()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

