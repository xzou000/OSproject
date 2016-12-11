# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visit_rent.ui'
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

class Ui_rent(object):

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



    def setupUi(self, rent):
        rent.setObjectName(_fromUtf8("rent"))
        rent.resize(800, 600)
        self.lineEdit = QtGui.QLineEdit(rent)
        self.lineEdit.setGeometry(QtCore.QRect(80, 99, 431, 31))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.search_Button = QtGui.QPushButton(rent)
        self.search_Button.setGeometry(QtCore.QRect(580, 90, 121, 41))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.listWidget = QtGui.QListWidget(rent)
        self.listWidget.setGeometry(QtCore.QRect(80, 190, 521, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        connection = sqlite3.connect('rentlist.db')
        result = connection.execute("SELECT * FROM ITEMS")
        for items in result:
            item_b = QtGui.QListWidgetItem()
            self.listWidget.addItem(item_b)


        self.label = QtGui.QLabel(rent)
        self.label.setGeometry(QtCore.QRect(50, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(rent)
        QtCore.QMetaObject.connectSlotsByName(rent)

    def retranslateUi(self, rent):
        rent.setWindowTitle(_translate("rent", "rentpage", None))
        self.search_Button.setText(_translate("rent", "search", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.put_item_to_list()
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("rent", "RENT PAGE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    rent = QtGui.QWidget()
    ui = Ui_rent()
    ui.setupUi(rent)
    rent.show()
    sys.exit(app.exec_())

