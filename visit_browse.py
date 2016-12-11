# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visit_browse.ui'
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

class Ui_Buypage(object):

    def setbox(self,title, message):
        box=QtGui.QMessageBox()
        box.setIcon(QtGui.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtGui.QMessageBox.Ok)
        box.exec_()

    def searchitem(self):
        item_name = self.lineEdit.text()
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS WHERE ITEMNAME = ?", (item_name,))
        length = len(result.fetchone())
        if(length > 0):
            self.setbox("Found", "Your items are in the list.")# change to new page which show login already
        else:
            self.setbox('Item not Found!', 'Please try others')# warning page
        connection.close()

    def put_item_to_list(self):
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        counter = 0
        index = 0
        #print(len(result.fetchall()))
        for item in result:
            temp_str = 'Seller: ' + item[counter] + ':   Item name:  ' + item[counter+1] + '      Price:  $'+ str(item[counter+2]) + \
                                          '     Description:  '+ item[counter+3]
            print(temp_str)
            item_c = self.listWidget.item(index)
            item_c.setText(temp_str)
            index += 1
        connection.close()



    def setupUi(self, Buypage):
        Buypage.setObjectName(_fromUtf8("Buypage"))
        Buypage.resize(800, 600)
        self.listWidget = QtGui.QListWidget(Buypage)
        self.listWidget.setGeometry(QtCore.QRect(90, 200, 521, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        connection = sqlite3.connect('itemslist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        for items in result:
            item_b = QtGui.QListWidgetItem()
            self.listWidget.addItem(item_b)

        self.search_Button = QtGui.QPushButton(Buypage)
        self.search_Button.setGeometry(QtCore.QRect(590, 100, 121, 41))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.search_Button.clicked.connect(self.searchitem)

        self.label = QtGui.QLabel(Buypage)
        self.label.setGeometry(QtCore.QRect(50, 30, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Buypage)
        self.lineEdit.setGeometry(QtCore.QRect(90, 109, 431, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Buypage)
        QtCore.QMetaObject.connectSlotsByName(Buypage)

    def retranslateUi(self, Buypage):
        Buypage.setWindowTitle(_translate("Buypage", "buypage", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.put_item_to_list()
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.search_Button.setText(_translate("Buypage", "search", None))
        self.label.setText(_translate("Buypage", "BUY PAGE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Buypage = QtGui.QWidget()
    ui = Ui_Buypage()
    ui.setupUi(Buypage)
    Buypage.show()
    sys.exit(app.exec_())

