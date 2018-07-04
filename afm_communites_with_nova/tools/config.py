# -*- coding:UTF-8 -*-
'''
Created on Jun 30, 2018

@author: Xor
'''
import ConfigParser

class ConfigureFile(object):
    __config = None
    
    def get_config():
        if ConfigureFile.__config is None:
            ConfigureFile.__config = ConfigParser.ConfigParser()
            ConfigureFile.__config.read('config.ini')
        
        return ConfigureFile.__config
    get_config = staticmethod(get_config)