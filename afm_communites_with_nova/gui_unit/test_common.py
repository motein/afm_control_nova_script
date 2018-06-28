'''
Created on Jun 28, 2018

@author: xiongan2
'''
from PySide import QtCore, QtGui
from gui_unit.common import select_directory, select_file

x = None
app = QtGui.QApplication([])

button = QtGui.QPushButton("Select File")
button.clicked.connect(select_file)
button.show()

app.exec_()