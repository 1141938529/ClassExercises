import os
import random
mstr=str(random.randint(0,100))
for i in range(49):
    mstr=mstr+" "+str(random.randint(0,100))
while True:
    filename = input("请输入文件名：")
    if not(os.path.exists("./alldirs/"+filename)):
        file = open("./alldirs/"+filename,mode="a+",encoding="utf-8")
        break
    else:
        print("该文件已存在，请重新输入！")
        pass
file.write(mstr)
# 此时的游标在末尾  需要移动到初始位置
file.seek(0)
mlist = file.read().split(" ")
# 将list中字符型元素转换为int型
for i in range(len(mlist)):
    mlist[i] = int(mlist[i])
mlist.sort()
for i in mlist:
    print(i,end=" ")
file.close()