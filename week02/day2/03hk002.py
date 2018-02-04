# 人口信息统计表
# ·使用input每次一个人员信息，形成一个元组，输入0代表输入结束
# ·（张三，男，20），（李四，女，30），（王五，男，25）...
# ·将所有失踪人员信息统计为一个列表
# ·遍历该列表，将人员信息打印为一个表格
# ·打印时按年龄降序排列

mlist = []
while True:
    mstr = input("请输入人员信息：")
    if (mstr == "0"):
        break
    mtuple = tuple(mstr.split(","))
    # print(mtuple)
    mlist.append(mtuple)
# print(mlist)
print(format("姓名", "5s"), format("性别", "5s"), format("年龄", "5s"))
# 把tuple 的元素转换成字符串进行排序在突破了输出
mlist0 = []
for item in mlist:
    mstr0 = item[2] + "," + item[0] + "," + item[1]
    mlist0.append(mstr0)
mlist0.sort(reverse=True)
for item in mlist0:
    mytuple0 = tuple(item.split(","))
    print(format(mytuple0[1], "5s"), format(mytuple0[2], "5s"), format(mytuple0[0], "5s"))
