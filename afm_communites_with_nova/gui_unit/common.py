# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
from PySide import QtGui

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