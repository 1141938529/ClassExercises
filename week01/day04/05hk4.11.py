# 用户输入某年某月求该月的天数
year = eval(input("请输入年份："))
month = eval(input("请输入月份："))

if (month == 1):
    print("%d年一月份有31天" % year)
    pass
elif (month == 2):
    # 判断今年是否为闰年
    isRun = True if ((year % 4 == 0 and year % 100 != 0)
                     or (year % 400 == 0)) else False
    if (isRun):
        print("%d年二月份有29天" % year)
        pass
    else:
        print("%d年二月份有28天" % year)
        pass
    pass
elif (month == 3):
    print("%d年三月份有31天" % year)
    pass
elif (month == 4):
    print("%d年四月份有30天" % year)
    pass
elif (month == 5):
    print("%d年五月份有31天" % year)
    pass
elif (month == 6):
    print("%d年六月份有30天" % year)
    pass
elif (month == 7):
    print("%d年七月份有31天" % year)
    pass
elif (month == 8):
    print("%d年八月份有31天" % year)
    pass
elif (month == 9):
    print("%d年九月份有30天" % year)
    pass
elif (month == 10):
    print("%d年十月份有31天" % year)
    pass
elif (month == 11):
    print("%d年十一月份有30天" % year)
    pass
else:
    print("%d年十二月份有31天" % year)
    pass
