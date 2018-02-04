# 4.8
a, b, c = eval(input("请输入三个整数值："))
min = min(a, b, c)
max = max(a, b, c)
if (a == min):  # 如果a最小
    if (b == max):  # 如果b最大
        print("这三个数的从大到小为：%d,%d,%d" % (b, c, a))
        pass
    else:
        print("这三个数的从大到小为：%d,%d,%d" % (c, b, a))
        pass
    pass
elif (a == max):  # 如果a最大
    if (b == min):  # 如果b最小
        print("这三个数的从大到小为：%d,%d,%d" % (a, c, b))
        pass
    else:
        print("这三个数的从大到小为：%d,%d,%d" % (a, b, c))
        pass
    pass
else:
    print("这三个数的从大到小为：%d,%d,%d" % (max, a, min))
    pass

