import os
import sys
# import ConfigParser
# import xlwings as xw
import multiprocessing
import time

def run(fn):
    time.sleep(2)
    print fn
    return fn*2

if __name__ == '__main__':
    startTime = time.time()
    testFL = [1,2,3,4,5]
    pool = multiprocessing.Pool(10)
    result = pool.map(run, testFL)
    pool.close()
    pool.join()
    endTime = time.time()

    for num in result:
        print num

    print 'time :', endTime - startTime
