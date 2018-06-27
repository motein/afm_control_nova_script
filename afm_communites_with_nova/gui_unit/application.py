# -*- coding:UTF-8 -*-
'''
Created on Jun 26, 2018

@author: xiongan2
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *

def createApplication():
    app = QApplication(sys.argv)
    label = QLabel("PySide on Windows")
    label.show()
    app.exec_()
    sys.exit()
    
if __name__ == '__main__':  
    createApplication()
