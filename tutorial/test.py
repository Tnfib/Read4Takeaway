import sys
#from PyQt4.QtWidgets import *
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import pyqtSlot
from random import randint
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *


from PyQt4.QtGui import QIcon, QColor
from PyQt4.QtCore import pyqtSlot, Qt, QTimer

import time
class TableWidgetItem(QTableWidgetItem):
    def setData(self, role, value):
        if role == Qt.DisplayRole:
            try:
                newvalue = int(value)
                oldvalue = int(self.data(role))
            except (ValueError, TypeError):
                pass
            else:
                current_color = QColor('aliceblue')
                def update_background(current_color=None):
                    if current_color == QColor('aliceblue'):
                        current_color = QColor('lightyellow')
                    else:
                        current_color = QColor('aliceblue')
                    super(TableWidgetItem, self).setData(
                        Qt.BackgroundRole, current_color)
                current_color = update_background(current_color=current_color)
                #QTimer.singleShot(2000, update_background)

                timer = QTimer()
                timer.timeout.connect(update_background)
                timer.start(100)
                #time.sleep(.5)
                #timer.stop()
            super(TableWidgetItem, self).setData(role, value)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 100, 350, 380)
        self.createTable()
        self.button = QPushButton('Update Values', self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.populateTable)
        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.nrows=10
        self.ncols=3
        self.tableWidget.setRowCount(self.nrows)
        self.tableWidget.setColumnCount(self.ncols)

        for i in range(self.nrows):
            for j in range(self.ncols):
                self.tableWidget.setItem(i, j, TableWidgetItem())

        self.tableWidget.move(0,0)
        self.tableWidget.doubleClicked.connect(self.populateTable)
        self.populateTable()

    @pyqtSlot()
    def populateTable(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.tableWidget.item(i, j).setText('{}'.format(randint(0,9)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())