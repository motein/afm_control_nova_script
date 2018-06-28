# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: xiongan2
'''
from PySide import QtGui

def select_directory():
    selected_directory = QtGui.QFileDialog.getExistingDirectory()
    return selected_directory

def select_file():
    selected_file = QtGui.QFileDialog.getOpenFileName()
    return selected_file