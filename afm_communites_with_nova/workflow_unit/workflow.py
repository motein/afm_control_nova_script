# -*- coding:UTF-8 -*-
'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from workflow_unit.controller import AFMController
from workflow_unit.excel import read_excel_file, validate_matrix
from tools.log import LogSystem
from tools.config import ConfigureFile

class Workflow:
    InProgress = False
    def __init__(self):
        self.logger = LogSystem.get_log("Workflow")
        self.conf = ConfigureFile.get_config()
        self.afm_controller =  AFMController()
        
        self.short_delay = self.conf.getfloat('GUI_DELAY_DEFAULT', 'ShortDelay')
        self.mid_delay = self.conf.getfloat('GUI_DELAY_DEFAULT', 'MiddleDelay')
        
        self.check_time_limit = self.conf.getint('EXPERIMENT_SETTINGS_DEFAULT', 'CheckTimesLimit')
        
        self.state_path = None
        self.state_file_name = self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'StateFileName')
        # Set-point Matrix
        self.enable_setpoint_matrix = self.conf.getboolean('EXPERIMENT_SETTINGS_DEFAULT', 'EnableSetpointMatrix')
        self.setpoint_matrix_file_path = None
        self.setpoint_matrix_sheet_name = None
        self.setpoint_matrix = None
        # Settling time
        self.settling_time_for_approach = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'SettlingTimeForApproach')
        self.settling_time_for_move = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'SettlingTimeForMove') 
        # Interval for checking state file
        self.state_check_interval = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'StateCheckInterval') # default 2s
        # Signal to trigger
        self.high_vol = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'HighVoltage')
        self.low_vol = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'LowVoltage')
        self.holding_time = self.conf.getfloat('EXPERIMENT_SETTINGS_DEFAULT', 'HoldingTime') # time of holding high voltage
    '''
    Start to do the experiment
    '''    
    def start_to_work(self, ui, position_callback, progress_callback):
        if self.check_experiment_conditions() == False:
            ui.com.speak_message.emit("Please prepare your experiment parameters.", "Error")
            time.sleep(self.mid_delay)
            print("Please prepare your experiment parameters.")
            self.logger.error("Please prepare your experiment parameters.")
            return
        
        print("Really started")
        self.logger.info("Really started")
        try:
            self.afm_controller.prepareAfmExperiment()
        except Exception as e:
            raise e
        points = self.afm_controller.getPoints()
        lines = self.afm_controller.getLines()
        
        if self.enable_setpoint_matrix == True:
            self.setpoint_matrix = read_excel_file(self.setpoint_matrix_file_path, self.setpoint_matrix_sheet_name)
            result, row_column = validate_matrix(self.setpoint_matrix, points, lines)
            if result == False:
                ui.com.speak_message.emit("Setpoint Matrix is not correct. Please check it.", "Error")
                time.sleep(self.mid_delay)
                print("Setpoint Matrix is not correct. Please check it.")
                self.logger.error("Setpoint Matrix is not correct. Row_Column->" + row_column)
                return
        file_path = self.state_path + '/' + self.state_file_name
        for i in range(lines):
            for j in range(points):
                
                if Workflow.InProgress == False: # Stop button pressed
                    return
                if position_callback != None:
                    position_callback("(" + str(j) +", " + str(i) + ")")
                    time.sleep(self.short_delay)
                self.logger.info("i=" + str(i) + ", j=" + str(j))
                print("i=" + str(i) + ", j=" + str(j))
                self.afm_controller.moveTip(j, i, self.settling_time_for_move)
                print("Move Tip")
                self.logger.info("Move Tip")
                if self.enable_setpoint_matrix == True:
                    self.afm_controller.doApproach(self.settling_time_for_approach, self.setpoint_matrix[i, j]) # self defined set-point
                else:
                    self.afm_controller.doApproach(self.settling_time_for_approach) # default set-point
                self.afm_controller.sendTriggerSingal(self.high_vol, self.low_vol, self.holding_time)
                acc_time = 0
                print("Approach")
                self.logger.info("Approach")
                while Workflow.InProgress == False and acc_time > self.check_time_limit and os.path.isfile(file_path) != True:
                    time.sleep(self.state_check_interval)
                    acc_time += 1
                progress_value = (i * points + j + 1) * 100.0 / (lines * points);
                print(progress_value)
                progress_callback(progress_value)
                time.sleep(self.short_delay)
                self.afm_controller.doWithdraw()
                print("Withdraw")
                self.logger.info("Withdraw")
    
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
        
    def get_state_file_name(self):
        return self.state_file_name
    
    def set_enable_setpoint_matrix(self, enable):
        self.enable_setpoint_matrix = enable
    
    def set_setpoint_matrix_file_path(self, path):
        self.setpoint_matrix_file_path = path
    
    def set_setpoint_matrix_sheet_name(self, sheet_name):
        self.setpoint_matrix_sheet_name = sheet_name
        
    def set_settling_time_for_approach(self, time_value):
        self.settling_time_for_approach = time_value
    
    def get_settling_time_for_approach(self):
        return self.settling_time_for_approach
    
    def set_settling_time_for_move(self, time_value):
        self.settling_time_for_move = time_value
    
    def get_settling_time_for_move(self):
        return self.settling_time_for_move
        
    def set_state_check_interval(self, interval):
        self.state_check_interval = interval
    
    def get_state_check_interval(self):
        return self.state_check_interval
        
    def set_high_voltage(self, high_vol):
        self.high_vol = high_vol
    
    def get_high_voltage(self):
        return self.high_vol
    
    def set_low_voltage(self, low_vol):
        self.low_vol = low_vol
        
    def get_low_voltage(self):
        return self.low_vol
    
    def set_holding_time(self, holding_time):
        self.holding_time = holding_time
    
    def get_holding_time(self):
        return self.holding_time