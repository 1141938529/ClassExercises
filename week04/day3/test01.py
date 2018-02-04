import threading

import time


class Product():
    def __init__(self, name):
        self.name = name

    pass


class Producter(threading.Thread):
    def __init__(self, condition, shop):
        super(Producter, self).__init__()
        self.condition = condition
        self.shop = shop

    def run(self):
        while True:
            with condition:
                p = Product(time.ctime())
                self.shop.append(p)
                print("%s被生产了" % (p.name))
                condition.notify()
                print("Producter notify()")
                time.sleep(0.5)
                condition.wait()
                print("Producter wait over")

    pass


class Consumer(threading.Thread):
    def __init__(self, condition, shop):
        super(Consumer, self).__init__()
        self.condition = condition
        self.shop = shop

    def run(self):
        while True:
            with condition:
                condition.notify()
                time.sleep(2)
                print("Consumer notify()")
                p = self.shop.pop(0)
                print("%s被消费了"%(p.name))
                condition.wait()
                print("Consumer wait over")

    pass


if __name__ == "__main__":
    condition = threading.Condition()
    shop = []
    Producter(condition, shop).start()
    Consumer(condition, shop).start()
    pass
