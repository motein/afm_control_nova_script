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
    
class AFMController:
    def __init__(self):
        self.matrix_type = Matrix_Type.MATRIX_8_8
        self.setpoint = 1
        self.matrix_X = np.empty(shape=[0, 0]) # fast
        self.matrix_Y = np.empty(shape=[0, 0]) # slow
        self.angle = None
        self.width = None
        self.center_x = None
        self.center_y = None
        self.points_number = None
        
        
    def prepareAfmExperiment(self):
        self.setpoint = picoscript.GetServoSetpoint()
        self.angle = picoscript.GetScanAngle()
        self.width = picoscript.GetScanSize()
        self.center_x = picoscript.GetScanXOffset()
        self.center_y = picoscript.GetScanYOffset()
    
    def doApproach(self, setpoint = None):
        if setpoint is not None:
            picoscript.SetServoSetpoint(setpoint)
            
        picoscript.MotorApproach()
    
    def doWithdraw(self):
        picoscript.MotorWithdraw(self)
    
    def calcPositionMatrix(self, matrix_type):
        if matrix_type == Matrix_Type.MATRIX_8_8:
            self.points_number = 8
            self.__calcSpecifedPositionMatrix()
        elif matrix_type == Matrix_Type.MATRIX_16_16:
            self.points_number = 16
            self.__calcSpecifedPositionMatrix()
        else:
            print("Not supported yet")
            sys.exit()
    
    def __calcSpecifedPositionMatrix(self):
        self.matrix_X = np.zeros(self.points_number, self.points_number)
        self.matrix_Y = np.zeros(self.points_number, self.points_number)
        start_x = self.center_x - self.width / 2
        start_y = self.center_y - self.width / 2
        step_size = self.width / (self.points_number - 1) # minus 1
        # Initialize
        for i in range(self.points_number):
            for j in range(self.points_number):
                self.matrix_X[i, j] = start_x + j * step_size
                self.matrix_X[i, j] = start_y + j * step_size
                
        rotation = self.__create_rotation_matrix()
        # Rotate an angle
        for i in range(self.points_number):
            for j in range(self.points_number):
                original = np.matrix([self.matrix_X[i, j], self.matrix_Y[i, j]])
                transformed = np.matmul(original, rotation)
                self.matrix_X[i, j] = transformed[0]
                self.matrix_Y[i, j] = transformed[1]
        
    def __create_rotation_matrix(self):
        theta = np.radians(self.angle)
        c, s = np.cos(theta), np.sin(theta)
        rotation = np.array(((c,-s), (s, c)))
        return rotation
    
    def getPositionbyIndex(self, x_index, y_index):
        return self.matrix_X[x_index, y_index], self.matrix_Y[x_index, y_index]
    
    def moveTip(self, fast, slow):
        picoscript.SetTipPosition(fast, slow)
    
    def sendTriggerSingal(self, high_vol, low_vol, holding_time):
        picoscript.SetOutputAux1(high_vol) # Trigger a signal
        time.sleep(holding_time)
        picoscript.SetOutputAux1(low_vol)
        
    def getPointsNumber(self):
        return self.points_number