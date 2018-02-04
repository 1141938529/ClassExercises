import threading

import time


class MyEvent(threading.Event):
    def __init__(self):
        super(MyEvent, self).__init__()
        self.args = None

    pass

    def setArgs(self, args):
        self.args = args

    def getArgs(self):
        return self.args


class MosueThread(threading.Thread):
    def __init__(self, event):
        super(MosueThread, self).__init__()
        self.event = event

    def run(self):
        mstr = "abcdefg"
        self.event.setArgs(mstr)
        self.event.sex ="nan"
        self.event.set()
        print("User:我第次点鼠标")
        time.sleep(1)
        pass


class OsThread(threading.Thread):
    def __init__(self, event):
        super(OsThread, self).__init__()
        self.event = event

    def run(self):
        self.event.wait()
        mstr = self.event.getArgs()
        print("osThread获得了数据："+str(mstr)+self.event.sex)
        event.clear()
        pass


if __name__ == "__main__":
    event = MyEvent()
    mt = MosueThread(event).start()
    ot = OsThread(event).start()

    pass
