#
import multiprocessing

import time


def func():
    time.sleep(4)
    pass


def test01():
    multp = multiprocessing.Process(target=func)
    multp.daemon = False
    multp.name = "ssss"
    multp.start()
    # multiprocessing.context
    multlist = multiprocessing.active_children()
    print(len(multlist))
    for mult in multlist:
        print(mult)


if __name__ == "__main__":
    # test01()
    mypool = multiprocessing.Pool(3)
    mypool.apply()