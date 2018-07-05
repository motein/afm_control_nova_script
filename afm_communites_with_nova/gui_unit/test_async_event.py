# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
import time
import sys
from functools import partial
from PySide import QtCore, QtGui
from PySide.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot

@Slot(str) 
def demo_speak_message(value, typeInfo = "Info"):
    msgBox = QtGui.QMessageBox()
    msgBox.setIcon(QtGui.QMessageBox.Information)
    msgBox.setText(typeInfo + ": " + str(value))
    msgBox.exec_()

class Communicate(QObject):                                                   
    speak_number = Signal()
    speak_message = Signal(str, str)

class Ui_Form(object):
    inProgress = True
    class StartRunnable(QRunnable):
        def __init__(self, ui):
            self.ui = ui
            QRunnable.__init__(self)
            
        def run(self):
            count = 0
            #self.ui.someone.speak_number.emit()
            self.ui.someone.speak_message.emit("Yeah", "Info")
            Ui_Form.inProgress = True
            while Ui_Form.inProgress == True:
                print("C Increasing")
                time.sleep(1)
                count += 1
                
    class StopRunnable(QRunnable):
        def __init__(self, ui):
            self.ui = ui
            QRunnable.__init__(self)
            
        def run(self):
            Ui_Form.inProgress = False
    
    def start_thread_func(self, ui):
        runnable = Ui_Form.StartRunnable(ui)
        QThreadPool.globalInstance().start(runnable)
        
    def stop_thread_func(self, ui):
        runnable = Ui_Form.StopRunnable(ui)
        QThreadPool.globalInstance().start(runnable)
    
    @Slot(str)
    def sayHello(self):
        self.stop_button.setText("AAA")
        QtGui.QApplication.processEvents()
        time.sleep(2)
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.someone = Communicate()
        self.someone.speak_number.connect(self.sayHello)
        self.someone.speak_message.connect(demo_speak_message)
        self.start_button = QtGui.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(140, 170, 100, 40))
        self.start_button.setObjectName("Select File")
        self.start_button.clicked.connect(partial(self.start_thread_func, self))
        
        self.stop_button = QtGui.QPushButton(Form)
        self.stop_button.setGeometry(QtCore.QRect(260, 170, 100, 40))
        self.stop_button.setObjectName("Select Path")
        self.stop_button.clicked.connect(partial(self.stop_thread_func, self))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Select Form", None, QtGui.QApplication.UnicodeUTF8))
        self.start_button.setText(QtGui.QApplication.translate("Form", "Start Button", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_button.setText(QtGui.QApplication.translate("Form", "Stop Button", None, QtGui.QApplication.UnicodeUTF8))

def test():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    app.aboutToQuit.connect(partial(ui.stop_thread_func, ui))
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    test()