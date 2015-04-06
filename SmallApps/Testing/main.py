__author__ = 'aDmin'

import sys
from Mean import *

array = []

class MeanView(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL('clicked()'), self.calculateMean)
        QtCore.QObject.connect(self.ui.addButton, QtCore.SIGNAL('clicked()'), self.addNumberToArray)
        QtCore.QObject.connect(self.ui.numberEdit, QtCore.SIGNAL('returnPressed()'), self.addNumberToArray)

    def addNumberToArray(self):
        numberString = str(self.ui.numberEdit.text()).strip(' \n')
        if isFloat(numberString):
            self.ui.infoLabel.setText('')
        elif len(numberString) == 0:
            return 0
        else:
            self.ui.infoLabel.setText('Invalid number value! Please enter correct data.')
            return 0

        array.append(float(numberString))
        self.ui.arrayListWidget.addItem(numberString)
        self.ui.numberEdit.setText('')
        self.ui.numberEdit.setFocus()

        return 0

    def calculateMean(self):
        sum = 0
        count = int(len(array) / 2)
        for index in xrange(1,len(array),2):
            sum += array[index]

        self.ui.infoLabel.setText(str(sum / count))
        return 0

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


app = QtGui.QApplication(sys.argv)
view = MeanView()
view.show()
sys.exit(app.exec_())