'''
----------
@ 线程池：
· 实现如下方法，从start到end之间任取count个素数（或平方数）
    def getNumbers(start,end,count=10,algor="素数")
· start或end为负数时抛出异常
· 以列表形式返回结果
· 使用3并发线程池返回素数、平方数各两组即4组结果，每组5个
· 在主线程打印结果

'''
import math
import random
import threading

import threadpool

# 所有线程的数据
dataList = []


# 取得数组列表的所有参数类
class NumbersMsg():
    def __init__(self, start, end, count, algor):
        self.start = start
        self.end = end
        self.count = count
        self.algor = algor

    pass


# 求质数
def getPrimeNumber(start, end):
    mlist = []
    # 素数 从2开始
    start = start if start > 2 else 2
    for i in range(start, end):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            mlist.append(i)
    return mlist
    pass


# 求平方数
def getSquareNumber(start, end):
    mlist = []
    for i in range(start, end):
        if round(math.sqrt(i)) ** 2 == i:
            mlist.append(i)
    return mlist
    pass


# 线程 函数
def getNumbers(start, end, count=10, algor="素数"):
    # start或end为负数时抛出异常
    momsg = NumbersMsg(start, end, count, algor)
    if (start < 0) or (end < 0) or (start > end):
        raise RuntimeError("范围有误！")
    # algor 为素数时
    elif algor == "素数":
        return momsg, getPrimeNumber(start, end)
    # algor 为平方数时
    elif algor == "平方数":
        return momsg, getSquareNumber(start, end)
    pass


# 子线程的返回值处理函数
def handleData(reqs, result):
    if len(result[1]) >= result[0].count:
        # 随机五个数字获取
        mlist = random.sample(result[1], result[0].count)
        dataList.append(True)
        dataList.append(result[0])
        dataList.append(mlist)
    else:
        dataList.append(False)
        dataList.append(result[0])
        dataList.append(result[1])
    pass


# 子线程异常处理函数
def handleExcrption(reqs, excInfo):
    print(reqs, excInfo)
    pass


if __name__ == "__main__":

    tpool = threadpool.ThreadPool(3)
    reqs = threadpool.makeRequests(getNumbers, [
        ([1, 50], {"count": 20, "algor": "素数"}),
        ([1, 150], {"count": 10, "algor": "平方数"}),
        ([90, 150], {"count": 5, "algor": "素数"}),
        ([-90, 150], {"count": 5, "algor": "素数"}),
        ([200, 400], {"count": 5, "algor": "平方数"})
    ], callback=handleData, exc_callback=handleExcrption)
    for req in reqs:
        tpool.putRequest(req)
    tpool.wait()
    for i in range(0, len(dataList), 3):
        if dataList[i]:
            print("%d—%d内随机的%d个%s为：" % (dataList[i + 1].start, dataList[i + 1].end,
                                        dataList[i + 1].count, dataList[i + 1].algor), dataList[i + 2])
        else:

            print("%d—%d内%s的个数不足%d个," % (dataList[i + 1].start, dataList[i + 1].end,
                                         dataList[i + 1].algor, dataList[i + 1].count), "所有的个数为：", dataList[i + 2])
    pass
