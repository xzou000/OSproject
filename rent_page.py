# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rent_page.ui'
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

class Ui_rent_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.search = QtGui.QTextEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(20, 80, 421, 41))
        self.search.setObjectName(_fromUtf8("search"))
        self.search_Button = QtGui.QPushButton(self.centralwidget)
        self.search_Button.setGeometry(QtCore.QRect(560, 80, 121, 41))
        self.search_Button.setObjectName(_fromUtf8("search_Button"))
        self.back_Button = QtGui.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(570, 400, 121, 51))
        self.back_Button.setObjectName(_fromUtf8("back_Button"))
        self.rent_Button = QtGui.QPushButton(self.centralwidget)
        self.rent_Button.setGeometry(QtCore.QRect(570, 240, 121, 51))
        self.rent_Button.setObjectName(_fromUtf8("rent_Button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 190, 411, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
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
        self.back_Button.setText(_translate("MainWindow", "BACK", None))
        self.rent_Button.setText(_translate("MainWindow", "RENT", None))
        self.label.setText(_translate("MainWindow", "RENT PAGE", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "新建项目", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_rent_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

