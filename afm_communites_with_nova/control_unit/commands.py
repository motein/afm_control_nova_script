'''
Created on Jun 23, 2018

@author: xiongan2
'''
import sys
import picoscript
import time
import numpy as np
from enum import Enum

class Matrix_Type(Enum):
    MATRIX_8_8 = 1
    MATRIX_16_16 = 2
    
class Commands:
    def __init__(self):
        self.matrix_type = Matrix_Type.MATRIX_8_8
        self.setpoint = 1
        self.matrix_X = np.empty() # fast
        self.matrix_Y = np.empty() # slow
        self.settling_time_for_approach = 1
        self.settling_time_for_move = 1
        self.angle = None
        self.width = None
        self.center_x = None
        self.center_y = None
        
        
    def prepareAfmExperiment(self):
        picoscript.SetServoSetpoint(self.setpoint)
        self.angle = picoscript.GetScanAngle()
        self.width = picoscript.GetScanSize()
        self.center_x = picoscript.GetScanXOffset()
        self.center_y = picoscript.GetScanYOffset()
    
    def doApproach(self):
        picoscript.MotorApproach()
        time.sleep(self.settling_time_for_approach)
    
    def doWithdraw(self):
        picoscript.MotorWithdraw(self)
    
    def calcPositionMatrix(self, matrix_type):
        if matrix_type == Matrix_Type.MATRIX_8_8:
            Commands.__calcSpecifedPositionMatrix(8)
        elif matrix_type == Matrix_Type.MATRIX_16_16:
            Commands.__calcSpecifedPositionMatrix(16)
        else:
            print("Not supported yet")
            sys.exit()
    
    def __calcSpecifedPositionMatrix(self, points_number):
        self.matrix_X = np.zeros(points_number, points_number)
        self.matrix_Y = np.zeros(points_number, points_number)
        start_x = self.center_x - self.width / 2
        start_y = self.center_y - self.width / 2
        step_size = self.width / (points_number - 1) # minus 1
        # Initialize
        for i in range(points_number):
            for j in range(points_number):
                self.matrix_X[i, j] = start_x + j * step_size
                self.matrix_X[i, j] = start_y + j * step_size
                
        rotation = self.__create_rotation_matrix()
        # Rotate an angle
        for i in range(points_number):
            for j in range(points_number):
                original = np.matrix([self.matrix_X[i, j], self.matrix_Y[i, j]])
                transformed = np.matmul(original, rotation)
                self.matrix_X[i, j] = transformed[0]
                self.matrix_Y[i, j] = transformed[1]
        
    def __create_rotation_matrix(self):
        theta = np.radians(self.angle)
        c, s = np.cos(theta), np.sin(theta)
        rotation = np.array(((c,-s), (s, c)))
        return rotation
    
    def getPositionbyIndex(self, index):
        return [index, 1]
    
    def moveTip(self, fast, slow):
        picoscript.SetTipPosition(fast, slow)
        time.sleep(self.settling_time_for_move)
    
    def sendTriggerSingal(self):
        picoscript.SetOutputAux1(5) # Trigger a signal
        time.sleep(1)
        picoscript.SetOutputAux1(0)