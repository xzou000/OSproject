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
                self.listWidget.takeItem(self.listWidget.row(target_pter))
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
    ui = Ui_buy_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

