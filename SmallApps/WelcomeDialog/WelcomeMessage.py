# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\WelcomeMessage.ui'
#
# Created: Mon Apr 06 16:36:53 2015
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
        Dialog.resize(397, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineUserName = QtGui.QLineEdit(Dialog)
        self.lineUserName.setObjectName(_fromUtf8("lineUserName"))
        self.gridLayout.addWidget(self.lineUserName, 0, 1, 1, 1)
        self.labelMessage = QtGui.QLabel(Dialog)
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.gridLayout.addWidget(self.labelMessage, 1, 1, 1, 1)
        self.labelEnterName = QtGui.QLabel(Dialog)
        self.labelEnterName.setObjectName(_fromUtf8("labelEnterName"))
        self.gridLayout.addWidget(self.labelEnterName, 0, 0, 1, 1)
        self.clickMeButton = QtGui.QPushButton(Dialog)
        self.clickMeButton.setObjectName(_fromUtf8("clickMeButton"))
        self.gridLayout.addWidget(self.clickMeButton, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.clickMeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineUserName.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit Dialog", None))
        self.labelEnterName.setText(_translate("Dialog", "Enter your name:", None))
        self.clickMeButton.setText(_translate("Dialog", "&Click Me", None))

