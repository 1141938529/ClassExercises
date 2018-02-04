# mdict = {"name": "zhangsan", "age": 20,"name1": "zhangsan", "age1": 20}
# print(type(mdict.values()))
# print(type(mdict.keys()))
# print(mdict.keys())

class Person():
    name = None
    age = 0
    rmb = 0

    def __init__(self, name, age, rmb):
        self.name = name
        self.age = age
        self.rmb = rmb
        pass

    def selfTell(self):
        print("我叫%s，我%d岁了，现在存款有%.2fRMB" % (self.name, self.age, self.rmb))
        pass

    pass


if __name__ == "__main__":
    p1 = Person("zhangsan", 21, 10000)
# p2 = Person(21, 10000)
    p1.selfTell()
