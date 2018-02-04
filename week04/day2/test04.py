import threading

import time


class BankBook(threading.Thread):
    def __init__(self, acount):
        super(BankBook, self).__init__()
        self.acount = acount

    def run(self):
        print("办理银行存折业务")
        if acount.acquire(timeout=3):
            print("存折办理中...........")
            time.sleep(1)
            # acount.release()
            # print("办理完成")
        else:
            print("账户正在办理其他业务，请稍后。。。。")
        pass


class BankCard(threading.Thread):
    def __init__(self, acount):
        super(BankCard, self).__init__()
        self.acount = acount

    def run(self):
        print("办理银行卡取钱业务")
        if acount.acquire(timeout=3):
            print("银行卡办理中...........")
            time.sleep(1)
            acount.release()
            print("办理完成")
        else:
            print("账户正在办理其他业务，请稍后。。。。")

if __name__ == "__main__":
    acount = threading.Lock()
    BankBook(acount).start()
    BankCard(acount).start()
    pass
