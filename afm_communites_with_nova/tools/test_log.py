# -*- coding:UTF-8 -*-
'''
Created on Jun 30, 2018

@author: xiongan2
'''
import unittest

from tools.log import LogSystem

class TestGetLogMethods(unittest.TestCase):
    def test_get_log(self):
        logger = LogSystem.get_log("Test")
        logger.warning("Test add log")
    
if __name__ == '__main__':
    unittest.main()