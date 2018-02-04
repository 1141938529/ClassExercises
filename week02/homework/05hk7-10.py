import time


class Time():
    __hour = 0
    __minute = 0
    __second = 0
    curSecond = int(time.time() % (24 * 60 * 60))

    def __init__(self,
                 hour=curSecond // (60 * 60),
                 minute=curSecond % (60 * 60) // 60,
                 second=curSecond % (60)):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elaspTime):
        curSecond1 = elaspTime % (24 * 60 * 60)
        self.__hour = curSecond1 // (60 * 60)
        self.__minute = curSecond1 % (60 * 60) // 60
        self.__second = curSecond1 % (60)
        pass


if __name__ == "__main__":
    print(time.time())
    curSecond = int(55550505 % (24 * 60 * 60))
    hour = curSecond // (60 * 60)
    minute = curSecond % (60 * 60) // 60
    seccond = curSecond % (60)
    print(curSecond, hour, minute, seccond)
    mtime = Time()
    print("当前时间为：%d：%d：%d" % (mtime.getHour(), mtime.getMinute(), mtime.getSecond()))
    elapsedtimes = eval(input("请输入你要设置的时间总秒数："))
    mtime.setTime(elapsedtimes)
    print("你所设置的时间为：%d：%d：%d" % (mtime.getHour(), mtime.getMinute(), mtime.getSecond()))
    pass
