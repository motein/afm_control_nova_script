# -*- coding:UTF-8 -*-
'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from workflow_unit.controller import AFMController
from workflow_unit.excel import read_excel_file, validate_matrix
from gui_unit.common import show_message
from tools.log import LogSystem
TIMES_LIMIT = 1

class Workflow:
    def __init__(self):
        self.logger = LogSystem.get_log("Workflow")
        self.inProgress = False
        self.afm_controller =  AFMController()
        self.state_path = None
        self.state_file_name = "state_fin"
        # Position Matrix
        self.position_matrix_type = None
        # Set-point Matrix
        self.enable_setpoint_matrix = False
        self.setpoint_matrix_file_path = None
        self.setpoint_matrix_sheet_name = None
        self.setpoint_matrix = None
        # Settling time
        self.settling_time_for_approach = None
        self.settling_time_for_move = None
        # Interval for checking state file
        self.state_check_interval = None
        # Signal to trigger
        self.high_vol = None
        self.low_vol = None
        self.holding_time = None # time of holding high voltage
    '''
    Start to do the experiment
    '''    
    def start_to_work(self, call_back):
        if self.check_experiment_conditions() == False:
            show_message("Please prepare your experiment parameters.", "Error")
            return
            
        self.afm_controller.prepareAfmExperiment()
        points = self.afm_controller.getPoints()
        lines = self.afm_controller.getLines()
        
        if self.enable_setpoint_matrix == True:
            self.setpoint_matrix = read_excel_file(self.setpoint_matrix_file_path, self.setpoint_matrix_sheet_name)
            result, row_column = validate_matrix(self.setpoint_matrix, points, lines)
            if result == False:
                show_message("Setpoint Matrix is not correct. Please check it.", "Error")
                self.logger.error("Row_Column->" + row_column)
                return
        file_path = self.state_path + '/' + self.state_file_name
        for i in range(lines):
            for j in range(points):
                
                if self.inProgress == False: # Stop button pressed
                    return
                
                call_back("(" + j +", " + i + ")")
                self.logger("i=" + i + ", j=" + j)
                self.afm_controller.moveTip(j, i, self.settling_time_for_move)
                if self.enable_setpoint_matrix == True:
                    self.afm_controller.doApproach(self.settling_time_for_approach, self.setpoint_matrix[i, j]) # self defined set-point
                else:
                    self.afm_controller.doApproach(self.settling_time_for_approach) # default set-point
                self.afm_controller.sendTriggerSingal(self.high_vol, self.low_vol, self.holding_time)
                acc_time = 0
                while self.inProgress == False and acc_time > TIMES_LIMIT and os.path.isfile(file_path) != True:
                    time.sleep(self.state_check_interval)
                    acc_time += 1
                
                self.afm_controller.doWithdraw()
    
    def check_experiment_conditions(self):
        if self.state_path == None or self.state_check_interval == None:
            return False
        
        if self.enable_setpoint_matrix == True:
            if self.setpoint_matrix_file_path == None or self.setpoint_matrix_sheet_name == None:
                return False
                
        if self.settling_time_for_approach == None or self.settling_time_for_move == None:
            return False
        
        if self.high_vol == None or self.low_vol == None or self.holding_time == None:
            return False
            
        return True
        
    '''
    Prepare experiments. Set functions
    '''
    def set_state_path(self, state_path):
        self.state_path = state_path
    
    def set_state_file_name(self, state_file_name):
        self.state_file_name = state_file_name
    
    def set_enable_setpoint_matrix(self, enable):
        self.enable_setpoint_matrix = enable
    
    def set_setpoint_matrix_file_path(self, path):
        self.setpoint_matrix_file_path = path
    
    def set_setpoint_matrix_sheet_name(self, sheet_name):
        self.setpoint_matrix_sheet_name = sheet_name
        
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
    
    def set_inProgress(self, value):
        self.inProgress = value
    
    def get_inProgress(self):
        return self.inProgress
    