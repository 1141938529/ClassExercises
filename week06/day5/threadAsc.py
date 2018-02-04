import threading

import threadpool

def downloadStockCsv(code,name):
    pass


if __name__ == '__main__':
    tpool = threadpool.ThreadPool(10)
    stockList =[]
    argList=[]
    for stock in stockList:
        mstock =([stock[0],stock[1]],)
        argList.append(mstock)
    reqs = threadpool.makeRequests(downloadStockCsv,argList)
    for req in reqs:
        tpool.putRequest(req)
    tpool.wait()
    print("下载完成！")
    pass