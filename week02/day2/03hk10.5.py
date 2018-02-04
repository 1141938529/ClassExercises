# 有空格飞凯输入一行数字  显示是不重复的数字（即如果一个数字重复出现只显示一次）
mystr = input("enter ten numbers:")
mylist1 = mystr.split(" ")
mylist2 = []
for item in mylist1:
    if mylist2.count(item) == 0:
        mylist2.append(item)
    pass
print("the distinct numbers are:", end=" ")
for item in mylist2:
    print(item, end=" ")
    pass
