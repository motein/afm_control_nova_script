'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from workflow_unit.controller import AFMController
TIMES_LIMIT = 1

class Workflow:
    def __init__(self):
        self.afm_controller =  AFMController()
        self.state_path = None
        # Position Matrix
        self.position_matrix_type = None
        # Set-point Matrix
        self.enable_setpoint_matrix = False
        self.setpoint_matrix_file_path = None
        self.setpoint_matrix = None
        # Settling time
        self.settling_time_for_approach = 1
        self.settling_time_for_move = 1
        # Interval for checking state file
        self.state_check_interval = 2
        # Signal to trigger
        self.high_vol = 5
        self.low_vol = 0
        self.holding_time = 1 # time of holding high voltage
        
    def start_to_work(self):
        self.afm_controller.prepareAfmExperiment()
        self.afm_controller.calcPositionMatrix(self.position_matrix_type)
        num = self.afm_controller.getPointsNumber()
        for i in range(num):
            for j in range(num):
                print(i, j)
                fast, slow = self.afm_controller.getPositionbyIndex(i, j)
                self.afm_controller.moveTip(fast, slow)
                time.sleep(self.settling_time_for_move) # settle
                if (self.enable_setpoint_matrix):
                    self.afm_controller.doApproach(self.setpoint_matrix[i, j]) # self defined set-point
                else:
                    self.afm_controller.doApproach() # default set-point
                time.sleep(self.settling_time_for_approach)
                self.afm_controller.sendTriggerSingal()
                acc_time = 0
                while acc_time > TIMES_LIMIT and os.path.isfile(self.state_path) is not True:
                    time.sleep(self.state_check_interval)
                    acc_time += 1
                
                self.afm_controller.doWithdraw()
        
        print("Done")
        
    def set_state_path(self, state_path):
        self.state_path = state_path
    
    def set_position_matrix_type(self, matrix_type):
        self.position_matrix_type = matrix_type
    
    def set_enable_setpoint_matrix(self, enable):
        self.enable_setpoint_matrix = enable
    
    def set_setpoint_matrix_file_path(self, path):
        self.setpoint_matrix_file_path = path
        
    def set_settling_time_for_approach(self, time_value):
        self.settling_time_for_approach = time_value
    
    def set_settling_time_for_move(self, time_value):
        self.settling_time_for_move = time_value
        
    def set_state_check_interval(self, interval):
        self.state_check_interval = interval
        
    def set_high_voltage(self, high_vol):
        self.high_vol = high_vol
    
    def set_low_voltage(self, low_vol):
        self.low_vol = low_vol
    
    def set_holding_time(self, holding_time):
        self.holding_time = holding_time
    