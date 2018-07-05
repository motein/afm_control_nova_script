# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
import time
import sys
from PySide import QtCore, QtGui
from PySide.QtCore import QRunnable, QThreadPool, QCoreApplication

class Ui_Form(object):
    inProgress = True
    class StartRunnable(QRunnable):
        def run(self):
            count = 0
            Ui_Form.inProgress = True
            app = QCoreApplication.instance()
            while Ui_Form.inProgress == True:
                print("C Increasing")
                time.sleep(1)
                count += 1
            app.quit()
    class StopRunnable(QRunnable):
        def run(self):
            Ui_Form.inProgress = False
    
    def start_thread_func(self):
        runnable = Ui_Form.StartRunnable()
        QThreadPool.globalInstance().start(runnable)
        
    def stop_thread_func(self):
        runnable = Ui_Form.StopRunnable()
        QThreadPool.globalInstance().start(runnable)
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        
        self.start_button = QtGui.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(140, 170, 100, 40))
        self.start_button.setObjectName("Select File")
        self.start_button.clicked.connect(self.start_thread_func)
        
        self.stop_button = QtGui.QPushButton(Form)
        self.stop_button.setGeometry(QtCore.QRect(260, 170, 100, 40))
        self.stop_button.setObjectName("Select Path")
        self.stop_button.clicked.connect(self.stop_thread_func)

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
    app.aboutToQuit.connect(ui.stop_thread_func)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    test()