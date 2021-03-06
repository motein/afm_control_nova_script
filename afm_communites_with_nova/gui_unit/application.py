# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
from functools import partial
from gui_unit.common import PathWrapper, select_directory, select_file, show_message, check_file_suffix, Communicate, \
    speak_message, start_thread_func, stop_thread_func
    
from workflow_unit.workflow import Workflow
from tools.config import ConfigureFile

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(963, 598)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        brandingIcon = QtGui.QIcon()
        brandingIcon.addPixmap(QtGui.QPixmap("../resources/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(brandingIcon)
        '''Workflow region
        '''
        self.workflow = Workflow()
        self.conf = ConfigureFile.get_config()
        self.com = Communicate()
        self.com.speak_message.connect(speak_message)
        '''Experiment Settings region
        '''
        self.experimentSettingsGroupBox = QtGui.QGroupBox(Form)
        self.experimentSettingsGroupBox.setGeometry(QtCore.QRect(30, 0, 901, 491))
        self.experimentSettingsGroupBox.setStyleSheet("font: 75 14pt \"Corbel\";")
        self.experimentSettingsGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.experimentSettingsGroupBox.setObjectName("experimentSettingsGroupBox")
        '''State Path Settings
        '''
        self.stateGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.stateGroupBox.setGeometry(QtCore.QRect(30, 50, 391, 171))
        self.stateGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.stateGroupBox.setFlat(False)
        self.stateGroupBox.setCheckable(False)
        self.stateGroupBox.setObjectName("stateGroupBox")
        
        self.stateFolderLabel = QtGui.QLabel(self.stateGroupBox)
        self.stateFolderLabel.setGeometry(QtCore.QRect(40, 50, 61, 16))
        self.stateFolderLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.stateFolderLabel.setObjectName("stateFolderLabel")
        
        self.stateFolderLineEdit = QtGui.QLineEdit(self.stateGroupBox)
        self.stateFolderLineEdit.setGeometry(QtCore.QRect(110, 50, 151, 20))
        self.stateFolderLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.stateFolderLineEdit.setObjectName("stateFolderLineEdit")
        self.stateFolderLineEdit.setEnabled(False)
        
        self.selected_folder = PathWrapper("") # Store folder path info
        self.selectFolderButton = QtGui.QPushButton(self.stateGroupBox)
        self.selectFolderButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.selectFolderButton.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.selectFolderButton.clicked.connect(partial(select_directory, self.selected_folder, self.selected_folder_callback)) # Click event
        
        self.stateFileLabel = QtGui.QLabel(self.stateGroupBox)
        self.stateFileLabel.setGeometry(QtCore.QRect(40, 90, 90, 16))
        self.stateFileLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.stateFileLabel.setObjectName("stateFileLabel")
        
        self.stateFileLineEdit = QtGui.QLineEdit(self.stateGroupBox)
        self.stateFileLineEdit.setGeometry(QtCore.QRect(110, 90, 151, 20))
        self.stateFileLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.stateFileLineEdit.setObjectName("checkIntervalLineEdit")
        self.stateFileLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'StateFileName'))
        self.stateFileLineEdit.textChanged.connect(self.stateFileLineEditTextChanged)
        
        self.checkIntervalLabel = QtGui.QLabel(self.stateGroupBox)
        self.checkIntervalLabel.setGeometry(QtCore.QRect(6, 130, 90, 16))
        self.checkIntervalLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLabel.setObjectName("checkIntervalLabel")
        
        self.checkIntervalLineEdit = QtGui.QLineEdit(self.stateGroupBox)
        self.checkIntervalLineEdit.setGeometry(QtCore.QRect(110, 130, 151, 20))
        self.checkIntervalLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLineEdit.setObjectName("checkIntervalLineEdit")
        self.checkIntervalLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'StateCheckInterval'))
        self.checkIntervalLineEdit.textChanged.connect(self.checkIntervalLineEditTextChanged)
        '''Set-point Matrix Settings region
        '''
        self.setpointSettingsGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.setpointSettingsGroupBox.setGeometry(QtCore.QRect(30, 240, 391, 151))
        self.setpointSettingsGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.setpointSettingsGroupBox.setFlat(False)
        self.setpointSettingsGroupBox.setCheckable(False)
        self.setpointSettingsGroupBox.setObjectName("setpointSettingsGroupBox")

        self.enableMatrixSetpoingRadio = QtGui.QRadioButton(self.setpointSettingsGroupBox)
        self.enableMatrixSetpoingRadio.setEnabled(True)
        self.enableMatrixSetpoingRadio.setGeometry(QtCore.QRect(20, 40, 161, 16))
        self.enableMatrixSetpoingRadio.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.enableMatrixSetpoingRadio.setObjectName("enableMatrixSetpoingRadio")
        self.enableMatrixSetpoingRadio.setChecked(self.conf.getboolean('EXPERIMENT_SETTINGS_DEFAULT', 'EnableSetpointMatrix'))
        self.enableMatrixSetpoingRadio.toggled.connect(self.enableMatrixSetpoingChanged)
        
        self.filePathLabel = QtGui.QLabel(self.setpointSettingsGroupBox)
        self.filePathLabel.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.filePathLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.filePathLabel.setObjectName("filePathLabel")
        
        self.filePathLineEdit = QtGui.QLineEdit(self.setpointSettingsGroupBox)
        self.filePathLineEdit.setEnabled(False)
        self.filePathLineEdit.setGeometry(QtCore.QRect(110, 80, 151, 20))
        self.filePathLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        
        self.selected_file = PathWrapper("")
        self.selectFileButton = QtGui.QPushButton(self.setpointSettingsGroupBox)
        self.selectFileButton.setEnabled(False)
        self.selectFileButton.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.selectFileButton.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.selectFileButton.setObjectName("selectFileButton")
        self.selectFileButton.clicked.connect(partial(select_file, self.selected_file, self.selected_file_callback))
        
        self.sheetNameLabel = QtGui.QLabel(self.setpointSettingsGroupBox)
        self.sheetNameLabel.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.sheetNameLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.sheetNameLabel.setObjectName("sheetNameLabel")
        
        self.sheetNameLineEdit = QtGui.QLineEdit(self.setpointSettingsGroupBox)
        self.sheetNameLineEdit.setEnabled(False)
        self.sheetNameLineEdit.setGeometry(QtCore.QRect(110, 120, 151, 20))
        self.sheetNameLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.sheetNameLineEdit.setObjectName("sheetNameLineEdit")
        self.sheetNameLineEdit.textChanged.connect(self.sheetNameLineEditTextChanged)
        '''Position Info region
        '''        
        self.positionInfoGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.positionInfoGroupBox.setGeometry(QtCore.QRect(30, 400, 391, 61))
        self.positionInfoGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.positionInfoGroupBox.setObjectName("positionInfoGroupBox")
        self.positionInfoLabel = QtGui.QLabel(self.positionInfoGroupBox)
        self.positionInfoLabel.setGeometry(QtCore.QRect(160, 20, 151, 31))
        self.positionInfoLabel.setStyleSheet("font: 75 12pt \"Arial\"")
        self.positionInfoLabel.setObjectName("positionInfoLabel")
        '''Settling time region
        '''
        self.timeGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.timeGroupBox.setGeometry(QtCore.QRect(490, 50, 381, 131))
        self.timeGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.timeGroupBox.setObjectName("timeGroupBox")
        
        self.approachSettlingTime = QtGui.QLabel(self.timeGroupBox)
        self.approachSettlingTime.setGeometry(QtCore.QRect(40, 50, 131, 16))
        self.approachSettlingTime.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.approachSettlingTime.setObjectName("approachSettlingTime")
        
        self.approachTimeLineEdit = QtGui.QLineEdit(self.timeGroupBox)
        self.approachTimeLineEdit.setGeometry(QtCore.QRect(180, 50, 161, 20))
        self.approachTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.approachTimeLineEdit.setObjectName("approachTimeLineEdit")
        self.approachTimeLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'SettlingTimeForApproach'))
        self.approachTimeLineEdit.textChanged.connect(self.approachTimeLineEditTextChanged)

        self.moveSettlingTime = QtGui.QLabel(self.timeGroupBox)
        self.moveSettlingTime.setGeometry(QtCore.QRect(60, 90, 111, 16))
        self.moveSettlingTime.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveSettlingTime.setObjectName("moveSettlingTime")
        
        self.moveTimeLineEdit = QtGui.QLineEdit(self.timeGroupBox)
        self.moveTimeLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.moveTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveTimeLineEdit.setObjectName("moveTimeLineEdit")
        self.moveTimeLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'SettlingTimeForMove'))
        self.moveTimeLineEdit.textChanged.connect(self.moveTimeLineEditTextChanged)
        '''Trigger Signal Settings region
        '''
        self.triggerSettingsGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.triggerSettingsGroupBox.setGeometry(QtCore.QRect(490, 200, 381, 171))
        self.triggerSettingsGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.triggerSettingsGroupBox.setObjectName("triggerSettingsGroupBox")
        
        self.highVolLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.highVolLabel.setGeometry(QtCore.QRect(90, 50, 80, 16))
        self.highVolLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.highVolLabel.setObjectName("highVolLabel")
        
        self.highVolLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.highVolLineEdit.setGeometry(QtCore.QRect(180, 50, 161, 20))
        self.highVolLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.highVolLineEdit.setObjectName("highVolLineEdit")
        self.highVolLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'HighVoltage'))
        self.highVolLineEdit.textChanged.connect(self.highVolLineEditTextChanged)

        self.lowVolLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.lowVolLabel.setGeometry(QtCore.QRect(90, 90, 80, 16))
        self.lowVolLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLabel.setObjectName("lowVolLabel")
        
        self.lowVolLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.lowVolLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.lowVolLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLineEdit.setObjectName("lowVolLineEdit")
        self.lowVolLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'LowVoltage'))
        self.lowVolLineEdit.textChanged.connect(self.lowVolLineEditTextChanged)

        self.holdingTimeLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.holdingTimeLabel.setGeometry(QtCore.QRect(84, 130, 80, 16))
        self.holdingTimeLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLabel.setObjectName("holdingTimeLabel")
        
        self.holdingTimeLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.holdingTimeLineEdit.setGeometry(QtCore.QRect(180, 130, 161, 20))
        self.holdingTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLineEdit.setObjectName("holdingTimeLineEdit")
        self.holdingTimeLineEdit.setText(self.conf.get('EXPERIMENT_SETTINGS_DEFAULT', 'HoldingTime'))
        self.holdingTimeLineEdit.textChanged.connect(self.holdingTimeLineEditTextChanged)
        '''Progress region
        '''
        self.progressGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.progressGroupBox.setGeometry(QtCore.QRect(490, 390, 381, 71))
        self.progressGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.progressGroupBox.setObjectName("progressGroupBox")
        
        self.progressBar = QtGui.QProgressBar(self.progressGroupBox)
        self.progressBar.setGeometry(QtCore.QRect(40, 30, 341, 23))
        self.progressBar.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        '''Start/Stop experiment
        '''
        self.startExperimentButton = QtGui.QPushButton(Form)
        self.startExperimentButton.setGeometry(QtCore.QRect(150, 530, 301, 41))
        self.startExperimentButton.setCursor(QtCore.Qt.ArrowCursor)
        self.startExperimentButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.startExperimentButton.setObjectName("startExperimentButton")
        self.startExperimentButton.clicked.connect(partial(start_thread_func, self)) # Click event
        
        self.stopExperimentButton = QtGui.QPushButton(Form)
        self.stopExperimentButton.setGeometry(QtCore.QRect(530, 530, 301, 41))
        self.stopExperimentButton.setCursor(QtCore.Qt.ArrowCursor)
        self.stopExperimentButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.stopExperimentButton.setObjectName("stopExperimentButton")
        self.stopExperimentButton.setEnabled(False)
        self.stopExperimentButton.clicked.connect(stop_thread_func) # Click event

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Robot", None, QtGui.QApplication.UnicodeUTF8))
        '''Experiment Settings Region
        '''
        self.experimentSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Experiment Settings", None, QtGui.QApplication.UnicodeUTF8))
        '''State Path Settings
        '''
        self.stateGroupBox.setTitle(QtGui.QApplication.translate("Form", "State Path Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.stateFolderLabel.setText(QtGui.QApplication.translate("Form", "State Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectFolderButton.setText(QtGui.QApplication.translate("Form", "Select Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.stateFileLabel.setText(QtGui.QApplication.translate("Form", "State File:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkIntervalLabel.setText(QtGui.QApplication.translate("Form", "Check Interval(s):", None, QtGui.QApplication.UnicodeUTF8))
        '''Set-point Matrix Settings region
        '''
        self.setpointSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Setpoint Matrix Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.filePathLabel.setText(QtGui.QApplication.translate("Form", "Matrix File Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectFileButton.setText(QtGui.QApplication.translate("Form", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.enableMatrixSetpoingRadio.setText(QtGui.QApplication.translate("Form", "Enable Setpoint Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.sheetNameLabel.setText(QtGui.QApplication.translate("Form", "Sheet Name:", None, QtGui.QApplication.UnicodeUTF8))
        '''Position Info region
        '''
        self.positionInfoGroupBox.setTitle(QtGui.QApplication.translate("Form", "Position Info", None, QtGui.QApplication.UnicodeUTF8))
        '''Settling time region
        '''
        self.timeGroupBox.setTitle(QtGui.QApplication.translate("Form", "Settling Time Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.approachSettlingTime.setText(QtGui.QApplication.translate("Form", "Approach Settling Time(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.moveSettlingTime.setText(QtGui.QApplication.translate("Form", "Move Settling Time(s):", None, QtGui.QApplication.UnicodeUTF8))
        '''Trigger Signal Settings region
        '''
        self.triggerSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Trigger Signal Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.highVolLabel.setText(QtGui.QApplication.translate("Form", "High Voltage(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.lowVolLabel.setText(QtGui.QApplication.translate("Form", "Low Voltage(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.holdingTimeLabel.setText(QtGui.QApplication.translate("Form", "Holding Time(s):", None, QtGui.QApplication.UnicodeUTF8))
        '''Progress region
        '''
        self.progressGroupBox.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.progressGroupBox.setTitle(QtGui.QApplication.translate("Form", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Please be patient</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        '''Start/Stop experiment
        '''
        self.startExperimentButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Click me</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.startExperimentButton.setText(QtGui.QApplication.translate("Form", "Start Experiment", None, QtGui.QApplication.UnicodeUTF8))
        
        self.stopExperimentButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Click me</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.stopExperimentButton.setText(QtGui.QApplication.translate("Form", "Stop Experiment", None, QtGui.QApplication.UnicodeUTF8))
    '''
    Event region
    '''    
    def selected_folder_callback(self):
        if self.selected_folder is not None:
            self.stateFolderLineEdit.setText(self.selected_folder.value)
            self.workflow.set_state_path(self.selected_folder.value)
    
    def selected_file_callback(self):
        if self.selected_file is not None:
            if check_file_suffix(self.selected_file.value, '.xlsx') is False:
                show_message("The selected file is not a .xlsx one.", "Error")
            else:
                self.filePathLineEdit.setText(self.selected_file.value)

    def enableMatrixSetpoingChanged(self):
        enabled = self.enableMatrixSetpoingRadio.isChecked()
        if enabled is True:
            show_message("Self-defined Setpoint Matrix enabled.")
        else:
            show_message("Self-defined Setpoint Matrix disabled.")
        self.selectFileButton.setEnabled(enabled)
        self.sheetNameLineEdit.setEnabled(enabled)
    
    def stateFileLineEditTextChanged(self):
        state_file_name = self.stateFileLineEdit.text().strip()
        try:
            if state_file_name != "":
                self.workflow.set_state_file_name(state_file_name)
            else:
                show_message("Invalid input, and must be a non-empty string.", "Error")
                self.stateFileLineEdit.textChanged.disconnect(self.stateFileLineEditTextChanged)
                self.stateFileLineEdit.setText(self.workflow.get_state_file_name())
                self.stateFileLineEdit.textChanged.connect(self.stateFileLineEditTextChanged)
        except Exception:
            show_message("Invalid input, and must be a non-empty string.", "Error")
            self.stateFileLineEdit.textChanged.disconnect(self.stateFileLineEditTextChanged)
            self.stateFileLineEdit.setText(self.workflow.get_state_file_name())
            self.stateFileLineEdit.textChanged.connect(self.stateFileLineEditTextChanged)
    
    def checkIntervalLineEditTextChanged(self):
        interval = self.checkIntervalLineEdit.text().strip()
        try:
            interval = float(interval)
            if interval < 0:
                show_message("Invalid input, and must be no less than 0.", "Error")
            else:
                self.workflow.set_state_check_interval(interval)
            show_message(interval)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.checkIntervalLineEdit.textChanged.disconnect(self.checkIntervalLineEditTextChanged)
            self.checkIntervalLineEdit.setText(str(self.workflow.get_state_check_interval()))
            self.checkIntervalLineEdit.textChanged.connect(self.checkIntervalLineEditTextChanged)
    
    def sheetNameLineEditTextChanged(self):
        sheet_name = self.sheetNameLineEdit.text().strip()
        try:
            if sheet_name != "":
                self.workflow.set_setpoint_matrix_sheet_name(sheet_name)
            else:
                show_message("Invalid input, and must be a non-empty string.", "Error")
                self.sheetNameLineEdit.textChanged.disconnect(self.sheetNameLineEditTextChanged)
                self.sheetNameLineEdit.setText("")
                self.sheetNameLineEdit.textChanged.connect(self.sheetNameLineEditTextChanged)
        except Exception:
            show_message("Invalid input, and must be a non-empty string.", "Error")
            self.sheetNameLineEdit.textChanged.disconnect(self.sheetNameLineEditTextChanged)
            self.sheetNameLineEdit.setText("")
            self.sheetNameLineEdit.textChanged.connect(self.sheetNameLineEditTextChanged)

    def approachTimeLineEditTextChanged(self):
        time_value = self.approachTimeLineEdit.text().strip()
        try:
            time_value = float(time_value)
            if time_value < 0:
                show_message("Invalid input, and must be no less than 0.", "Error")
            else:
                self.workflow.set_settling_time_for_approach(time_value)
                show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.approachTimeLineEdit.textChanged.disconnect(self.approachTimeLineEditTextChanged)
            self.approachTimeLineEdit.setText(str(self.workflow.get_settling_time_for_approach()))
            self.approachTimeLineEdit.textChanged.connect(self.approachTimeLineEditTextChanged)
    
    def moveTimeLineEditTextChanged(self):
        time_value = self.moveTimeLineEdit.text().strip()
        try:
            time_value = float(time_value)
            if time_value < 0:
                show_message("Invalid input, and must be no less than 0.", "Error")
            else:
                self.workflow.set_settling_time_for_move(time_value)
                show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.moveTimeLineEdit.textChanged.disconnect(self.moveTimeLineEditTextChanged)
            self.moveTimeLineEdit.setText(str(self.workflow.get_settling_time_for_move()))
            self.moveTimeLineEdit.textChanged.connect(self.moveTimeLineEditTextChanged)
    
    def highVolLineEditTextChanged(self):
        voltage_value = self.highVolLineEdit.text().strip()
        if voltage_value == '-':
            return
        
        try:
            voltage_value = float(voltage_value)
            if voltage_value < -10:
                show_message("Clip value.")
                self.highVolLineEdit.setText("-10")
            elif voltage_value > 10:
                show_message("Clip value.")
                self.highVolLineEdit.setText("10")
            else:
                self.workflow.set_high_voltage(voltage_value)
                show_message(voltage_value)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.highVolLineEdit.textChanged.disconnect(self.highVolLineEditTextChanged)
            self.highVolLineEdit.setText(str(self.workflow.get_high_voltage()))
            self.highVolLineEdit.textChanged.connect(self.highVolLineEditTextChanged)
            
    def lowVolLineEditTextChanged(self):
        voltage_value = self.lowVolLineEdit.text().strip()
        if voltage_value == '-':
            return
        
        try:
            voltage_value = float(voltage_value)
            if voltage_value < -10:
                show_message("Clip value.")
                self.lowVolLineEdit.setText("-10")
            elif voltage_value > 10:
                show_message("Clip value.")
                self.lowVolLineEdit.setText("10")
            else:
                self.workflow.set_low_voltage(voltage_value)
                show_message(voltage_value)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.lowVolLineEdit.textChanged.disconnect(self.lowVolLineEditTextChanged)
            self.lowVolLineEdit.setText(str(self.workflow.get_low_voltage()))
            self.lowVolLineEdit.textChanged.connect(self.lowVolLineEditTextChanged)
            
    def holdingTimeLineEditTextChanged(self):
        time_value = self.holdingTimeLineEdit.text().strip()
        try:
            time_value = float(time_value)
            if time_value < 0:
                show_message("Invalid input, and must be no less than 0.", "Error")
            else:
                self.workflow.set_holding_time(time_value)
                show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float.", "Error")
            self.holdingTimeLineEdit.textChanged.disconnect(self.holdingTimeLineEditTextChanged)
            self.holdingTimeLineEdit.setText(str(self.workflow.get_holding_time()))
            self.holdingTimeLineEdit.textChanged.connect(self.holdingTimeLineEditTextChanged)

    def setPositionInfoLabelText(self, content):
        self.positionInfoLabel.setText(content)
        QtGui.QApplication.processEvents()
        
    def updateProgress(self, value):
        self.progressBar.setProperty("value", value)
        QtGui.QApplication.processEvents()
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(stop_thread_func)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
