from week02.day4.MyPerson import MyPerson


class Man(MyPerson):

    def selfTell(self):
        print("劳资%s，纵横江湖%d年，我的性别为:%s" % (self.name, self.age, self.sex))

    def paoxiao(self):
        print("吼吼吼 咆哮")
pass

if __name__ == "__main__":
    man = Man("lisi",23,"nan")
    man.selfTell()
    pass