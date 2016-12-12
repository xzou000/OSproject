# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buy_page.ui'
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

class Ui_buy_page(object):
    def __init__(self,name,money):
        self.user=name
        self.balance=money


    def setbox(self,title, message):
        box=QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()

    def put_item_to_list(self):
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        counter = 0
        index = 0
        #print(len(result.fetchall()))
        for item in result:
            temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                          '     Description:  '+ item[counter+3]

            item_c = self.listWidget.item(index)
            item_c.setText(temp_str)
            index += 1
        connection.close()

    def changeMoney(self):
        connect = sqlite3.connect('login.db')
        connect.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?",(self.balance,self.user))
        connect.commit()
        connect.close()

    def money_from_buy(self,cost):
        if(cost < self.balance):
            self.balance=self.balance-cost
            self.setbox("Information", "You successfully purchase the item!")
            self.changeMoney()
            self.update_money()

    def update_money(self):
        self.moneyLabel.setText("Balance: " + str(self.balance))

    def getint(self):

        gui = QtGui.QWidget()
        text, ok = QtGui.QInputDialog.getInt(gui, "question",
                                              """Please rate the seller from 1 to 5.""")
        if ok:
            if(text < 1 or text > 5):
                self.getint()
            return text
        else:
            self.setbox("Warning","Please rate the seller from 1 to 5")
            self.getint()

    def buy_item(self):
        target = self.listWidget.currentItem().text()
        target_pter = self.listWidget.currentItem()
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        counter = 0
        index = 0
        for item in result:
            temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                          '     Description:  '+ item[counter+3]
            if temp_str == target:
                connection.execute("DELETE FROM ITEMS WHERE SELLER = ? AND ITEMNAME = ? AND \
                PRICE = ? AND DESCRIPTION = ?", (item[counter], item[counter+1], item[counter+2], item[counter+3],))
                if(self.balance < float(item[counter+2])):
                    self.setbox("Warning", "You don't have enough money in your account")
                    return
                connectLogin = sqlite3.connect('login.db')
                result2 = connectLogin.execute("SELECT * FROM USERS WHERE USERNAME = ?", (item[counter],))
                current_balance = 0
                for user in result2:
                    current_balance = user[2]
                current_balance+=item[counter+2]
                connectLogin.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?",(current_balance,item[counter]))
                connectLogin.commit()
                connectLogin.close()
                self.listWidget.takeItem(self.listWidget.row(target_pter))
                self.money_from_buy(float(item[counter+2]))
                self.getint()
                break
            index += 1
        connection.commit()

        connection.close()


    def searchitem(self):
        item_name = self.search.text()
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS WHERE ITEMNAME = ?", (item_name,))
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
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))


        self.search = QtGui.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(30, 80, 421, 41))
        self.search.setObjectName(_fromUtf8("search"))


        self.search_Button = QtGui.QPushButton(self.centralwidget)
        self.search_Button.setGeometry(QtCore.QRect(570, 80, 121, 41))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.search_Button.clicked.connect(self.searchitem)

        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 190, 511, 381))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        ##create the list in listwidge
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        for items in result:
            item_b = QtGui.QListWidgetItem()
            self.listWidget.addItem(item_b)
        #self.listWidget.clicked.connect(self.)
        #self.listWidget.clicked()

        self.buy_Button = QtGui.QPushButton(self.centralwidget)
        self.buy_Button.setGeometry(QtCore.QRect(580, 240, 121, 51))
        self.buy_Button.setObjectName(_fromUtf8("buy_Button"))
        self.buy_Button.clicked.connect(self.buy_item)

        font1 = QtGui.QFont()
        font1.setPointSize(15)

        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(500, 5, 221, 41))
        self.userLabel.setFont(font1)
        self.userLabel.setText("Username: " + self.user)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.moneyLabel = QtGui.QLabel(self.centralwidget)
        self.moneyLabel.setGeometry(QtCore.QRect(500, 35, 221, 41))
        self.moneyLabel.setFont(font1)
        self.moneyLabel.setText("Balance: " + str(self.balance))
        self.moneyLabel.setAlignment(QtCore.Qt.AlignCenter)


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
        MainWindow.setWindowTitle(_translate("MainWindow", "BUY", None))
        self.label.setText(_translate("MainWindow", "BUY PAGE", None))
        self.search_Button.setText(_translate("MainWindow", "search", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.put_item_to_list()
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.buy_Button.setText(_translate("MainWindow", "BUY", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_buy_page('super',1000000)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())