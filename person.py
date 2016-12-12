__author__ = 'hanguup'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'person.ui'
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

class Ui_person(object):
    def __init__(self,name,money,rating,suspend,rflag,isvip):
        self.user=name
        self.balance=money
        self.rate=rating
        self.suspended=suspend
        self.flag=rflag
        self.vip=isvip

    def setbox(self, title, message):
        box = QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()

#############   Deposit ###########
    def chargeMoney(self,amount):
        amount=self.recharge.text()
        self.balance=self.balance+float(amount)
        self.changeMoney()
        self.setbox("Information", "You balance now is " + str(self.balance))
        self.update_money()
        print(self.balance)

    def getAmount(self):
        self.chargeMoney()


    def changeMoney(self):
        connect = sqlite3.connect('login.db')
        connect.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?",(self.balance,self.user))
        connect.commit()
        connect.close()
######################################################################################################

###########     Withdraw #########
    def getMoney(self,amount):
        amount=self.withdraw.text()
        money=float(amount)
        if(money > self.balance):
            self.setbox("Warning","You don't have enough money in your account")
        else:
            self.balance=self.balance-money
            self.changeMoney()
            self.setbox("Information","You balance now is " + str(self.balance))
            self.update_money()
            print(self.balance)

    def getAmount(self):
        self.getMoney()
####################################

    def update_money(self):
        self.moneyLabel.setText(str(self.balance))

####################################
    def sellitem(self):
        sellername = self.user
        itemname = self.lineEdit.text()
        itemprice = self.lineEdit_2.text()
        itemdescription = self.lineEdit_3.text()
        connection = sqlite3.connect('itemslist.db')
        connection.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", (sellername, itemname, itemprice, itemdescription))
        connection.commit()
        self.setbox('Completed', 'Your item is already placed into shopping list!')


    def rentitem(self):
        sellername = self.user
        itemname = self.lineEdit_4.text()
        itemprice = self.lineEdit_5.text()
        itemdescription = self.lineEdit_6.text()
        connection = sqlite3.connect('rentlist.db')
        connection.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", (sellername, itemname, itemprice, itemdescription))
        connection.commit()
        self.setbox('Completed', 'Your item is already placed into renting list!')


    def sentmessage(self):
        target = self.text.toPlainText()
        connection = sqlite3.connect('superuser.db')
        if target is not None:
            connection.execute("INSERT INTO USERMESSAGES VALUES(?, ?)",(self.user,target))
        connection.commit()
        connection.close()

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
        self.label_2.setGeometry(QtCore.QRect(60, 40, 151, 61))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_4 = QtGui.QLabel(person)
        self.label_4.setGeometry(QtCore.QRect(90, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))




        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_3 = QtGui.QLabel(person)
        self.label_3.setGeometry(QtCore.QRect(90, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Add = QtGui.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(390, 230, 121, 41))
        self.Add.setObjectName(_fromUtf8("Add"))
        self.Add.clicked.connect(self.sellitem)

        self.rentAdd = QtGui.QPushButton(self.centralwidget)
        self.rentAdd.setGeometry(QtCore.QRect(390, 420, 121, 41))
        self.rentAdd.setObjectName(_fromUtf8("rentAdd"))
        self.rentAdd.clicked.connect(self.rentitem)


        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        # Deposit
        self.rechargeButton = QtGui.QPushButton(self.centralwidget)
        self.rechargeButton.setGeometry(QtCore.QRect(640, 100, 121, 41))
        self.rechargeButton.setObjectName(_fromUtf8("rechargeButton"))

        self.recharge = QtGui.QLineEdit(self.centralwidget)
        self.recharge.setGeometry(QtCore.QRect(430, 100, 191, 41))
        self.recharge.setObjectName(_fromUtf8("recharge"))
        self.rechargeButton.clicked.connect(self.chargeMoney)

        # Withdraw
        self.withdrawButton = QtGui.QPushButton(self.centralwidget)
        self.withdrawButton.setGeometry(QtCore.QRect(640, 150, 121, 41))
        self.withdrawButton.setObjectName(_fromUtf8("withdrawButton"))

        self.withdraw = QtGui.QLineEdit(self.centralwidget)
        self.withdraw.setGeometry(QtCore.QRect(430, 150, 191, 41))
        self.withdraw.setObjectName(_fromUtf8("withdraw"))
        self.withdrawButton.clicked.connect(self.getMoney)


        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(430, 30, 191, 61))
        self.text.setObjectName(_fromUtf8("text"))

        self.sentButton = QtGui.QPushButton(self.centralwidget)
        self.sentButton.setGeometry(QtCore.QRect(640, 40, 121, 41))
        self.sentButton.setObjectName(_fromUtf8("sentButton"))
        self.sentButton.clicked.connect(self.sentmessage)


        self.message = QtGui.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(550, 270, 211, 121))
        self.message.setObjectName(_fromUtf8("message"))
        connection = sqlite3.connect(self.user+'.db')
        result = connection.execute("SELECT * FROM MESSAGES")
        for item in result:
            self.message.setText(item[0])
        connection.close()

        self.lineEdit = QtGui.QLineEdit(person)
        self.lineEdit.setGeometry(QtCore.QRect(180, 190, 181, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(person)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 240, 181, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(person)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 290, 181, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_7 = QtGui.QLabel(person)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_4 = QtGui.QLineEdit(person)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 400, 181, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(person)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 450, 181, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_5 = QtGui.QLabel(person)
        self.label_5.setGeometry(QtCore.QRect(80, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(person)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_6 = QtGui.QLineEdit(person)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 500, 181, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_9 = QtGui.QLabel(person)
        self.label_9.setGeometry(QtCore.QRect(10, 490, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(person)
        self.label_10.setGeometry(QtCore.QRect(20, 140, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_12 = QtGui.QLabel(person)
        self.label_12.setGeometry(QtCore.QRect(10, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.username = QtGui.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(170, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setText(_fromUtf8(""))
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName(_fromUtf8("username"))

        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(120, 40, 270, 41))
        self.userLabel.setFont(font)
        self.userLabel.setText(self.user)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.moneyLabel = QtGui.QLabel(self.centralwidget)
        self.moneyLabel.setGeometry(QtCore.QRect(120, 100, 221, 41))
        self.moneyLabel.setFont(font)
        self.moneyLabel.setText(str(self.balance))
        self.moneyLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.ratingLabel = QtGui.QLabel(self.centralwidget)
        self.ratingLabel.setGeometry(QtCore.QRect(120, 5, 221, 41))
        self.ratingLabel.setFont(font)
        self.ratingLabel.setText("Rating: "+str(self.rate))
        self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)

        if(self.vip==1):
            self.ratingLabel = QtGui.QLabel(self.centralwidget)
            self.ratingLabel.setGeometry(QtCore.QRect(0, 5, 221, 41))
            self.ratingLabel.setFont(font)
            self.ratingLabel.setText("VIP")
            self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)

        if(self.suspended==1):
            self.ratingLabel = QtGui.QLabel(self.centralwidget)
            self.ratingLabel.setGeometry(QtCore.QRect(550, 420, 221, 41))
            self.ratingLabel.setFont(font)
            self.ratingLabel.setText("Suspended")
            self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)

        if(self.flag==1):
            self.ratingLabel = QtGui.QLabel(self.centralwidget)
            self.ratingLabel.setGeometry(QtCore.QRect(550, 500, 221, 41))
            self.ratingLabel.setFont(font)
            self.ratingLabel.setText("Red-Flaged")
            self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)


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
        self.label_7.setText(_translate("person", "Description:", None))
        self.label_5.setText(_translate("person", "Price : ", None))
        self.label_6.setText(_translate("person", "Item : ", None))
        self.label_9.setText(_translate("person", "Description:", None))
        self.label_10.setText(_translate("person", "SELL/BID", None))
        self.label_12.setText(_translate("person", "RENT", None))
        self.label_4.setText(_translate("person", "Price : ", None))


        self.Add.setText(_translate("person", "Add", None))
        self.rentAdd.setText(_translate("person", "Add", None))
        self.label_8.setText(_translate("person", "Balance : ", None))
        self.rechargeButton.setText(_translate("person", "Deposit", None))
        self.withdrawButton.setText(_translate("person", "Withdraw", None))
        self.sentButton.setText(_translate("person", "SENT", None))
        self.label_2.setText(_translate("person", "Sent message to Superuser:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    person = QtGui.QMainWindow()
    ui = Ui_person('aaa','100009898000',5,0,0,0)
    ui.setupUi(person)
    person.show()
    sys.exit(app.exec_())
