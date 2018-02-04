from week02.day4.MyPerson import MyPerson


class Woman(MyPerson):

    def selfTell(self):
        print("小女子%s，芳龄%d年，人家是个:%s" % (self.name, self.age, self.sex))

    def sajiao(self):
        print("嘻嘻嘻，撒娇")
    pass