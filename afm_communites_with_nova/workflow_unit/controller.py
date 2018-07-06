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
        self.approach_status_delay = self.conf.getfloat('STATUS_DELAY_DEFAULT', 'ApproachStatusDelay')
        self.move_status_delay = self.conf.getfloat('STATUS_DELAY_DEFAULT', 'MoveStatusDelay')
        self.aux_output = self.conf.getint('EXPERIMENT_SETTINGS_DEFAULT', 'AuxOutput')
        
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
        if self.aux_output == 1:
            self.logger.info("Aux Output 1.")
            picoscript.SetOutputAux1(high_vol) # Trigger a signal
            time.sleep(holding_time)
            picoscript.SetOutputAux1(low_vol)
        elif self.aux_output == 2:
            self.logger.info("Aux Output 2.")
            picoscript.SetOutputAux2(high_vol) # Trigger a signal
            time.sleep(holding_time)
            picoscript.SetOutputAux2(low_vol)
        else:
            self.logger.info("Aux Output 1.")
            picoscript.SetOutputAux1(high_vol) # Trigger a signal
            time.sleep(holding_time)
            picoscript.SetOutputAux1(low_vol)
        
    def getPoints(self):
        return self.points
    
    def getLines(self):
        return self.lines