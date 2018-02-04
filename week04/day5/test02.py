# 协程


import time
from greenlet import greenlet


def func1():
    print("床前明月光")
    time.sleep(1)
    gl2.switch()
    print("举头望明月")
    time.sleep(1)
    gl2.switch()
    pass
def func2():
    print("疑似地上霜")
    time.sleep(1)
    gl1.switch()
    print("低头思故乡")
    time.sleep(1)
    pass

gl1 = greenlet(func1)
gl2 = greenlet(func2)
if __name__ == "__main__":
    gl1.switch()
    pass
