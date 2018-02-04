# 进程池
import multiprocessing

import time


def func(start, end):
    result = 0
    time.sleep(1)
    for i in range(start, end + 1):
        result += i
    print(result)
    pass


def func2(start, end):
    result = 0
    time.sleep(5)
    for i in range(start, end + 1):
        result += i
    print(result)
    pass


def func3(start, end):
    result = 0
    time.sleep(2)
    for i in range(start, end + 1):
        result += i
    print(result)
    pass


def handleResult(result):
    print(result)
    pass


def handleError(error):
    pass


def asyncProcess():
    mpool = multiprocessing.Pool()
    mpool.apply_async(func2, args=(10000, 50000), callback=handleResult, error_callback=handleError)
    mpool.apply_async(func, args=(1, 5), callback=handleResult, error_callback=handleError)
    mpool.apply_async(func3, args=(100, 500), callback=handleResult, error_callback=handleError)
    mpool.close()
    mpool.join()


def sycnProcess():
    mpool = multiprocessing.Pool()
    mpool.apply(func=func2, args=(10, 50))
    mpool.apply(func=func, args=(1, 5))
    mpool.apply(func=func3, args=(100, 500))
    mpool.close()
    mpool.join()


if __name__ == '__main__':
    # sycnProcess()
    asyncProcess()

    print("main over")
