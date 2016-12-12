# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_inf.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_user_inf(object):

    def __init__(self,username, balance, flag):
        self.name=username
        self.bala = balance
        self.flag = flag

    def senttouser(self):
        message = self.text.toPlainText()
        connection = sqlite3.connect(self.name+'.db')
        connection.execute("INSERT INTO MESSAGES VALUES(?)", (message,))
        connection.commit()
        connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(400, 30, 141, 41))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))

        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(30, 240, 191, 101))
        self.text.setObjectName(_fromUtf8("text"))


        self.sentButton = QtGui.QPushButton(self.centralwidget)
        self.sentButton.setGeometry(QtCore.QRect(240, 270, 121, 41))
        self.sentButton.setObjectName(_fromUtf8("sentButton"))
        self.sentButton.clicked.connect(self.senttouser)


        self.vipButton = QtGui.QPushButton(self.centralwidget)
        self.vipButton.setGeometry(QtCore.QRect(400, 90, 141, 41))
        self.vipButton.setObjectName(_fromUtf8("vipButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.money = QtGui.QLabel(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(180, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.money.setFont(font)
        self.money.setObjectName(_fromUtf8("label_3"))
        self.money.setText(str(self.bala))

        self.username = QtGui.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(200, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName(_fromUtf8("label_3"))
        self.username.setText(self.name)

        self.fl = QtGui.QLabel(self.centralwidget)
        self.fl.setGeometry(QtCore.QRect(180, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fl.setFont(font)
        self.fl.setObjectName(_fromUtf8("label_3"))
        self.fl.setText(str(self.flag))

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.deleteButton.setText(_translate("MainWindow", "Delete", None))
        self.sentButton.setText(_translate("MainWindow", "SENT", None))
        self.vipButton.setText(_translate("MainWindow", "VIP", None))
        self.label_3.setText(_translate("MainWindow", "Username : ", None))
        self.label_4.setText(_translate("MainWindow", "Flag : ", None))
        self.label_8.setText(_translate("MainWindow", "Balance : ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_user_inf('aaa',10000,0)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

