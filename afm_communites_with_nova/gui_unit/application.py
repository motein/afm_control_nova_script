# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot.ui'
#
# Created: Fri Jun 29 11:30:27 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(963, 598)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        brandingIcon = QtGui.QIcon()
        brandingIcon.addPixmap(QtGui.QPixmap("../resources/branding.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(brandingIcon)
        '''Experiment Settings Region
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
        
        self.selectFolderButton = QtGui.QPushButton(self.stateGroupBox)
        self.selectFolderButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.selectFolderButton.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.selectFolderButton.setObjectName("selectFolderButton")
        
        self.checkIntervalLabel = QtGui.QLabel(self.stateGroupBox)
        self.checkIntervalLabel.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.checkIntervalLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLabel.setObjectName("checkIntervalLabel")
        
        self.checkIntervalLineEdit = QtGui.QLineEdit(self.stateGroupBox)
        self.checkIntervalLineEdit.setGeometry(QtCore.QRect(110, 90, 151, 20))
        self.checkIntervalLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.checkIntervalLineEdit.setObjectName("checkIntervalLineEdit")
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
        
        self.filePathLabel = QtGui.QLabel(self.setpointSettingsGroupBox)
        self.filePathLabel.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.filePathLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.filePathLabel.setObjectName("filePathLabel")
        
        self.filePathLineEdit = QtGui.QLineEdit(self.setpointSettingsGroupBox)
        self.filePathLineEdit.setEnabled(False)
        self.filePathLineEdit.setGeometry(QtCore.QRect(110, 80, 151, 20))
        self.filePathLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        
        self.selectFileButton = QtGui.QPushButton(self.setpointSettingsGroupBox)
        self.selectFileButton.setEnabled(False)
        self.selectFileButton.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.selectFileButton.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.selectFileButton.setObjectName("selectFileButton")
        
        self.sheetNameLabel = QtGui.QLabel(self.setpointSettingsGroupBox)
        self.sheetNameLabel.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.sheetNameLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.sheetNameLabel.setObjectName("sheetNameLabel")
        
        self.sheetNameLineEdit = QtGui.QLineEdit(self.setpointSettingsGroupBox)
        self.sheetNameLineEdit.setEnabled(False)
        self.sheetNameLineEdit.setGeometry(QtCore.QRect(110, 120, 151, 20))
        self.sheetNameLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.sheetNameLineEdit.setObjectName("sheetNameLineEdit")
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

        self.moveSettlingTime = QtGui.QLabel(self.timeGroupBox)
        self.moveSettlingTime.setGeometry(QtCore.QRect(60, 90, 111, 16))
        self.moveSettlingTime.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveSettlingTime.setObjectName("moveSettlingTime")
        
        self.moveTimeLineEdit = QtGui.QLineEdit(self.timeGroupBox)
        self.moveTimeLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.moveTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.moveTimeLineEdit.setObjectName("moveTimeLineEdit")
        '''Trigger Signal Settings region
        '''
        self.triggerSettingsGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.triggerSettingsGroupBox.setGeometry(QtCore.QRect(490, 200, 381, 171))
        self.triggerSettingsGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.triggerSettingsGroupBox.setObjectName("triggerSettingsGroupBox")
        
        self.highVolLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.highVolLabel.setGeometry(QtCore.QRect(90, 50, 71, 16))
        self.highVolLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.highVolLabel.setObjectName("highVolLabel")
        
        self.highVolLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.highVolLineEdit.setGeometry(QtCore.QRect(180, 50, 161, 20))
        self.highVolLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.highVolLineEdit.setObjectName("highVolLineEdit")

        self.lowVolLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.lowVolLabel.setGeometry(QtCore.QRect(90, 90, 71, 16))
        self.lowVolLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLabel.setObjectName("lowVolLabel")
        
        self.lowVolLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.lowVolLineEdit.setGeometry(QtCore.QRect(180, 90, 161, 20))
        self.lowVolLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.lowVolLineEdit.setObjectName("lowVolLineEdit")

        self.holdingTimeLabel = QtGui.QLabel(self.triggerSettingsGroupBox)
        self.holdingTimeLabel.setGeometry(QtCore.QRect(90, 130, 71, 16))
        self.holdingTimeLabel.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLabel.setObjectName("holdingTimeLabel")
        
        self.holdingTimeLineEdit = QtGui.QLineEdit(self.triggerSettingsGroupBox)
        self.holdingTimeLineEdit.setGeometry(QtCore.QRect(180, 130, 161, 20))
        self.holdingTimeLineEdit.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.holdingTimeLineEdit.setObjectName("holdingTimeLineEdit")
        '''Progress region
        '''
        self.progressGroupBox = QtGui.QGroupBox(self.experimentSettingsGroupBox)
        self.progressGroupBox.setGeometry(QtCore.QRect(490, 390, 381, 71))
        self.progressGroupBox.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.progressGroupBox.setObjectName("progressGroupBox")
        
        self.progressBar = QtGui.QProgressBar(self.progressGroupBox)
        self.progressBar.setGeometry(QtCore.QRect(40, 30, 341, 23))
        self.progressBar.setStyleSheet("font: 8pt \"Times New Roman\";")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        
        self.startExperimentButton = QtGui.QPushButton(Form)
        self.startExperimentButton.setGeometry(QtCore.QRect(330, 530, 301, 41))
        self.startExperimentButton.setCursor(QtCore.Qt.ArrowCursor)
        self.startExperimentButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.startExperimentButton.setObjectName("startExperimentButton")

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
        self.checkIntervalLabel.setText(QtGui.QApplication.translate("Form", "Check Interval:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.approachSettlingTime.setText(QtGui.QApplication.translate("Form", "Approach Settling Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.moveSettlingTime.setText(QtGui.QApplication.translate("Form", "Move Settling Time:", None, QtGui.QApplication.UnicodeUTF8))
        '''Trigger Signal Settings region
        '''
        self.triggerSettingsGroupBox.setTitle(QtGui.QApplication.translate("Form", "Trigger Signal Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.highVolLabel.setText(QtGui.QApplication.translate("Form", "High Voltage:", None, QtGui.QApplication.UnicodeUTF8))
        self.lowVolLabel.setText(QtGui.QApplication.translate("Form", "Low Voltage:", None, QtGui.QApplication.UnicodeUTF8))
        self.holdingTimeLabel.setText(QtGui.QApplication.translate("Form", "Holding Time:", None, QtGui.QApplication.UnicodeUTF8))
        '''Progress region
        '''
        self.progressGroupBox.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.progressGroupBox.setTitle(QtGui.QApplication.translate("Form", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Please be patient</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        '''Start experiment
        '''
        self.startExperimentButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Click me</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.startExperimentButton.setText(QtGui.QApplication.translate("Form", "Start Experiment", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

