# -*- coding:UTF-8 -*-
'''
Created on Jun 23, 2018

@author: xiongan2
'''
import sys
import picoscript
import time
import numpy as np
from enum import Enum
from tools.log import LogSystem
    
class AFMController:
    def __init__(self):
        self.logger = LogSystem.get_log("AFMController")
        self.points = None
        self.lines = None
        self.setpoint = None
        
    def prepareAfmExperiment(self):
        self.points = picoscript.GetScanXPixels()
        self.lines = picoscript.GetScanYPixels()
        self.setpoint = picoscript.GetServoSetpoint()
    
    def doApproach(self, settling_time, setpoint = None):
        if setpoint is not None:
            picoscript.SetServoSetpoint(setpoint)
            
        picoscript.MotorApproach()
        picoscript.WaitForStatusApproachState(1)
        time.sleep(settling_time)
    
    def doWithdraw(self):
        picoscript.MotorWithdraw(self)
    
    def moveTip(self, fast, slow, settling_time):
        picoscript.SetTipPosition(fast, slow)
        time.sleep(settling_time)
    
    def sendTriggerSingal(self, high_vol, low_vol, holding_time):
        picoscript.SetOutputAux1(high_vol) # Trigger a signal
        time.sleep(holding_time)
        picoscript.SetOutputAux1(low_vol)
        
    def getPoints(self):
        return self.points
    
    def getLines(self):
        return self.lines