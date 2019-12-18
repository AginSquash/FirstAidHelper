# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reader(object):
    def setupUi(self, Reader):
        Reader.setObjectName("Reader")
        Reader.resize(375, 790)
        self.centralwidget = QtWidgets.QWidget(Reader)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 351, 711))
        self.textBrowser.setObjectName("textBrowser")
        self.push_goBack = QtWidgets.QPushButton(self.centralwidget)
        self.push_goBack.setGeometry(QtCore.QRect(130, 730, 113, 32))
        self.push_goBack.setObjectName("push_goBack")
        Reader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reader)
        self.statusbar.setObjectName("statusbar")
        Reader.setStatusBar(self.statusbar)

        self.retranslateUi(Reader)
        QtCore.QMetaObject.connectSlotsByName(Reader)

    def retranslateUi(self, Reader):
        _translate = QtCore.QCoreApplication.translate
        Reader.setWindowTitle(_translate("Reader", "Reader"))
        self.push_goBack.setText(_translate("Reader", "Назад"))
