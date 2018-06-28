'''
Created on Jun 28, 2018

@author: xiongan2
'''
import sys
from PySide import QtCore, QtGui
from functools import partial
from gui_unit.common import select_directory, select_file, show_message, PathWrapper

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 435)
        self.path = PathWrapper("")
        self.select_button = QtGui.QPushButton(Form)
        self.select_button.setGeometry(QtCore.QRect(250, 170, 211, 20))
        self.select_button.setObjectName("Select File")
        self.select_button.clicked.connect(partial(select_directory, self.path))
        
        self.show_button = QtGui.QPushButton(Form)
        self.show_button.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.show_button.setObjectName("Show Button")
        self.show_button.clicked.connect(partial(show_message, self.path))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.select_button.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.show_button.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

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