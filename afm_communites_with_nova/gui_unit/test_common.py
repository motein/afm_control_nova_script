# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
import sys
from PySide import QtCore, QtGui
from functools import partial
from gui_unit.common import select_directory, select_file, show_message_wrapper, PathWrapper

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        
        self.path = PathWrapper("")
        self.select_file_button = QtGui.QPushButton(Form)
        self.select_file_button.setGeometry(QtCore.QRect(140, 170, 100, 40))
        self.select_file_button.setObjectName("Select File")
        self.select_file_button.clicked.connect(partial(select_file, self.path))
        
        self.select_path_button = QtGui.QPushButton(Form)
        self.select_path_button.setGeometry(QtCore.QRect(260, 170, 100, 40))
        self.select_path_button.setObjectName("Select Path")
        self.select_path_button.clicked.connect(partial(select_directory, self.path))
        
        self.show_button = QtGui.QPushButton(Form)
        self.show_button.setGeometry(QtCore.QRect(200, 220, 100, 40))
        self.show_button.setObjectName("Show Button")
        self.show_button.clicked.connect(partial(show_message_wrapper, self.path))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Select Form", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file_button.setText(QtGui.QApplication.translate("Form", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.select_path_button.setText(QtGui.QApplication.translate("Form", "Select Path", None, QtGui.QApplication.UnicodeUTF8))
        self.show_button.setText(QtGui.QApplication.translate("Form", "Show Button", None, QtGui.QApplication.UnicodeUTF8))

def test():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

def test2():
    path = PathWrapper()
    select_directory(path)
    print(path.value)
    

if __name__ == '__main__':
    test()