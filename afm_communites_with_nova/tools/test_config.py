# -*- coding:UTF-8 -*-
'''
Created on Jun 30, 2018

@author: xiongan2
'''
import unittest

from tools.config import ConfigureFile

class TestGetConfigMethods(unittest.TestCase):
    def test_get_conf(self):
        conf = ConfigureFile.get_config()
        print(conf.get('DEFAULT', 'StateCheckInterval'))
    
if __name__ == '__main__':
    unittest.main()