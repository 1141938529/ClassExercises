import multiprocessing

import time


def func():
    print("hello ")
    time.sleep(1)
    print("func over")
    pass

if __name__ == '__main__':
    mp = multiprocessing.Process(target=func,name="hello")
    mp.start()
    print("main  over")
    pass
