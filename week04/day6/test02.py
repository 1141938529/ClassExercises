import multiprocessing

import time


class Product():
    def __init__(self, name):
        self.name = name


def producter(condition, conn):
    num = 0
    while True:
        with condition:
            num += 1
            p = Product("天地" + str(num) + "号")
            print("生产者：生产了" + p.name)
            conn.send(p)
            time.sleep(1)
            condition.notify()
            time.sleep(1)
            condition.wait()
    conn.close()


def consumer(condition, conn):
    print("1")
    while True:
        with condition:
            condition.notify()
            condition.wait()
            p = conn.recv()
            print("消费者：消费了" + p.name)
            condition.notify()
    conn.close()


if __name__ == '__main__':
    condiction = multiprocessing.Condition()
    mpipe = multiprocessing.Pipe(duplex=True)
    sendconn = mpipe[1]
    recvconn = mpipe[0]
    multiprocessing.Process(target=producter, args=(condiction, sendconn)).start()
    multiprocessing.Process(target=consumer, args=(condiction, recvconn)).start()

    print("main over")
    pass
