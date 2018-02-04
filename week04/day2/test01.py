import threading
import time

import _thread


def download(url, name="thread001"):
    tname = threading.current_thread().getName()
    print(name)
    print(tname + "下载地址：" + url)
    print(tname + "开始下载。。。。")
    for i in range(5):
        print(tname + "下载", i)
        time.sleep(1)
    print(tname + "下载完成！")


def thread1():
    _thread.start_new_thread(download, ("www.baidu.com",))
    for i in range(6):
        time.sleep(1)


class myThread(threading.Thread):
    def __init__(self, url):
        super(myThread, self).__init__()
        self.url = url

    def run(self):
        download(self.url)
        pass

    def __str__(self):
        return "name为" + self.getName() + "id为：" +str(self.ident)


def thread3():
    for i in range(5):
        mt = myThread("www.xinlang.com" + str(i))
        mt.start()
        # mt.join()


def thread2():
    threading.Thread(target=download, args=("www.tengxu.com",), kwargs={"name": "No.1"}, daemon=False).start()
    for i in range(3):
        time.sleep(1)


if __name__ == "__main__":
    # thread1()
    # thread2()
    thread3()

    mlist = threading.enumerate()
    print("main over")
    for thread in mlist:
        threading.active_count()
        print(thread)
