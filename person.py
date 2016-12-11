# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'person.ui'
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

class Ui_person(object):
    def __init__(self,name,money):
        self.user=name
        self.balance=money



    def setupUi(self, person):
        person.setObjectName(_fromUtf8("person"))
        person.resize(800, 600)
        self.centralwidget = QtGui.QWidget(person)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 151, 41))

        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.buyItem = QtGui.QTextEdit(self.centralwidget)
        self.buyItem.setGeometry(QtCore.QRect(136, 198, 201, 41))
        self.buyItem.setObjectName(_fromUtf8("buyItem"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 198, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.buyPrice = QtGui.QTextEdit(self.centralwidget)
        self.buyPrice.setGeometry(QtCore.QRect(136, 258, 201, 41))
        self.buyPrice.setObjectName(_fromUtf8("buyPrice"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(16, 258, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.rentItem_2 = QtGui.QTextEdit(self.centralwidget)
        self.rentItem_2.setGeometry(QtCore.QRect(140, 420, 201, 41))
        self.rentItem_2.setObjectName(_fromUtf8("rentItem_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.rentItem = QtGui.QTextEdit(self.centralwidget)
        self.rentItem.setGeometry(QtCore.QRect(140, 360, 201, 41))
        self.rentItem.setObjectName(_fromUtf8("rentItem"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Add = QtGui.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(390, 230, 121, 41))
        self.Add.setObjectName(_fromUtf8("Add"))
        self.rentAdd = QtGui.QPushButton(self.centralwidget)
        self.rentAdd.setGeometry(QtCore.QRect(390, 420, 121, 41))
        self.rentAdd.setObjectName(_fromUtf8("rentAdd"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.rechargeButton = QtGui.QPushButton(self.centralwidget)
        self.rechargeButton.setGeometry(QtCore.QRect(640, 130, 121, 41))
        self.rechargeButton.setObjectName(_fromUtf8("rechargeButton"))

        self.recharge = QtGui.QLineEdit(self.centralwidget)
        self.recharge.setGeometry(QtCore.QRect(430, 130, 191, 41))
        self.recharge.setObjectName(_fromUtf8("recharge"))



        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(430, 30, 191, 61))
        self.text.setObjectName(_fromUtf8("text"))
        self.sentButton = QtGui.QPushButton(self.centralwidget)
        self.sentButton.setGeometry(QtCore.QRect(640, 40, 121, 41))
        self.sentButton.setObjectName(_fromUtf8("sentButton"))
        self.message = QtGui.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(550, 270, 211, 121))
        self.message.setObjectName(_fromUtf8("message"))


        self.username = QtGui.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(170, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setText(_fromUtf8(""))
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName(_fromUtf8("username"))

        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(100, 40, 221, 41))
        self.userLabel.setFont(font)
        self.userLabel.setText(self.user)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.moneyLabel = QtGui.QLabel(self.centralwidget)
        self.moneyLabel.setGeometry(QtCore.QRect(100, 100, 221, 41))
        self.moneyLabel.setFont(font)
        self.moneyLabel.setText(str(self.balance))
        self.moneyLabel.setAlignment(QtCore.Qt.AlignCenter)


        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 10, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        person.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(person)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        person.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(person)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        person.setStatusBar(self.statusbar)

        self.retranslateUi(person)
        QtCore.QMetaObject.connectSlotsByName(person)

    def retranslateUi(self, person):
        person.setWindowTitle(_translate("person", "Personal Page", None))
        self.label.setText(_translate("person", "Username : ", self.user))
        self.label_3.setText(_translate("person", "Item : ", None))
        self.label_4.setText(_translate("person", "Price : ", None))
        self.label_5.setText(_translate("person", "Price : ", None))
        self.label_6.setText(_translate("person", "Item : ", None))
        self.Add.setText(_translate("person", "Add", None))
        self.rentAdd.setText(_translate("person", "Add", None))
        self.label_8.setText(_translate("person", "Balance : ", None))
        self.rechargeButton.setText(_translate("person", "Recharge", None))
        self.sentButton.setText(_translate("person", "SENT", None))
        self.label_2.setText(_translate("person", "Sent message to Superuser:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    person = QtGui.QMainWindow()
    ui = Ui_person()
    ui.setupUi(person)
    person.show()
    sys.exit(app.exec_())

