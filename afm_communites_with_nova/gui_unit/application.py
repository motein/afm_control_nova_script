# -*- coding: utf-8 -*-
import time
from PySide import QtCore, QtGui
from functools import partial
from gui_unit.common import PathWrapper, select_directory, select_file, show_message
from workflow_unit.workflow import Workflow
from workflow_unit.controller import Matrix_Type

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
        self.stateGroupBox.setGeometry(QtCore.QRect(30, 50, 391, 131))
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
        
        self.selected_folder = PathWrapper("") # Store folder path info
        self.selectFolderButton = QtGui.QPushButton(self.stateGroupBox)
        self.selectFolderButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.selectFolderButton.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.selectFolderButton.clicked.connect(partial(select_directory, self.selected_folder, self.selected_folder_callback)) # Click event
        
        self.checkIntervalLabel = QtGui.QLabel(self.stateGroupBox)
        self.checkIntervalLabel.setGeometry(QtCore.QRect(6, 90, 90, 16))
        self.checkIntervalLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLabel.setObjectName("checkIntervalLabel")
        
        self.checkIntervalLineEdit = QtGui.QLineEdit(self.stateGroupBox)
        self.checkIntervalLineEdit.setGeometry(QtCore.QRect(110, 90, 151, 20))
        self.checkIntervalLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLineEdit.setObjectName("checkIntervalLineEdit")
        self.checkIntervalLineEdit.textChanged.connect(self.checkIntervalLineEditTextChanged)
        '''Position Matrix Type Settings region
        '''
        self.positionSettingsGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.positionSettingsGroupBox.setGeometry(QtCore.QRect(30, 200, 391, 81))
        self.positionSettingsGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.positionSettingsGroupBox.setFlat(False)
        self.positionSettingsGroupBox.setCheckable(False)
        self.positionSettingsGroupBox.setObjectName("positionSettingsGroupBox")
        
        self.matrixTypeLabel = QtGui.QLabel(self.positionSettingsGroupBox)
        self.matrixTypeLabel.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.matrixTypeLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.matrixTypeLabel.setObjectName("matrixTypeLabel")
        
        self.matrixTypeCombo = QtGui.QComboBox(self.positionSettingsGroupBox)
        self.matrixTypeCombo.setGeometry(QtCore.QRect(110, 40, 151, 22))
        self.matrixTypeCombo.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.matrixTypeCombo.setObjectName("matrixTypeCombo")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.addItem("")
        self.matrixTypeCombo.currentIndexChanged.connect(self.matrixTypeChanged)
        '''Set-point Matrix Settings region
        '''
        self.setpointSettingsGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.setpointSettingsGroupBox.setGeometry(QtCore.QRect(30, 310, 391, 151))
        self.setpointSettingsGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.setpointSettingsGroupBox.setFlat(False)
        self.setpointSettingsGroupBox.setCheckable(False)
        self.setpointSettingsGroupBox.setObjectName("setpointSettingsGroupBox")

        self.enableMatrixSetpoingRadio = QtGui.QRadioButton(self.setpointSettingsGroupBox)
        self.enableMatrixSetpoingRadio.setEnabled(True)
        self.enableMatrixSetpoingRadio.setGeometry(QtCore.QRect(20, 40, 161, 16))
        self.enableMatrixSetpoingRadio.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.enableMatrixSetpoingRadio.setObjectName("enableMatrixSetpoingRadio")
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
        self.approachTimeLineEdit.textChanged.connect(self.approachTimeLineEditTextChanged)

        self.moveSettlingTime = QtGui.QLabel(self.timeGroupBox)
        self.moveSettlingTime.setGeometry(QtCore.QRect(60, 90, 111, 16))
        self.moveSettlingTime.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveSettlingTime.setObjectName("moveSettlingTime")
        
        self.moveTimeLineEdit = QtGui.QLineEdit(self.timeGroupBox)
        self.moveTimeLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.moveTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveTimeLineEdit.setObjectName("moveTimeLineEdit")
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
        self.highVolLineEdit.textChanged.connect(self.highVolLineEditTextChanged)

        self.lowVolLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.lowVolLabel.setGeometry(QtCore.QRect(90, 90, 80, 16))
        self.lowVolLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLabel.setObjectName("lowVolLabel")
        
        self.lowVolLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.lowVolLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.lowVolLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLineEdit.setObjectName("lowVolLineEdit")
        self.lowVolLineEdit.textChanged.connect(self.lowVolLineEditTextChanged)

        self.holdingTimeLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.holdingTimeLabel.setGeometry(QtCore.QRect(84, 130, 80, 16))
        self.holdingTimeLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLabel.setObjectName("holdingTimeLabel")
        
        self.holdingTimeLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.holdingTimeLineEdit.setGeometry(QtCore.QRect(180, 130, 161, 20))
        self.holdingTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLineEdit.setObjectName("holdingTimeLineEdit")
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
        self.startExperimentButton.clicked.connect(self.startExperimentButtonClicked) # Click event
        
        self.stopExperimentButton = QtGui.QPushButton(Form)
        self.stopExperimentButton.setGeometry(QtCore.QRect(530, 530, 301, 41))
        self.stopExperimentButton.setCursor(QtCore.Qt.ArrowCursor)
        self.stopExperimentButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.stopExperimentButton.setObjectName("stopExperimentButton")
        self.stopExperimentButton.setEnabled(False)
        self.stopExperimentButton.clicked.connect(self.stopExperimentButtonClicked) # Click event

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
        self.checkIntervalLabel.setText(QtGui.QApplication.translate("Form", "Check Interval(s):", None, QtGui.QApplication.UnicodeUTF8))
        '''Position Matrix Type Settings region
        '''
        self.positionSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Position Matrix Type Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeLabel.setText(QtGui.QApplication.translate("Form", "Matrix Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(0, QtGui.QApplication.translate("Form", "    8 × 8", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(1, QtGui.QApplication.translate("Form", "  16 × 16", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(2, QtGui.QApplication.translate("Form", "  32 × 32", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(3, QtGui.QApplication.translate("Form", "  64 × 64", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(4, QtGui.QApplication.translate("Form", "128 × 128", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(5, QtGui.QApplication.translate("Form", "256 × 256", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixTypeCombo.setItemText(6, QtGui.QApplication.translate("Form", "512 × 512", None, QtGui.QApplication.UnicodeUTF8))
        '''Set-point Matrix Settings region
        '''
        self.setpointSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Setpoint Matrix Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.filePathLabel.setText(QtGui.QApplication.translate("Form", "Matrix File Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectFileButton.setText(QtGui.QApplication.translate("Form", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.enableMatrixSetpoingRadio.setText(QtGui.QApplication.translate("Form", "Enable Setpoint Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.sheetNameLabel.setText(QtGui.QApplication.translate("Form", "Sheet Name:", None, QtGui.QApplication.UnicodeUTF8))
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
    
    def selected_file_callback(self):
        if self.selected_folder is not None:
            self.filePathLineEdit.setText(self.selected_file.value)

    def enableMatrixSetpoingChanged(self):
        enabled = self.enableMatrixSetpoingRadio.isChecked()
        show_message(enabled)
        self.filePathLineEdit.setEnabled(enabled)
        self.selectFileButton.setEnabled(enabled)
        self.sheetNameLineEdit.setEnabled(enabled)

    def matrixTypeChanged(self):
        index = self.matrixTypeCombo.currentIndex() # Index from 0
        if index == 0:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_8_8)
        elif index == 1:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_16_16)
        elif index == 2:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_32_32)
        elif index == 3:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_64_64)
        elif index == 4:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_128_128)
        elif index == 5:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_256_256)
        elif index == 6:
            self.workflow.set_position_matrix_type(Matrix_Type.MATRIX_512_512)
            
        show_message(index)
    
    def checkIntervalLineEditTextChanged(self):
        interval = self.checkIntervalLineEdit.text()
        try:
            if interval != "":
                interval = float(interval)
                if interval < 0:
                    show_message("Invalid input, and must be no less than 0", "Error:")
                else:
                    self.workflow.set_state_check_interval(interval)
                show_message(interval)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.checkIntervalLineEdit.setText("")
    
    def sheetNameLineEditTextChanged(self):
        sheet_name = self.sheetNameLineEdit.text()
        try:
            if sheet_name != "":
                self.workflow.set_setpoint_matrix_sheet_name(sheet_name)
                show_message(sheet_name)
        except Exception as e:
            show_message(e.message, "Error:")
            self.sheetNameLineEdit.setText("")

    def approachTimeLineEditTextChanged(self):
        time_value = self.approachTimeLineEdit.text()
        try:
            if time_value != "":
                time_value = float(time_value)
                if time_value < 0:
                    show_message("Invalid input, and must be no less than 0", "Error:")
                else:
                    self.workflow.set_settling_time_for_approach(time_value)
                    show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.approachTimeLineEdit.setText("")
    
    def moveTimeLineEditTextChanged(self):
        time_value = self.moveTimeLineEdit.text()
        try:
            if time_value != "":
                time_value = float(time_value)
                if time_value < 0:
                    show_message("Invalid input, and must be no less than 0", "Error:")
                else:
                    self.workflow.set_settling_time_for_move(time_value)
                    show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.moveTimeLineEdit.setText("")
    
    def highVolLineEditTextChanged(self):
        voltage_value = self.highVolLineEdit.text()
        if voltage_value == '-':
            return
        
        try:
            if voltage_value != "":
                voltage_value = float(voltage_value)
                if voltage_value < -10:
                    show_message("Clip value", "")
                    self.highVolLineEdit.setText("-10")
                elif voltage_value > 10:
                    show_message("Clip value", "")
                    self.highVolLineEdit.setText("10")
                else:
                    self.workflow.set_high_voltage(voltage_value)
                    show_message(voltage_value)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.highVolLineEdit.setText("")
            
    def lowVolLineEditTextChanged(self):
        voltage_value = self.lowVolLineEdit.text()
        if voltage_value == '-':
            return
        
        try:
            if voltage_value != "":
                voltage_value = float(voltage_value)
                if voltage_value < -10:
                    show_message("Clip value", "")
                    self.lowVolLineEdit.setText("-10")
                elif voltage_value > 10:
                    show_message("Clip value", "")
                    self.lowVolLineEdit.setText("10")
                else:
                    self.workflow.set_low_voltage(voltage_value)
                    show_message(voltage_value)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.lowVolLineEdit.setText("")
            
    def holdingTimeLineEditTextChanged(self):
        time_value = self.holdingTimeLineEdit.text()
        try:
            if time_value != "":
                time_value = float(time_value)
                if time_value < 0:
                    show_message("Invalid input, and must be no less than 0", "Error:")
                else:
                    self.workflow.set_holding_time(time_value)
                    show_message(time_value)
        except Exception:
            show_message("Invalid input, and must be a float", "Error:")
            self.holdingTimeLineEdit.setText("")
    
    def startExperimentButtonClicked(self):
        if self.workflow.get_inProgress() == True:
            return
        
        self.workflow.set_inProgress(True)
        self.startExperimentButton.setEnabled(False)
        self.stopExperimentButton.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        
        try:
            show_message("Experiment started", "")
            time.sleep(3)
#             self.workflow.start_to_work()
        finally:
            self.progressBar.setProperty("value", 100)
            self.workflow.set_inProgress(False)
            self.stopExperimentButton.setEnabled(False)
            self.startExperimentButton.setEnabled(True)
    
    def stopExperimentButtonClicked(self):
        if self.workflow.get_inProgress() == True:
            self.workflow.set_inProgress(False)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

