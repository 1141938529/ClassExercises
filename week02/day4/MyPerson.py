class MyPerson(object):
    name = None
    age = 0
    sex = None

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def selfTell(self):
        print("我是%s，今年%d，我的性别为:%s" % (self.name, self.age, self.sex))
    pass

    def __str__(self):
        return ("MyPerson{'name'= %s ,'age'=%d,'sex'=%s}"%(self.name,self.age,self.sex))


if __name__ == "__main__":
    mp = MyPerson("王五",21,"man")
    print(mp)
    pass