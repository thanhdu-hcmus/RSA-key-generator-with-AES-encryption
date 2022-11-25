import sys
from genkeys import *
from crypt import *
from time import time
import numpy as np
import matplotlib.pyplot as plt

def calAverageTime():
    fi = open("Time.txt","r", encoding='utf-8')
    data = []
    while fi:
        line = fi.readline()
        if line == "":
            break
        time = float(line.rstrip('\n'))
        data.append(time)
    print(data)
    print(np.mean(data))
    fi.close()
    plt.hist(data)
    plt.xlabel('Time (s)')
    plt.ylabel('Number of occurrences')
    plt.show()

if (__name__ == "__main__"):
    fo = open("Time.txt","w", encoding='utf-8')
    for i in range(0,1000):
        start_time = time()
        makeKeyFiles("alice", 1024)
        encrypt("alice.pub","sample-10mb-text-file.txt","message.cip")
        decrypt("alice.prv","message.cip","secret.txt",)
        end_time = time()
        print('Time generating: %s' %(end_time - start_time))
        fo.write(str(end_time - start_time)+'\n')
    fo.close()
    calAverageTime()