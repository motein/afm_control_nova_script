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

def show_message(message_wrapper):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(" ")
    message = message_wrapper.value
    if (isinstance(message, tuple)):
        message = message[0]
    try:
        msgBox.setText("Message: " + message)
    except (Exception, AttributeError) as e:
        msgBox.setText("Exception: " + e.message)
    msgBox.exec_()

def show_value(value):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(" ")
    msgBox.setText("Value: " + str(value))
    msgBox.exec_()

class PathWrapper:
    def __init__(self, path = None):
        self.value = path