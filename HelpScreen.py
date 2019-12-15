# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/HelpScreen.ui'
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
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(140, 540, 113, 32))
        self.button.setObjectName("button")
        self.name_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.name_in.setGeometry(QtCore.QRect(20, 40, 361, 31))
        self.name_in.setObjectName("name_in")
        self.adress_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.adress_in.setGeometry(QtCore.QRect(20, 110, 361, 31))
        self.adress_in.setObjectName("adress_in")
        self.symptom_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.symptom_in.setGeometry(QtCore.QRect(20, 180, 361, 351))
        self.symptom_in.setObjectName("symptom_in")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 361, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 361, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вызов помощи"))
        self.button.setText(_translate("MainWindow", "Отправить"))
        self.label.setText(_translate("MainWindow", "Ваше Имя:"))
        self.label_2.setText(_translate("MainWindow", "Ваш адрес:"))
        self.label_3.setText(_translate("MainWindow", "Опишите, что с вами произошло:"))
