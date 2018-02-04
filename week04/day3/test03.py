# 线程池
import threading

import threadpool
import time


def func(name, price, reason="有时候杀人不需要理由！"):
    print(threading.current_thread().getName() + "开始杀%s了。。。，赏金是：%d，理由是%s" % (name, price, reason))
    if (price > 250):
        raise RuntimeError(threading.current_thread().getName() + "对面太厉害了，打不过！")
    else:
        return threading.current_thread().getName() + "杀完了，收工！"

    pass


def handleData(request, result):
    print(request, result)
    pass


def handleExc(request, excInfo):
    print(request, excInfo)
    pass


if __name__ == "__main__":
    tpool = threadpool.ThreadPool(3)
    reqs = threadpool.makeRequests(func,
                                   [
                                       (["张三", 100], {"reason": "长得太丑了，影响市容！"}),
                                       (["李四", 300], {"reason": "长得太帅了，必须死！"}),
                                       (["王五", 500], {"reason": "长得一般，没啥创意！"}),
                                       (["赵六", 200], {"reason": "长得还行，就是没啥特点！"}),
                                       (["麻七", 400], None),
                                   ],
                                   callback=handleData,
                                   exc_callback=handleExc)

    for req in reqs:
        tpool.putRequest(req)

    tpool.wait()

    pass
