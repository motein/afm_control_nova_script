# -*- coding:UTF-8 -*-
'''
Created on Jun 23, 2018

@author: xiongan2
'''
import sys
import picoscript
import time
import logging
import numpy as np
from enum import Enum

class Matrix_Type(Enum):
    MATRIX_8_8 = 0
    MATRIX_16_16 = 1
    MATRIX_32_32 = 2
    MATRIX_64_64 = 3
    MATRIX_128_128 = 4
    MATRIX_256_256 = 5
    MATRIX_512_512 = 6
    
class AFMController:
    def __init__(self):
        logging.basicConfig(filename='../data/afm_nova.log',level=logging.DEBUG) # Log system
        self.matrix_type = Matrix_Type.MATRIX_8_8
        self.points_number = 8
        self.setpoint = 1
        self.matrix_X = np.empty(shape=[0, 0]) # fast
        self.matrix_Y = np.empty(shape=[0, 0]) # slow
        self.angle = None
        self.width = None
        self.center_x = None
        self.center_y = None
        
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
        elif matrix_type == Matrix_Type.MATRIX_16_16:
            self.points_number = 16
        elif matrix_type == Matrix_Type.MATRIX_32_32:
            self.points_number = 32
        elif matrix_type == Matrix_Type.MATRIX_64_64:
            self.points_number = 64
        elif matrix_type == Matrix_Type.MATRIX_128_128:
            self.points_number = 128
        elif matrix_type == Matrix_Type.MATRIX_256_256:
            self.points_number = 256
        elif matrix_type == Matrix_Type.MATRIX_512_512:
            self.points_number = 512
        else:
            print("Not supported yet")
            logging.warning("Not supported yet")
            sys.exit()
            
        self.__calcSpecifedPositionMatrix()
    
    def __calcSpecifedPositionMatrix(self):
        self.matrix_X = np.zeros(shape=[self.points_number, self.points_number])
        self.matrix_Y = np.zeros(shape=[self.points_number, self.points_number])
        start_x = self.center_x - self.width / 2
        start_y = self.center_y - self.width / 2
        step_size = self.width / (self.points_number - 1) # minus 1
        # Initialize
        for i in range(self.points_number):
            for j in range(self.points_number):
                self.matrix_X[i, j] = start_x + j * step_size
                self.matrix_Y[i, j] = start_y + j * step_size
                
        rotation = self.__create_rotation_matrix()
#         print(rotation)
        # Rotate an angle
        for i in range(self.points_number):
            for j in range(self.points_number):
                original = np.matrix([self.matrix_X[i, j], self.matrix_Y[i, j]])
#                 print(original[0])
#                 print(original[0,0])
#                 print(original[0,1])
                transformed = np.matmul(original, rotation)
#                 print(transformed)
                self.matrix_X[i, j] = transformed[0, 0]
                self.matrix_Y[i, j] = transformed[0, 1]
        
    def __create_rotation_matrix(self):
        theta = np.radians(self.angle)
        c, s = np.cos(theta), np.sin(theta)
        rotation = np.array(((c,-s), (s, c)))
        return rotation
    '''
    Index starts from 0
    '''
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