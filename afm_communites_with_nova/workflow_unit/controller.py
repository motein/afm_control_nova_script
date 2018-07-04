# -*- coding:UTF-8 -*-
'''
Created on Jun 23, 2018

@author: xiongan2
'''
import picoscript
import time
from tools.log import LogSystem
from tools.config import ConfigureFile
    
class AFMController:
    def __init__(self):
        self.logger = LogSystem.get_log("AFMController")
        self.conf = ConfigureFile.get_config()
        self.points = None
        self.lines = None
        self.setpoint = None
        self.approach_status_delay = 3
        self.move_status_delay = 3
        
    def prepareAfmExperiment(self):
        self.points = picoscript.GetScanXPixels()
        self.lines = picoscript.GetScanYPixels()
        self.setpoint = picoscript.GetServoSetpoint()
    
    def doApproach(self, settling_time, setpoint = None):
        if setpoint is not None:
            picoscript.SetServoSetpoint(setpoint)
            
        picoscript.MotorApproach()
        time.sleep(self.approach_status_delay)
        picoscript.WaitForStatusApproachState(0)
        time.sleep(settling_time)
    
    def doWithdraw(self):
        picoscript.MotorWithdraw()
    
    def moveTip(self, fast, slow, settling_time):
        picoscript.SetTipPosition(fast, slow)
        time.sleep(self.move_status_delay)
        picoscript.WaitForStatusTipMoving(0)
        time.sleep(settling_time)
    
    def sendTriggerSingal(self, high_vol, low_vol, holding_time):
        picoscript.SetOutputAux1(high_vol) # Trigger a signal
        time.sleep(holding_time)
        picoscript.SetOutputAux1(low_vol)
        
    def getPoints(self):
        return self.points
    
    def getLines(self):
        return self.lines