def Par5_4():
    print(format("公斤", "^5s"), format("磅", "^10s"))
    for i in range(1, 10):
        print(format(i, ">5d"), format(i * 1.609, ">10.3f"))


def Par5_5():
    print(format("公斤", "^6s"), format("磅", "^8s"),
          format("磅", "^8s"), format("公斤", "^6s"))
    for i in range(1, 101):
        print(format(2 * i - 1, "6d"), format((2 * i - 1) * 2.2, "8.1f"),
              format((15 + 5 * i) / 2.2, "10.2f"), format(15 + 5 * i, "8d"))


def Par5_6():
    print(format("英里", "^8s"), format("公里", "^6s"),
          format("公里", "^8s"), format("英里", "^8s"))
    for i in range(1, 11):
        print(format(i, "6d"), format(1.609 * i, "10.3f"),
              format((15 + 5 * i) / 1.609, "10.3f"), format(15 + 5 * i, "8d"))
    pass


def Par5_9():
    nowFate = 10000
    rate = 0.05
    mySum = 0
    for i in range(11):
        nowFate = (1 + rate) * nowFate
    pass
    for i in range(5):
        mySum += nowFate
        nowFate = nowFate = (1 + rate) * nowFate
    print("十年后的学费为：", format(nowFate, ".2f"))
    print("十年后的大学四年总学费为：", format(mySum, ".2f"))


def Par5_11():
    stuScoreList = []
    stuCount = eval(input("请输入学生个数:"))
    First = 0
    Scenod = 0
    Max = 0
    for i in range(stuCount):
        stuScore = eval(input("请输入第%d个学生的分数:" % (i + 1)))
        stuScoreList.append(stuScore)
    # 求最大值
    for i in range(len(stuScoreList)):
        if (stuScoreList[i] > First):
            First = stuScoreList[i]
        pass

    for i in range(len(stuScoreList)):
        if (stuScoreList[i] > Scenod):
            if (stuScoreList[i] != First):
                Scenod = stuScoreList[i]

    print("最高分为%d,次高分为:%d" % (First, Scenod))


def Par5_13():
    # 找出同时能整除5和6 的 正数  100-10000之间
    num = 0
    for i in range(100, 10001):
        if ((i % 5 == 0) and (i % 6 == 0)):
            print(format(i, "5d"), end="")
            num += 1
            if num % 10 == 0:
                num = 0
                print("")
            pass
    pass

def Par5_16(n1, n2):
    myMin = min(n1, n2)
    for i in range(myMin):
        if ((n1 % myMin == 0) and (n2 % myMin == 0)):
            return myMin
        else:
            myMin -= 1

def Par5_17():
    n = ord("~") - ord("!")
    for i in range(n+1):
        print(format(chr(ord("!") + i), "3s"), end=" ")
        if i % 10 == 9:
            print("")
        pass
# Par5_4()
# Par5_5()
# Par5_6()
# Par5_9()
# Par5_11()
# Par5_13()
# print(Par5_16(31,14))
Par5_17()