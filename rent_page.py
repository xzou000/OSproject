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

    def setbox(self,title, message):
        box=QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()


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
                PRICE = ? AND DESCRIPTION = ?", (item[counter], item[counter+1], item[counter+2], item[counter+3],))
                self.listWidget.takeItem(self.listWidget.row(target_pter))
                break
            index += 1
        connection.commit()
        connection.close()


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
    ui = Ui_rent_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

