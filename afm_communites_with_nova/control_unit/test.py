'''
Created on Jun 23, 2018

@author: xiongan2
'''
import time
import os
from control_unit.commands import prepareAfmExperiment, calcPositionMatrix,\
    moveTip, getPositionbyIndex, doApproach, sendTriggerSingal, doWithdraw

TIME_LIMIT = 1

def main():
    prepareAfmExperiment()
    matrix = calcPositionMatrix()
    for index in range(1, 10):
        print(index)
        pos = getPositionbyIndex(index)
        moveTip(pos[0], pos[1])
        time.sleep(0.5) # settle
        doApproach()
        time.sleep(0.5)
        sendTriggerSingal()
        time.sleep(0.5)
        acc_time = 0
        while acc_time > TIME_LIMIT and os.path.isfile('state_fin') is not True:
            time.sleep(1)
            acc_time += 1
        
        doWithdraw()
        
    print('Finished')


if __name__ == '__main__':  
    main()