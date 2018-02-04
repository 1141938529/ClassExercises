import threading
import time

import threadpool


def singleThread():
    starttime = time.time()
    calculation(1, 10 ** 8)
    endtime = time.time()
    realtime = (endtime - starttime)
    print(format(realtime, ".2f"))


def multiThread():
    starttime = time.time()

    for i in range(10):
        mpool = threadpool.ThreadPool(10)
        rag = []
        for i in range(10):
            rag.append(([i*10**7+1,(i+1)*10**7],))
        # [([],{}),()]
        # ([1, 50], {"count": 20, "algor": "素数"})
        print(rag)
        reqs = threadpool.makeRequests(calculation, rag)
        for req in reqs:
            mpool.putRequest(req)
        mpool.wait()

    endtime = time.time()
    realtime = (endtime - starttime)
    print(format(realtime, ".2f"))


def calculation(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


if __name__ == '__main__':
    # 单线程 从1到10**8
    # singleThread()
    multiThread()
    # print(format(20,".2f"))
    print("main  over")
