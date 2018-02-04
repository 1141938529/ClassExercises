def excis3_9():
    name = input("Enter employees's:")
    weekhours = input("enter number of hours worked in a week:")

    pass


def excis8_1():
    mstr = input("请输入字符串：")
    isValid = True
    if len(mstr) == 11:
        for i in range(len(mstr)):
            if (i == 3 or i == 6) and mstr[i] == "-":
                pass
            elif ord(mstr[i]) >= ord("0") and ord(mstr[i]) <= ord("9"):
                pass
            else:
                isValid = False
                # print("hello i'm error")
                break
    else:
        isValid = False

    if isValid:
        print("Valid SSN")
    else:
        print("InValid SSN")
    pass


def excis8_2():
    mstr1 = input("第一个字符串：")
    mstr2 = input("第二个字符串：")

    pass


def excis8_4():
    mstr1 = input("第一个字符串：")
    print(mstr1.count("hello"))
    print(mstr1.isalpha())
    mstr2 = "A"
    mstr3 = mstr2.lower()
    print(mstr3)
    # mstr1[1] = "A"
    print(mstr1)
    print("pqrs".find("p"))
    pass


def excis8_7():
    mstr1 = input("第一个字符串：")
    mstr1 = mstr1.lower()
    for i in range(len(mstr1)):
        if mstr1[i].isalpha():

            if ((ord(mstr1[i]) - ord("a")) // 3 + 2) < 7:
                mstr1 = mstr1[:i] + str((ord(mstr1[i]) - ord("a")) // 3 + 2) + mstr1[i + 1:]
            elif "pqrs".find(mstr1[i]) >= 0:
                mstr1 = mstr1[:i] + "7" + mstr1[i + 1:]
            elif "tuv".find(mstr1[i]) >= 0:
                mstr1 = mstr1[:i] + "8" + mstr1[i + 1:]
            elif "wxyz".find(mstr1[i]) >= 0:
                mstr1 = mstr1[:i] + "9" + mstr1[i + 1:]
                pass
    print("结果为：" + mstr1)

    pass


def excis8_3():
    mstr1 = input("第一个字符串：")
    numcounts = 0
    isValid = True
    if len(mstr1) >= 8:
        for i in range(len(mstr1)):
            if (ord(mstr1[i]) >= ord("0") and ord(mstr1[i]) <= ord("9")):
                numcounts += 1
                pass
            elif (ord(mstr1[i]) >= ord("a") and ord(mstr1[i]) <= ord("z")
                  ) or (ord(mstr1[i]) >= ord("A") and ord(mstr1[i]) <= ord("Z")):
                pass
            else:
                isValid = False
        if numcounts < 2:
            isValid = False
    else:
        isValid = False

    if isValid:
        print("Valid SSN")
    else:
        print("InValid SSN")


def excise8_11():
    mstr1 = input("第一个字符串：")
    mstr2 = ""
    for char in reversed(mstr1):
        mstr2 += char
        pass
    print(mstr2)
    pass


def excise8_12():
    mstr = input("请输入基因序列：")

    mstrList = []
    while len(mstr) > 6:
        if "ATG" in mstr:
            mstr = mstr[mstr.find("ATG") + 3:]
            if ("TAG" in mstr) or ("TAA" in mstr) or ("TGA" in mstr):
                index = min(mstr.find("TAG") if mstr.find("TAG") != -1 else len(mstr),
                            mstr.find("TAA") if mstr.find("TAA") != -1 else len(mstr),
                            mstr.find("TGA") if mstr.find("TGA") != -1 else len(mstr))
                mstr1 = mstr[:index]
                mstr = mstr[index + 3:]
                if (len(mstr1) % 3 == 0):
                    mstrList.append(mstr1)
            else:
                break
        else:
            break
    if len(mstrList) > 0:
        for item in mstrList:
            print(item)
    else:
        print("no gene is found")


def excise8_13():
    mstr1 = input("请输入基因序列：")
    mstr2 = input("请输入基因序列：")
    mstr3 = ""
    for i in range(len(mstr1) if (len(mstr1) < len(mstr2)) else len(mstr2)):
        if mstr1[i] == mstr2[i]:
            mstr3 += mstr1[i]
        else:
            break
    print(mstr3)


def excise8_14():
    while True:
        mstr1 = input("请输入一个9位的数字:")
        if len(mstr1) == 9 and mstr1.isdigit():
            break
        else:
            print("输入有误！请重新输入")
    d10 = 0
    for i in range(len(mstr1)):
        d10 += int(mstr1[i]) * (i + 1)
    d10 = d10 % 11
    if (d10) == 10:
        str10 = "X"
    else:
        str10 = str(d10)
    print(mstr1 + str10)

def charSort():
    mstr = "abc"
    mlist = list(mstr)
    # print(mlist)
    list2 = []
    print(example(mlist)[1])
    # print(removestr(mlist,1))
    pass

def removestr(list,i):
    mlist=[]
    for j in range(len(list)):
        if j!=i:
            mlist +=list[j]
    return mlist

def example(mlist):
    newstr = ""
    list2 = []
    if mlist!=[]:
        for i in range(len(mlist)):
            if len(mlist)==1:
                newstr =mlist[i]

            else:
                # print(mlist.remove(mlist[i]))
                newstr = example(removestr(mlist,i))[0]+mlist[i]
                list2.append(newstr)
            pass

    return newstr,list2
    pass


def test():
    print("".join(reversed("123456")))
    pass


if __name__ == "__main__":
    # excis3_9()
    # excis8_4()
    # excis8_7()
    # excise8_11()
    # excise8_12()
    # excise8_13()
    # excise8_14()
    charSort()
pass
