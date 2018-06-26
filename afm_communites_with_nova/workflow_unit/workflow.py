'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from workflow_unit.controller import AFMController
TIMES_LIMIT = 1

class Workflow:
    def __init__(self, state_path, matrix_type):
        self.afm_controller =  AFMController()
        self.state_path = state_path
        self.matrix_type = matrix_type
        self.setpoint_matrix = None
        self.enable_self_setpoint = False
        self.settling_time_for_approach = 1
        self.settling_time_for_move = 1
        self.check_interval = 2
        
    def start_to_work(self):
        if self.setpoint_matrix is not None:
            self.enable_self_setpoint = True
        
        self.afm_controller.prepareAfmExperiment()
        self.afm_controller.calcPositionMatrix(self.matrix_typ)
        num = self.afm_controller.getPointsNumber()
        for i in range(num):
            for j in range(num):
                print(i, j)
                fast, slow = self.afm_controller.getPositionbyIndex(i, j)
                self.afm_controller.moveTip(fast, slow)
                time.sleep(0.5) # settle
                if (self.enable_self_setpoint):
                    self.afm_controller.doApproach(self.setpoint_matrix[i, j]) # self defined setpoint
                else:
                    self.afm_controller.doApproach() # default setpoint
                time.sleep(self.settling_time_for_approach)
                self.afm_controller.sendTriggerSingal()
                acc_time = 0
                while acc_time > TIMES_LIMIT and os.path.isfile(self.state_path) is not True:
                    time.sleep(self.check_interval)
                    acc_time += 1
                
                self.afm_controller.doWithdraw()
        
        print("Done")