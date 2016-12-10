# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_inf.ui'
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
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(400, 30, 141, 41))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(30, 240, 191, 101))
        self.text.setObjectName(_fromUtf8("text"))
        self.sentButton = QtGui.QPushButton(self.centralwidget)
        self.sentButton.setGeometry(QtCore.QRect(240, 270, 121, 41))
        self.sentButton.setObjectName(_fromUtf8("sentButton"))
        self.vipButton = QtGui.QPushButton(self.centralwidget)
        self.vipButton.setGeometry(QtCore.QRect(400, 90, 141, 41))
        self.vipButton.setObjectName(_fromUtf8("vipButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Balance = QtGui.QTextEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(180, 150, 201, 41))
        self.Balance.setObjectName(_fromUtf8("Balance"))
        self.user = QtGui.QTextEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(180, 30, 201, 41))
        self.user.setObjectName(_fromUtf8("user"))
        self.id = QtGui.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(180, 90, 201, 41))
        self.id.setObjectName(_fromUtf8("id"))
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
        self.label_3.setText(_translate("MainWindow", "User : ", None))
        self.label_4.setText(_translate("MainWindow", "ID : ", None))
        self.label_8.setText(_translate("MainWindow", "Balance : ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

