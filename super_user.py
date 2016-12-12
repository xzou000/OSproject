# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'super_user.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import sqlite3
from user_inf import Ui_user_inf
from PyQt4 import QtCore, QtGui

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

class Ui_super_user(object):

    def put_user_to_list(self):
        connection = sqlite3.connect('superuser.db')
        result = connection.execute("SELECT * FROM USERMESSAGES")
        counter = 0
        index = 0
        #print(len(result.fetchall()))
        for item in result:
            #USERNAME TEXT NOT NULL,PASSWORD NOT NULL, MONEY REAL, ACTIVATE INTEGER, FLAG INTEGER
            temp_str = 'username: ' + item[counter] + '   Message:  ' + item[counter+1]
            item_c = self.message_list.item(index)
            item_c.setText(temp_str)
            index += 1
        connection.close()


    def openuser(self):
        target = self.userSearch.text()
        connection = sqlite3.connect('login.db')
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ?", (target,))
        if len(result.fetchall()) > 0:
            tem1 = ''; tem2 = 0; tem3 = 0
            for item in result:
                tem1 = item[0]; tem2 = item[2]; tem3 = item[4]
            self.user_wind = QtGui.QMainWindow()
            self.ui = Ui_user_inf(tem1,tem2,tem3)
            self.ui.setupUi(self.user_wind)
            self.user_wind.show()
        else:
            print('nothing')
        connection.close()






    def searchitem(self):
        item_name = self.userSearch.text()
        connection = sqlite3.connect('login.db')
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ?", (item_name,))
        if result.fetchone() is None:
            self.setbox('Item not Found!', 'Please try others')# warning page
        elif len(result.fetchone()) > 0:
            self.setbox("Found", "Your items are in the list.")# change to new page which show login already
        connection.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.message_list = QtGui.QListWidget(self.centralwidget)
        self.message_list.setGeometry(QtCore.QRect(120, 180, 551, 361))
        self.message_list.setObjectName(_fromUtf8("message_list"))
        connection = sqlite3.connect('superuser.db')
        result = connection.execute("SELECT * FROM USERMESSAGES")
        for items in result:
            item_b = QtGui.QListWidgetItem()
            self.message_list.addItem(item_b)

        #self.message_list.doubleClicked.connect(self.openuser)



        self.userSearchButton = QtGui.QPushButton(self.centralwidget)
        self.userSearchButton.setGeometry(QtCore.QRect(590, 80, 81, 41))
        self.userSearchButton.setObjectName(_fromUtf8("userSearchButton"))
        self.userSearchButton.clicked.connect(self.openuser)

        self.userSearch = QtGui.QLineEdit(self.centralwidget)
        self.userSearch.setGeometry(QtCore.QRect(350, 80, 221, 41))
        self.userSearch.setObjectName(_fromUtf8("userSearch"))


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
        self.label.setText(_translate("MainWindow", "Wlecome, Admin", None))
        __sortingEnabled = self.message_list.isSortingEnabled()
        self.message_list.setSortingEnabled(False)
        self.put_user_to_list()
        self.message_list.setSortingEnabled(__sortingEnabled)
        self.userSearchButton.setText(_translate("MainWindow", "SEARCH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_super_user()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

