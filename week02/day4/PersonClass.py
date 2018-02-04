class Person():
    name = None
    age = 0
    __RMB = 0
    password = None

    def __init__(self, name, age, RMB, password):
        self.name = name
        self.age = age
        self.__RMB = RMB
        self.password = password

    def setPassword(self,password):
        if password == self.password:
           newpw = input("请输入新密码的为：")
           self.password = newpw
        else:
            print("密码错误，修改失败")

    def searchRMB(self, password):
        if password == self.password:
            print("你的存款为：%d"%(self.__RMB))
        else:
            print("密码错误，查询失败")
        pass

    def selfTell(self):
        print("我是%s，今年%d，我有%.2f元钱" % (self.name, self.age, self.__RMB))
    pass


if __name__ == "__main__":
    p = Person("张三", 21, 10000,"123456")
    p.selfTell()
    p.searchRMB("123456")
    p.setPassword("123456")
    print(p.password)