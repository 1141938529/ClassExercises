from week02.day4.PersonClass import Person


class BadGay(Person):
    horrbit  = None
    def __init__(self ,name, age, RMB, password,horrbit):
        super(BadGay, self).__init__(name, age, RMB, password)
        self.horrbit=horrbit

    def doBad(self):
        print("我要去%s"%(self.horrbit))
    pass

if __name__ == "__main__":
    mh = BadGay("李四",22,100,"54621","LOL")
    mh.selfTell()
    mh.doBad()
    mh.setPassword("54621")
    print(mh.horrbit)
