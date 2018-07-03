# -*- coding:UTF-8 -*-
'''
Created on Jun 27, 2018

@author: xiongan2
'''
import unittest

from controller import AFMController

class TestControllerMethods(unittest.TestCase):
    def test_calcPositionMatrix(self):
        con = AFMController()
        con.prepareAfmExperiment()
        print(con.points)
        print(con.lines)
        print(con.setpoint)
        
    
if __name__ == '__main__':
    unittest.main()