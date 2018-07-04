# -*- coding:UTF-8 -*-
'''
Created on Jun 30, 2018

@author: xiongan2
'''
import logging

class LogSystem(object):
    file_name = 'robot.log'
    logging.basicConfig(filename=file_name, level=logging.DEBUG)
    
    def get_log(name):
        return logging.getLogger(name)
    get_log = staticmethod(get_log)