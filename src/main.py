# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Feb  6 11:46:59 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1039, 696)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.bottomFrame.setGeometry(QtCore.QRect(10, 630, 1021, 31))
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.label = QtWidgets.QLabel(self.bottomFrame)
        self.label.setGeometry(QtCore.QRect(450, 10, 111, 16))
        self.label.setObjectName("label")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 1021, 601))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.searchFrame = QtWidgets.QFrame(self.mainFrame)
        self.searchFrame.setGeometry(QtCore.QRect(0, 50, 1021, 41))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.searchLineEdit.setGeometry(QtCore.QRect(10, 0, 881, 41))
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchButton = QtWidgets.QPushButton(self.searchFrame)
        self.searchButton.setGeometry(QtCore.QRect(890, 0, 121, 41))
        self.searchButton.setObjectName("searchButton")
        self.mainTable = QtWidgets.QTableView(self.mainFrame)
        self.mainTable.setGeometry(QtCore.QRect(10, 120, 1001, 461))
        self.mainTable.setObjectName("mainTable")
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setGeometry(QtCore.QRect(10, 0, 991, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(self.frame)
        self.delButton.setGeometry(QtCore.QRect(120, 0, 121, 41))
        self.delButton.setObjectName("delButton")
        self.changeButton = QtWidgets.QPushButton(self.frame)
        self.changeButton.setGeometry(QtCore.QRect(240, 0, 121, 41))
        self.changeButton.setObjectName("changeButton")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 41))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.quitButton = QtWidgets.QPushButton(self.frame)
        self.quitButton.setGeometry(QtCore.QRect(380, 0, 121, 41))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1039, 26))
        self.menuBar.setObjectName("menuBar")
        self.sysMenu = QtWidgets.QMenu(self.menuBar)
        self.sysMenu.setObjectName("sysMenu")
        self.elseMenu = QtWidgets.QMenu(self.menuBar)
        self.elseMenu.setObjectName("elseMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionChange = QtWidgets.QAction(MainWindow)
        self.actionChange.setObjectName("actionChange")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.sysMenu.addAction(self.actionChange)
        self.sysMenu.addAction(self.actionQuit)
        self.elseMenu.addAction(self.actionAbout)
        self.menuBar.addAction(self.sysMenu.menuAction())
        self.menuBar.addAction(self.elseMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.clickQuitButton)
        self.addButton.clicked.connect(MainWindow.clickAddButton)
        self.delButton.clicked.connect(MainWindow.clickDelButton)
        self.changeButton.clicked.connect(MainWindow.clickChangeButton)
        self.searchButton.clicked.connect(MainWindow.clickSearchButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "通讯备忘录"))
        self.label.setText(_translate("MainWindow", "yunsle荣誉出品"))
        self.searchButton.setText(_translate("MainWindow", "查找联系人"))
        self.addButton.setText(_translate("MainWindow", "添加"))
        self.delButton.setText(_translate("MainWindow", "删除"))
        self.changeButton.setText(_translate("MainWindow", "修改"))
        self.quitButton.setText(_translate("MainWindow", "退出"))
        self.sysMenu.setTitle(_translate("MainWindow", "系统"))
        self.elseMenu.setTitle(_translate("MainWindow", "其他"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actionChange.setText(_translate("MainWindow", "修改密码"))
        self.actionChange.setToolTip(_translate("MainWindow", "修改密码"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionAbout.setToolTip(_translate("MainWindow", "关于"))
