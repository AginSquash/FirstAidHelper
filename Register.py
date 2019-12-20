# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registorWindow(object):
    def setupUi(self, registorWindow):
        registorWindow.setObjectName("registorWindow")
        registorWindow.resize(400, 790)
        self.centralwidget = QtWidgets.QWidget(registorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 240, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(60, 270, 281, 21))
        self.lineName.setObjectName("lineName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 320, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 350, 281, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineSymptoms = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSymptoms.setGeometry(QtCore.QRect(60, 430, 281, 191))
        self.lineSymptoms.setObjectName("lineSymptoms")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 400, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(140, 680, 113, 32))
        self.register_button.setObjectName("register_button")
        registorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(registorWindow)
        self.statusbar.setObjectName("statusbar")
        registorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(registorWindow)
        QtCore.QMetaObject.connectSlotsByName(registorWindow)

    def retranslateUi(self, registorWindow):
        _translate = QtCore.QCoreApplication.translate
        registorWindow.setWindowTitle(_translate("registorWindow", "Регистрация"))
        self.label.setText(_translate("registorWindow", "<html><head/><body><p align=\"center\">Добро пожаловать!<br/><br/>Пожалуйста, зарегистрируйтесь</p></body></html>"))
        self.label_2.setText(_translate("registorWindow", "Имя:"))
        self.label_3.setText(_translate("registorWindow", "Адрес:"))
        self.lineEdit_2.setText(_translate("registorWindow", "Moscow, Vadkovsky per. 1"))
        self.label_4.setText(_translate("registorWindow", "Заболевания:"))
        self.register_button.setText(_translate("registorWindow", "Регистрация"))
