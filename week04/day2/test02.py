# 进程的死锁
import threading

import time

moneyLock = threading.Lock()
techLock = threading.Lock()
def money():
    if moneyLock.acquire():
        time.sleep(2)
        if techLock.acquire():
            print("我有钱")
            techLock.release()
        moneyLock.release()
    pass
def tech():
    if techLock.acquire():
        time.sleep(2)
        if moneyLock.acquire():
            print("我you计数")
            moneyLock.release()
        techLock.release()
    pass

if __name__ == "__main__":
    threading.Thread(target=money).start()
    threading.Thread(target=tech).start()
    pass