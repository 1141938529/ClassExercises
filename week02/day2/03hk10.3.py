# 编写程序读取1-100之间的一些证书 并统计个数
# 获取键盘上的输入的字符串
mstr = input("enter integers between 1 and 100:")
# 将各个数字分开 装在mtuple中
mtuple = mstr.split(" ")
mtuple = [int(item) for item in mtuple]
# 获取总共有多少种数字 装在mlist中
mlist = sorted(set(mtuple))
# mlist2 = [int(item) for item in mlist]
mlist.sort()
for item in mlist:
    counts = mtuple.count(item)
    if counts > 1:
        print("%d occurs %d times" % (item, counts))
    else:
        print("%d occurs %d time" % (item, counts))

# print(mlist)
# print(mstr.split(" "))s
