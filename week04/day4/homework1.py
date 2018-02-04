import multiprocessing

import time


class Product:
    def __init__(self,name):
        self.name = name

def producter(mcond,connShop):
    num = 0
    while True:
        with mcond:
            num +=1
            p = Product("生产者%d号"%(num))
            print("生产者生产了"+p.name)
            connShop.send(p)
            mcond.notify()
            time.sleep(1)
            mcond.wait()
    connShop.close()
    pass
def consumer(mcond,connShop):
    while True:
        with mcond:
            print("-----------")
            time.sleep(1)
            mcond.notify()
            p = connShop.recv()
            print("消费者消费了"+p.name)
            mcond.wait()
    connShop.close()


if __name__ == "__main__":
    mcond = multiprocessing.Condition()
    mpipe = multiprocessing.Pipe(duplex=False)
    sendproduct = mpipe[1]
    recvproduct = mpipe[0]
    mp1 = multiprocessing.Process(target=producter,args=(mcond,sendproduct))
    mp2= multiprocessing.Process(target=consumer,args=(mcond,recvproduct))
    mp1.start()
    mp2.start()
    print("main voer")
    pass