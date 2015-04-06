# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Calculator.ui'
#
# Created: Mon Apr 06 19:01:35 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelFirstNumber = QtGui.QLabel(Dialog)
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.gridLayout.addWidget(self.labelFirstNumber, 0, 0, 1, 1)
        self.lineFirstNumber = QtGui.QLineEdit(Dialog)
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.gridLayout.addWidget(self.lineFirstNumber, 0, 1, 1, 1)
        self.lineSecondNumber = QtGui.QLineEdit(Dialog)
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))
        self.gridLayout.addWidget(self.lineSecondNumber, 1, 1, 1, 1)
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.gridLayout.addWidget(self.AddButton, 4, 0, 1, 1)
        self.labelSecondNumber = QtGui.QLabel(Dialog)
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.gridLayout.addWidget(self.labelSecondNumber, 1, 0, 1, 1)
        self.labelResult = QtGui.QLabel(Dialog)
        self.labelResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.gridLayout.addWidget(self.labelResult, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number", None))
        self.labelResult.setText(_translate("Dialog", "0", None))

