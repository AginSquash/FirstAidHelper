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
        MainWindow.resize(375, 790)
        MainWindow.setMinimumSize(QtCore.QSize(375, 790))
        MainWindow.setMaximumSize(QtCore.QSize(375, 790))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(200, 720, 113, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.name_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.name_in.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.name_in.setObjectName("name_in")
        self.adress_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.adress_in.setEnabled(False)
        self.adress_in.setGeometry(QtCore.QRect(10, 110, 351, 31))
        self.adress_in.setObjectName("adress_in")
        self.symptom_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.symptom_in.setGeometry(QtCore.QRect(10, 180, 351, 531))
        self.symptom_in.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
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
        self.button_goBack = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack.setGeometry(QtCore.QRect(70, 720, 113, 32))
        self.button_goBack.setObjectName("button_goBack")
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
        self.adress_in.setPlainText(_translate("MainWindow", "Moscow, Vadkovsky per. 1"))
        self.label.setText(_translate("MainWindow", "Ваше Имя:"))
        self.label_2.setText(_translate("MainWindow", "Ваш адрес:"))
        self.label_3.setText(_translate("MainWindow", "Опишите, что с вами произошло:"))
        self.button_goBack.setText(_translate("MainWindow", "Назад"))
