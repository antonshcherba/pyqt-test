__author__ = 'aDmin'

import sys
from Mean import *
from PyQt4.QtGui import *

array = []

class MeanView(QtGui.QDialog):


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.calculateButton, QtCore.SIGNAL('clicked()'), self.calculateMean)
        QtCore.QObject.connect(self.ui.addButton, QtCore.SIGNAL('clicked()'), self.addNumberToArray)
        QtCore.QObject.connect(self.ui.numberEdit, QtCore.SIGNAL('returnPressed()'), self.addNumberToArray)
        QtCore.QObject.connect(self.ui.editItemButton, QtCore.SIGNAL('clicked()'), self.editListItem)
        QtCore.QObject.connect(self.ui.deleteItemButton, QtCore.SIGNAL('clicked()'), self.deleteListItem)
        QtCore.QObject.connect(self.ui.deleteAllButton, QtCore.SIGNAL('clicked()'), self.deleteListContent)
        QtCore.QObject.connect(self.ui.openFileButton, QtCore.SIGNAL('clicked()'), self.loadDataFromFile)
        return None

    def loadDataFromFile(self):
        dataFileName = QFileDialog.getOpenFileName(self,'Open data','.','Text files (*.txt)')
        if (dataFileName.length() == 0):
            return 0

        dataFile = open(dataFileName, 'r')
        #loadedData = []
        for line in dataFile:
            if (isFloat(line)):
                number = float(line)
                #loadedData.append(number)
                array.append(number)
                self.ui.arrayListWidget.addItem(str(number))
            else:
                choise = self.showMessage(
                    'Invalid value!',
                    'Line ' + line + ' has incorrect data. Do you want to continue?',
                    QMessageBox.Ok|QMessageBox.Abort,
                    QMessageBox.Ok)
                if (choise != QMessageBox.Ok):
                    return 0

        #array.extend(loadedData)
        #self.ui.arrayListWidget.addItems(loadedData)
        return 0

    def editListItem(self):
        selectedItems = self.ui.arrayListWidget.selectedItems()
        if (len(selectedItems) == 0):
            return 0

        for item in selectedItems:
            itemRow = self.ui.arrayListWidget.row(item)

            number, ok = QInputDialog.getDouble(self, 'Enter new value', 'Change the old value: ' + str(array[itemRow]), decimals=8)
            if (ok):
                array[itemRow] = number
                self.ui.arrayListWidget.takeItem(itemRow)
                self.ui.arrayListWidget.insertItem(itemRow,str(number))

        self.ui.arrayListWidget.setCurrentRow(-1)
        return 0

    def deleteListItem(self):
        selectedItems = self.ui.arrayListWidget.selectedItems()
        if (len(selectedItems) == 0):
            return 0

        choise = self.showMessage(
            'Delete values!',
            'Do you really want to delete?',
            QMessageBox.Ok|QMessageBox.Cancel,
            QMessageBox.Cancel)
        if (choise == QMessageBox.Cancel):
            return 0

        for item in selectedItems:
            itemRow = self.ui.arrayListWidget.row(item)
            array.pop(itemRow)
            self.ui.arrayListWidget.takeItem(itemRow)

        self.ui.arrayListWidget.setCurrentRow(-1)
        return 0

    def deleteListContent(self):
        choise = self.showMessage(
            'Delete all values!',
            'Do you really want to delete?',
            QMessageBox.Ok|QMessageBox.Cancel,
            QMessageBox.Cancel)
        if (choise == QMessageBox.Cancel):
            return 0

        self.ui.arrayListWidget.clear()
        del array[:]
        return 0

    def addNumberToArray(self):
        numberString = str(self.ui.numberEdit.text()).strip(' \n')
        if (isFloat(numberString)):
            self.ui.infoLabel.setText('')
        elif (len(numberString) == 0):
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
        if (len(array) == 0):
            self.ui.infoLabel.setText('There is no data. Please, add values to list.')
            return 0

        sum = 0
        count = 0
        for index in xrange(1,len(array),2):
            if (array[index] % 2 == 0):
                sum += array[index]
                count += 1

        if (count == 0):
            self.ui.infoLabel.setText('There is no even numbers. Please change list values')
            return  0

        self.ui.infoLabel.setText(str(sum / count))
        return 0

    def showMessage(self, title, text, buttons, defaultButton):
        messageBox = QMessageBox()
        messageBox.setText(title)
        messageBox.setInformativeText(text)
        messageBox.setStandardButtons(buttons)
        messageBox.setDefaultButton(defaultButton)
        choise = messageBox.exec_()
        return choise
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