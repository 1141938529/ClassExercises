class MyPerson2(object):
    name = None
    age = 0
    sex = None

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("创建对象")

    def selfTell(self):
        print("我是%s，今年%d，我的性别为:%s" % (self.name, self.age, self.sex))
    pass

    def __str__(self):
        return ("MyPerson{'name'= %s ,'age'=%d,'sex'=%s}"%(self.name,self.age,self.sex))

    def __del__(self):
        print("销毁对象")
    def __len__(self):
        return 10
    # > 用__gt__ 的方法重写  年龄比较  返回2个人之后的大的数
    def __gt__(self, other):
        Bool = True if self.age>other.age else False
        return Bool
    # + 表示2个人的名字相加，年级取小的，性别无所谓
    def __add__(self, other):
        mp3 = MyPerson2(self.name + other.name,self.age + other.age,self.sex +other.sex)
        print("合作了！")
        return mp3

    # + 表示2个人的名字，年级取小的，性别无所谓
    def __sub__(self, other):
        mp4 = self if self.age>other.age else other
        mp4.sex = "我获胜了"
        mp4.name = "No1"+mp4.name
        mp4.age = self.age+other.age
        return mp4

if __name__ == "__main__":
    mp1 = MyPerson2("王五", 21, "man")
    mp2 = MyPerson2("李四", 23, "woman")
    print(mp1)
    print(len(mp1))
    print(mp1>mp2)
    print(mp1 + mp2)
    print(mp1 - mp2)
    print(mp2-MyPerson2("来六",21, "man"))
    pass