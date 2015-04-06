__author__ = 'aDmin'

import sys

from WelcomeMessage import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.clickMeButton, QtCore.SIGNAL('clicked()'), self.dispMessage)

    def dispMessage(self):
        self.ui.labelMessage.setText('Hello ' + self.ui.lineUserName.text() + '!!! Have a nice day')

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
sys.exit(app.exec_())