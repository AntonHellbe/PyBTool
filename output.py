# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybtool.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_connect = QtGui.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(60, 471, 230, 50))
        self.btn_connect.setObjectName(_fromUtf8("btn_connect"))
        self.btn_scan = QtGui.QPushButton(self.centralwidget)
        self.btn_scan.setGeometry(QtCore.QRect(60, 390, 230, 50))
        self.btn_scan.setObjectName(_fromUtf8("btn_scan"))
        self.te_device_adr = QtGui.QTextEdit(self.centralwidget)
        self.te_device_adr.setGeometry(QtCore.QRect(60, 70, 230, 40))
        self.te_device_adr.setObjectName(_fromUtf8("te_device_adr"))
        self.cb_device_connect = QtGui.QComboBox(self.centralwidget)
        self.cb_device_connect.setGeometry(QtCore.QRect(60, 230, 230, 40))
        self.cb_device_connect.setObjectName(_fromUtf8("cb_device_connect"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 200, 181, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 211, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_test_adr = QtGui.QPushButton(self.centralwidget)
        self.btn_test_adr.setGeometry(QtCore.QRect(60, 120, 94, 32))
        self.btn_test_adr.setObjectName(_fromUtf8("btn_test_adr"))
        self.tb_output = QtGui.QTextBrowser(self.centralwidget)
        self.tb_output.setGeometry(QtCore.QRect(400, 260, 301, 261))
        self.tb_output.setObjectName(_fromUtf8("tb_output"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 230, 63, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_connect.setText(_translate("MainWindow", "Connect", None))
        self.btn_scan.setText(_translate("MainWindow", "Scan", None))
        self.label.setText(_translate("MainWindow", "Select device to connect to", None))
        self.label_2.setText(_translate("MainWindow", "Manual Connect: Device Adress", None))
        self.btn_test_adr.setText(_translate("MainWindow", "Test Adress", None))
        self.label_3.setText(_translate("MainWindow", "Output", None))