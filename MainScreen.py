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
        MainWindow.resize(375, 790)
        MainWindow.setMinimumSize(QtCore.QSize(375, 790))
        MainWindow.setMaximumSize(QtCore.QSize(375, 790))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushFAH_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushFAH_button.setGeometry(QtCore.QRect(90, 170, 201, 171))
        self.pushFAH_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushFAH_button.setAutoFillBackground(False)
        self.pushFAH_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushFAH_button.setIcon(icon)
        self.pushFAH_button.setCheckable(False)
        self.pushFAH_button.setAutoDefault(True)
        self.pushFAH_button.setDefault(True)
        self.pushFAH_button.setFlat(True)
        self.pushFAH_button.setObjectName("pushFAH_button")
        self.pushQH_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushQH_button.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.pushQH_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/void.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushQH_button.setIcon(icon1)
        self.pushQH_button.setFlat(True)
        self.pushQH_button.setObjectName("pushQH_button")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 375, 770))
        self.background_label.setMaximumSize(QtCore.QSize(375, 830))
        self.background_label.setAutoFillBackground(True)
        self.background_label.setText("")
        self.background_label.setTextFormat(QtCore.Qt.AutoText)
        self.background_label.setPixmap(QtGui.QPixmap(":/newPrefix/tg_image_3861561027.jpeg"))
        self.background_label.setScaledContents(True)
        self.background_label.setAlignment(QtCore.Qt.AlignCenter)
        self.background_label.setWordWrap(False)
        self.background_label.setIndent(-2)
        self.background_label.setObjectName("background_label")
        self.background_label.raise_()
        self.pushQH_button.raise_()
        self.pushFAH_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import resources_rc
