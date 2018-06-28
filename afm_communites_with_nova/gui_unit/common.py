# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
from PySide import QtGui

def select_directory(selected_directory):
    selected_directory.value = QtGui.QFileDialog.getExistingDirectory()

def select_file(selected_file):
    selected_file.value = QtGui.QFileDialog.getOpenFileName()

def show_message(message_wrapper):
    msgBox = QtGui.QMessageBox()
    message = message_wrapper.value
    if (isinstance(message, tuple)):
        message = message[0]
    try:
        msgBox.setText("Message: " + message)
    except Exception as e:
        msgBox.setText("Exception: " + e.message)
    msgBox.exec_()

class PathWrapper:
    def __init__(self, path = None):
        self.value = path