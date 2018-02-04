import multiprocessing

import time


def func1(num,count):
    pname = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    if(num>count):
        for i in range(num):
            print(pname+"",i)
            time.sleep(1)
        return pname+"输完了！"
    else:
        raise RuntimeError("GG，有异常！")
    pass

def func2(num):
    pname = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    for i in range(num):
        print(pname + "", i)
        time.sleep(1)
    return pname+"shu wan l！"


def handleResult(result):
    print(result)
    pass
def handleError(errorInfo):
    print(errorInfo)
    pass

if __name__ == "__main__":
    mpool = multiprocessing.Pool(3)
    mpool.apply_async(func1,args=(10,5),callback=handleResult,error_callback=handleError)
    mpool.apply_async(func2,args=(10,),callback=handleResult,error_callback=handleError)
    mpool.apply_async(func1,args=(5,10),callback=handleResult,error_callback=handleError)
    mpool.apply_async(func2,args=(5,),callback=handleResult,error_callback=handleError)
    mpool.close()
    mpool.join()
    pass