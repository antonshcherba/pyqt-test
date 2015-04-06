# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Mean.ui'
#
# Created: Mon Apr 06 23:56:49 2015
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
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 5, 1, 1)
        self.numberEdit = QtGui.QLineEdit(Dialog)
        self.numberEdit.setObjectName(_fromUtf8("numberEdit"))
        self.gridLayout.addWidget(self.numberEdit, 0, 0, 1, 2)
        self.calculateButton = QtGui.QPushButton(Dialog)
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.gridLayout.addWidget(self.calculateButton, 3, 0, 1, 1)
        self.arrayListWidget = QtGui.QListWidget(Dialog)
        self.arrayListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.arrayListWidget.setSelectionRectVisible(False)
        self.arrayListWidget.setObjectName(_fromUtf8("arrayListWidget"))
        self.gridLayout.addWidget(self.arrayListWidget, 1, 0, 1, 1)
        self.infoLabel = QtGui.QLabel(Dialog)
        self.infoLabel.setText(_fromUtf8(""))
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.gridLayout.addWidget(self.infoLabel, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.addButton.setText(_translate("Dialog", "Add", None))
        self.calculateButton.setText(_translate("Dialog", "Calculate", None))

