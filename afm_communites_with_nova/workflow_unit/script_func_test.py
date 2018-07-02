'''
Created on Jul 2, 2018

@author: xiongan2
'''
import picoscript

def main():
        picoscript.DisplayMessage("Hello")
        setpoint = picoscript.GetServoSetpoint()
        print("Setpoint", setpoint)
        angle = picoscript.GetScanAngle()
        print("Angle", angle)
        width = picoscript.GetScanSize()
        print("Width", width)
        center_x = picoscript.GetScanXOffset()
        print("Offset X", center_x)
        picoscript.SetScanXOffset(1.30000004245e-06)
        center_y = picoscript.GetScanYOffset()
        print("Offset Y", center_y)
        aux1 = picoscript.SetOutputAux1(-1)
        print("Aux 1", aux1)
        #picoscript.MotorApproach()
        #picoscript.WaitForStatusApproachState(1)
        #picoscript.MotorWithdraw()
        picoscript.SetTipPosition(1,1)
        picoscript.WaitForStatusTipMoving(1)
        #picoscript.MotorZeroPosition()
if __name__ == '__main__':
    print("Start")
    main()
    print("End")
    