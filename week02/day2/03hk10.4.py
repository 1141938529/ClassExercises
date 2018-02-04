# 输入一行数 然后打印出有多少个大于平均的数 多少个小于平均的数
mystr = input("请输入学生的成绩（2个成绩之间空格隔开）：")
mylist = mystr.split(" ")
mysum = 0
for item in mylist:
    mysum += int(item)
average = mysum / (len(mylist))
count1 = 0
count2 = 0
for item in mylist:
    if int(item) >= average:
        count1 += 1
    else:
        count2 +=1
        pass
print("%d个人的成绩小于平均分，%d个人的成绩大于等于平均分"%(count2,count1))
