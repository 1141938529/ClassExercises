'''@ 多线程：
· 使用三种不同的方式开辟三条不同的线程ta，tb，tc；
· ta，tb，tc分别求出1-100内的所有奇数、质数（除了1和自身外没有因子）、平方数（1、4、9、16...）；
· 当所有结果已得到时，在主线程中打印结果；
· 提示：主线程必须等待子线程执行完毕；

'''
import threading
from threading import Thread

# 求奇数
import math

import _thread

import time

mdict = {}

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
    def run(self):
        getSquareNumber()
    pass


def getOdd():
    mlist = []
    for i in range(1, 101):
        if i % 2 == 1:
            mlist.append(i)
    mdict["奇数"] = mlist
    # return mlist
    pass

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 求质数
def getPrimeNumber():
    mlist = []
    for i in range(2, 101):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
        else:
            mlist.append(i)
    mdict["质数"] = mlist
    pass


# 求平方数
def getSquareNumber():
    mlist = []
    for i in range(1, 101):
        if round(math.sqrt(i)) ** 2 == i:
            mlist.append(i)
    mdict["平方数"] = mlist
    pass


if __name__ == "__main__":

    _thread.start_new_thread(getPrimeNumber,())
    tb = Thread(target=getOdd)
    tb.start()
    tb.join()
    tc= MyThread()
    tc.start()
    tc.join()
    while mdict["质数"]==None:
        pass
    print("质数为：",mdict["质数"])
    print("平方数为：",mdict["平方数"])
    print("奇数为：",mdict["奇数"])

