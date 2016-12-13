# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rent_page.ui'
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

class Ui_rent_page(object):
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

    def changeMoney(self):
        connect = sqlite3.connect('login.db')
        connect.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?", (self.balance, self.user))
        connect.commit()
        connect.close()

    def money_from_rent(self, cost):
        connection = sqlite3.connect('login.db')
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ?", (self.user,))
        for i in result:
            price = (cost*0.9)
            if(i[9] >= 5 and self.balance >= price):
                self.balance -= price
                self.setbox("Information", "You successfully purchase the item with 10% discount!")
                self.changeMoney()
                self.update_money()
            elif (cost < self.balance):
                self.balance=self.balance-cost
                self.setbox("Information", "You successfully purchase the item!")
                self.changeMoney()
                self.update_money()

    def update_money(self):
        self.moneyLabel.setText("Balance: " + str(self.balance))

    def put_item_to_list(self):
        connection = sqlite3.connect('rentlist.db')
        result = connection.execute("SELECT * FROM RENTITEMS")
        counter = 0
        index = 0
        for item in result:
            temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                          '     Description:  '+ item[counter+3]
            print(temp_str)
            item_c = self.listWidget.item(index)
            item_c.setText(temp_str)
            index += 1
        connection.close()

    def searchitem(self):
        item_name = self.search.text()
        connection = sqlite3.connect('rentlist.db')
        result = connection.execute("SELECT * FROM RENTITEMS WHERE ITEMNAME = ?", (item_name,))
        #length = len(result.fetchone())
        if result.fetchone() is None:
            self.setbox('Item not Found!', 'Please try others')# warning page
        else:
            self.setbox("Found", "Your items are in the list.")# change to new page which show login already
        connection.close()

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


    def getcomplaint(self):
        gui = QtGui.QWidget()
        text, ok = QtGui.QInputDialog.getText(gui, "question",
                                              """Put 'complain' below to complain this seller""")
        if text == 'complain':#if yes complaint of seller +1
            target = self.listWidget.currentItem().text()
            connection = sqlite3.connect('rentlist.db')
            result = connection.execute("SELECT * FROM RENTITEMS")
            counter = 0
            index = 0
            for item in result:
                temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                              '     Description:  '+ item[counter+3]
                if temp_str == target:
                    connect_to_seller = sqlite3.connect('login.db')
                    this_seller = connect_to_seller.execute("SELECT * FROM USERS WHERE USERNAME = ?", (item[counter],))
                    complaint = 0
                    for seller in this_seller:
                        complaint = seller[7]
                    complaint+=1
                    connect_to_seller.execute("UPDATE USERS SET COMPLAINT = ? WHERE USERNAME = ?" ,(complaint, item[counter]))
                    connect_to_seller.commit()

                    if complaint >= 3:
                        connect_to_seller.execute("DELETE FROM USERS WHERE USERNAME = ?",(item[counter]))
                        connect_to_seller.commit()
                    connect_to_seller.close()

    def rent_item(self):
        target = self.listWidget.currentItem().text()
        target_pter = self.listWidget.currentItem()
        connection = sqlite3.connect('rentlist.db')
        result = connection.execute("SELECT * FROM RENTITEMS")
        counter = 0
        index = 0
        for item in result:
            temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                          '     Description:  '+ item[counter+3]
            if temp_str == target:
                connection.execute("DELETE FROM RENTITEMS WHERE SELLER = ? AND ITEMNAME = ? AND \
                PRICE = ? AND DESCRIPTION = ?", (item[counter], item[counter+1], item[counter+2], item[counter+3]))
                connection.commit()
                connection.close()
                if(self.balance < float(item[counter+2])):
                    self.setbox("Warning", "You don't have enough money in your account")
                    return
                connectLogin = sqlite3.connect('login.db')
                getrate = self.getint()
                print(getrate)
                if getrate <= 2 or getrate >= 4:
                    result3 = connectLogin.execute("SELECT * FROM USERS WHERE USERNAME = ?", (self.user,))
                    cur_act = 0
                    for items in result3:
                        cur_act = items[3]
                    cur_act += 1
                    connectLogin.execute("UPDATE USERS SET ACTIVATE = ? WHERE USERNAME =?", (cur_act, self.user))
                    connectLogin.commit()
                    print(cur_act)
                    if cur_act >= 3:
                        connectLogin.execute("UPDATE USERS SET SUSPENDED = ? WHERE USERNAME =?", (1, self.user))
                        connectLogin.commit()
                result4 = connectLogin.execute("SELECT * FROM USERS WHERE USERNAME = ?", (self.user,))
                vip = 0
                for i in result4:
                    vip = i[9]
                vip += 1
                connectLogin.execute("UPDATE USERS SET VIP = ? WHERE USERNAME =?", (vip, self.user))
                connectLogin.commit()
                connectLogin.close()
                current_balance = 0
                current_rate = 0
                cur_num_rate = 0
                print(cur_num_rate,
                      current_rate)
                connectLogin1 = sqlite3.connect('login.db')
                result2 = connectLogin1.execute("SELECT * FROM USERS WHERE USERNAME = ?", (item[counter],))
                for user in result2:
                    current_balance = user[2]
                    current_rate = user[5]
                    cur_num_rate = user[6]
                print(current_balance)
                cur_num_rate += 1
                current_rate = (current_rate+getrate)/cur_num_rate
                current_balance= current_balance + item[counter+2]
                print(current_balance, item[counter+2])
                if cur_num_rate>=3 and current_rate <= 2:
                    connectLogin1.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?",(current_balance, item[counter]))
                    connectLogin1.execute("UPDATE USERS SET RATE = ? WHERE USERNAME = ?",(current_rate, item[counter]))
                    connectLogin1.execute("UPDATE USERS SET NUMRATE = ? WHERE USERNAME = ?",(cur_num_rate, item[counter]))
                    connectLogin1.execute("UPDATE USERS SET SUSPENDED = ? WHERE USERNAME = ?",(1, item[counter]))
                    print('hahah',current_rate)
                    connectLogin1.commit()
                else:
                    connectLogin1.execute("UPDATE USERS SET MONEY = ? WHERE USERNAME = ?",(current_balance, item[counter]))
                    connectLogin1.execute("UPDATE USERS SET RATE = ? WHERE USERNAME = ?",(current_rate, item[counter]))
                    connectLogin1.execute("UPDATE USERS SET NUMRATE = ? WHERE USERNAME = ?",(cur_num_rate, item[counter]))
                    print('heheh',current_rate, current_balance, item[counter])
                    connectLogin1.commit()
                self.listWidget.takeItem(self.listWidget.row(target_pter))
                self.getcomplaint()
                self.money_from_rent(float(item[counter+2]))
                connectLogin1.close()
                break
            index += 1


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.search = QtGui.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(20, 80, 421, 41))
        self.search.setObjectName(_fromUtf8("search"))
        self.search_Button = QtGui.QPushButton(self.centralwidget)
        self.search_Button.setGeometry(QtCore.QRect(560, 80, 121, 41))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.search_Button.clicked.connect(self.searchitem)


        self.rent_Button = QtGui.QPushButton(self.centralwidget)
        self.rent_Button.setGeometry(QtCore.QRect(570, 240, 121, 51))
        self.rent_Button.setObjectName(_fromUtf8("rent_Button"))
        self.rent_Button.clicked.connect(self.rent_item)


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


        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 190, 411, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        connection = sqlite3.connect('rentlist.db')
        result = connection.execute("SELECT * FROM RENTITEMS")
        for items in result:
            item_b = QtGui.QListWidgetItem()
            self.listWidget.addItem(item_b)


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
        MainWindow.setWindowTitle(_translate("MainWindow", "Rent", None))
        self.search_Button.setText(_translate("MainWindow", "search", None))
        self.rent_Button.setText(_translate("MainWindow", "RENT", None))
        self.label.setText(_translate("MainWindow", "RENT PAGE", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.put_item_to_list()
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_rent_page('user1',3000000)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

