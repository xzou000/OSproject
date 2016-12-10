# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'super_user.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
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
        self.message_list.setGeometry(QtCore.QRect(20, 80, 291, 261))
        self.message_list.setObjectName(_fromUtf8("message_list"))
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        item = QtGui.QListWidgetItem()
        self.message_list.addItem(item)
        self.userSearchButton = QtGui.QPushButton(self.centralwidget)
        self.userSearchButton.setGeometry(QtCore.QRect(590, 80, 81, 41))
        self.userSearchButton.setObjectName(_fromUtf8("userSearchButton"))
        self.userSearch = QtGui.QTextEdit(self.centralwidget)
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
        item = self.message_list.item(0)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(1)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(2)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(3)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(4)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(5)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(6)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.message_list.item(7)
        item.setText(_translate("MainWindow", "新建项目", None))
        self.message_list.setSortingEnabled(__sortingEnabled)
        self.userSearchButton.setText(_translate("MainWindow", "SEARCH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

