# 验证码生成器
import random


def verCodeGenerator(verNums=4, verChars=4):
    mstr = "ABCDEFGHIJKLIMNOPQRSTUVWXYZ0123456789"
    totalList = []
    for i in range(verNums):
        mlist = random.sample(mstr, verChars)
        str2 = "".join(mlist)
        totalList.append(str2)
    return totalList


print("-".join(verCodeGenerator(3, 2)))
