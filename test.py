# from __future__ import print_function
from textstat.textstat import textstat
import time


if __name__ == '__main__':
        with open('./Data/chesterton-ball.txt', 'r') as myfile:
         data=myfile.read().replace('\n', '')
        TS = textstat
        
        print("Serial FOG index")
        
        t2=time.clock()
        print(TS.gunning_fog(data ))
        t3=time.clock()        
        
        print("Time : " , (t3-t2))
        print("\nParallel FOG index")
        
        t0=time.clock()
        print(TS.gunning_fog_multiprocess(data ))
        t1=time.clock()
        
        print("Time : " , (t1-t0))
        
