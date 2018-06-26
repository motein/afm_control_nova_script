'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from workflow_unit.controller import AFMController
TIME_LIMIT = 1

def main():
    controller = AFMController()
    controller.prepareAfmExperiment()
    controller.calcPositionMatrix()
    num = controller.getPointsNumber()
    for i in range(num):
        for j in range(num):
            print(i, j)
            fast, slow = controller.getPositionbyIndex(i, j)
            controller.moveTip(fast, slow)
            time.sleep(0.5) # settle
            controller.doApproach()
            time.sleep(0.5)
            controller.sendTriggerSingal()
            time.sleep(0.5)
            acc_time = 0
            while acc_time > TIME_LIMIT and os.path.isfile('state_fin') is not True:
                time.sleep(1)
                acc_time += 1
            
            controller.doWithdraw()
        
    print('Finished')


if __name__ == '__main__':  
    main()