__author__ = 'aDmin'

import sys
from Calculator import *

class CalculatorView(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.AddButton, QtCore.SIGNAL('clicked()'), self.calculate)

    def calculate(self):
        result = ''

        firstNumber = str(self.ui.lineFirstNumber.text())
        if firstNumber.isdigit():
            firstNumber = float(firstNumber)
        else:
            result += '\tError: Invalid value of the first number'

        secondNumber = str(self.ui.lineSecondNumber.text())
        if secondNumber.isdigit():
            secondNumber = float(secondNumber)
        else:
            result += '\tError: Invalid value of the second number'
        if result == '':
            result = str(firstNumber + secondNumber)

        self.ui.labelResult.setText(result)
        return 0

app = QtGui.QApplication(sys.argv)
view = CalculatorView()
view.show()
sys.exit(app.exec_())