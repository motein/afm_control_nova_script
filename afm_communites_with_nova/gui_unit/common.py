# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
import time
from PySide import QtGui
from PySide.QtCore import QObject, Signal, QRunnable, QThreadPool, Slot
from os import path
from workflow_unit.workflow import Workflow
from tools.config import ConfigureFile

def check_file_suffix(file_path, file_suffix):
    result = get_file_suffix(file_path)
    if (result == file_suffix):
        return True
    
    return False

def get_file_suffix(file_path):
    result = path.splitext(file_path)
#     print(result)
    return result[-1]

def get_file_name(file_path):
    result = path.split(file_path)
#     print(result)
    return result[-1] 

def select_directory(selected_directory, callback = None):
    selected_directory.value = QtGui.QFileDialog.getExistingDirectory()
    if callback is not None:
        callback()

def select_file(selected_file, callback = None):
    selected_file.value = QtGui.QFileDialog.getOpenFileName()[0]
    if callback is not None:
        callback()

def show_message_wrapper(message_wrapper):
    msgBox = QtGui.QMessageBox()
    
    message = message_wrapper.value
    if (isinstance(message, tuple)):
        message = message[0]
    try:
        msgBox.setWindowTitle("Info")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText(message)
    except (Exception, AttributeError) as e:
        msgBox.setWindowTitle("Error")
        msgBox.setIcon(QtGui.QMessageBox.Critical)
        msgBox.setText(e.message)
    msgBox.exec_()

def show_message(value, message_type='Info'):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(message_type)
    windowIcon = QtGui.QIcon()
    windowIcon.addPixmap(QtGui.QPixmap("../resources/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msgBox.setWindowIcon(windowIcon)
    
    msgBox.setIcon(QtGui.QMessageBox.Information)
    if message_type.lower() == "warning":
        msgBox.setIcon(QtGui.QMessageBox.Warning)
    elif message_type.lower() == "error":
        msgBox.setIcon(QtGui.QMessageBox.Critical)

    msgBox.setText(str(value))
    msgBox.exec_()

class PathWrapper:
    def __init__(self, path = None):
        self.value = path
        
@Slot(str)
def speak_message(value, message_type='Info'):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(message_type)
    windowIcon = QtGui.QIcon()
    windowIcon.addPixmap(QtGui.QPixmap("../resources/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msgBox.setWindowIcon(windowIcon)
    
    msgBox.setIcon(QtGui.QMessageBox.Information)
    if message_type.lower() == "warning":
        msgBox.setIcon(QtGui.QMessageBox.Warning)
    elif message_type.lower() == "error":
        msgBox.setIcon(QtGui.QMessageBox.Critical)
    msgBox.setText(str(value))
    msgBox.exec_()
    
class Communicate(QObject):                                                   
    speak_message = Signal(str, str)

class StartRunnable(QRunnable):
    def __init__(self, ui):
        self.ui = ui
        self.conf = ConfigureFile.get_config()
        self.short_delay = self.conf.getfloat('GUI_DELAY_DEFAULT', 'ShortDelay')
        self.mid_delay = self.conf.getfloat('GUI_DELAY_DEFAULT', 'MiddleDelay')
        
        QRunnable.__init__(self)
        
    def run(self):
        print("Start Experiment")
        if Workflow.InProgress == True:
            return
        
        Workflow.InProgress = True
        self.ui.startExperimentButton.setEnabled(False)
        QtGui.QApplication.processEvents()
        time.sleep(self.short_delay)
        self.ui.stopExperimentButton.setEnabled(True)
        QtGui.QApplication.processEvents()
        time.sleep(self.short_delay)
        self.ui.progressBar.setProperty("value", 0)
        QtGui.QApplication.processEvents()
        time.sleep(self.short_delay)
        
        try:
            self.ui.com.speak_message.emit("Experiment started...", "Info")
            time.sleep(self.mid_delay )
            self.ui.workflow.start_to_work(self.ui, self.ui.setPositionInfoLabelText, self.ui.updateProgress)
        finally:
            self.ui.progressBar.setProperty("value", 100)
            QtGui.QApplication.processEvents()
            time.sleep(self.short_delay)
            Workflow.InProgress = False
            self.ui.stopExperimentButton.setEnabled(False)
            QtGui.QApplication.processEvents()
            time.sleep(self.short_delay)
            self.ui.startExperimentButton.setEnabled(True)
            QtGui.QApplication.processEvents()
            time.sleep(self.short_delay)

class StopRunnable(QRunnable):
    def run(self):
        Workflow.InProgress = False
        print("Stop Experiment")

def start_thread_func(ui):
    runnable = StartRunnable(ui)
    QThreadPool.globalInstance().start(runnable)

def stop_thread_func():
    runnable = StopRunnable()
    QThreadPool.globalInstance().start(runnable)