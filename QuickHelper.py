# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/QuickHelper.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuickHelper(object):
    def setupUi(self, QuickHelper):
        QuickHelper.setObjectName("QuickHelper")
        QuickHelper.resize(400, 600)
        QuickHelper.setMinimumSize(QtCore.QSize(400, 600))
        QuickHelper.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(QuickHelper)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 531))
        self.listWidget.setObjectName("listWidget")
        self.pushBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushBackButton.setGeometry(QtCore.QRect(140, 550, 113, 32))
        self.pushBackButton.setObjectName("pushBackButton")
        QuickHelper.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuickHelper)
        self.statusbar.setObjectName("statusbar")
        QuickHelper.setStatusBar(self.statusbar)

        self.retranslateUi(QuickHelper)
        QtCore.QMetaObject.connectSlotsByName(QuickHelper)

    def retranslateUi(self, QuickHelper):
        _translate = QtCore.QCoreApplication.translate
        QuickHelper.setWindowTitle(_translate("QuickHelper", "QuickHelper"))
        self.pushBackButton.setText(_translate("QuickHelper", "Back"))
