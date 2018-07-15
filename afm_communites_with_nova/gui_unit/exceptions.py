# -*- coding:UTF-8 -*-
'''
Created on Jul 15, 2018

@author: xiongan2
'''
class NotConnectException(Exception):
    def __init__(self):
        err = 'Perhaps, PicoView is not connected'
        Exception.__init__(self, err)