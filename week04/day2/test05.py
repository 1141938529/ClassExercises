import threading

import time


class Wife(threading.Thread):
    def __init__(self, apologize1, apologize2):
        super(Wife, self).__init__()
        self.apologize1 = apologize1
        self.apologize2 = apologize2

    def run(self):
        if self.apologize1.acquire(timeout=2):
            print("妻子：等待对方道歉。。。")
            time.sleep(1)
            if self.apologize2.acquire(timeout=2):
                print("妻子：我道歉")
                print("对方先道歉了")
                self.apologize2.release()
            else:
                print("妻子：对方不道歉，按我也不！！")
            self.apologize1.release()


class Husband(threading.Thread):
    def __init__(self, apologize1, apologize2):
        super(Husband, self).__init__()
        self.apologize1 = apologize1
        self.apologize2 = apologize2

    def run(self):
        if self.apologize1.acquire(timeout=2):
            print("丈夫：等待对方道歉。。。")
            time.sleep(1)
            if  self.apologize2.acquire(timeout=2):
                print("对方先道歉了")
                print("丈夫：我道歉")
                self.apologize2.release()
            else:
                print("丈夫：对方不道歉，按我也不！！")
        self.apologize1.release()

        pass


if __name__ == "__main__":
    wApologize = threading.Lock()
    hAologize = threading.Lock()
    Wife(hAologize, wApologize).start()
    Husband(wApologize, hAologize).start()
