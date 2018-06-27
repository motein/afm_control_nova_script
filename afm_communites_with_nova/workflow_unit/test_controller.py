'''
Created on Jun 27, 2018

@author: xiongan2
'''
import unittest

from controller import AFMController, Matrix_Type

class TestControllerMethods(unittest.TestCase):
    def test_calcPositionMatrix(self):
        con = AFMController()
        con.angle = 30.0
        con.width = 10.0
        con.center_x = 0.0
        con.center_y = 0.0
        print(con.width)
        con.calcPositionMatrix(Matrix_Type.MATRIX_8_8)
        print(con.matrix_X)
        print(con.matrix_Y)
        print(con.getPointsNumber())
        print(con.getPositionbyIndex(2, 5))
    
if __name__ == '__main__':
    unittest.main()