sum = 0
Num = 0
positiveNo = 0
negativeNo = 0
while True:
    value = eval(input("请输入一个数字"))
    if (value == 0):
        break
    sum += value
    if (value > 0):
        positiveNo += 1
        Num += 1
    else:
        negativeNo += 1
        Num += 1
# vear = sum/Num
if(Num == 0):
    print("正数有%d个，负数有%d个，平均值为%f，总和为%d" % (0, 0,0,0))
else:
  print("正数有%d个，负数有%d个，平均值为%f，总和为%d"%(positiveNo,negativeNo,sum/Num,sum))
