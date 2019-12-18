# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushFAH_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushFAH_button.setGeometry(QtCore.QRect(100, 510, 181, 61))
        self.pushFAH_button.setObjectName("pushFAH_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 200, 200))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/black-magic.gif"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushQH_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushQH_button.setGeometry(QtCore.QRect(100, 440, 181, 61))
        self.pushQH_button.setObjectName("pushQH_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushFAH_button.setText(_translate("MainWindow", "Get First Help Online!"))
        self.pushQH_button.setText(_translate("MainWindow", "Get Qucik Help!"))
import resources_rc
