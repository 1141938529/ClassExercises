import random


def test01():
    mset = set()
    for i in range(10):
        mset.add(i)
    for i in mset:
        print(i)


def test02():
    mstr = input("请输入一行数字（空格隔开）：")
    mlist1 = mstr.split(" ")
    mlist2 = []
    for item in mlist1:
        if mlist2.count(item) == 0:
            mlist2.append(item)
    return mlist2
    pass


def test03():
    mstr = input("请输入一行数字（空格隔开）：")
    list1 = list(set(mstr.split(" ")))
    return list1


def test04():
    list1 = [1, 2, 5, 1, 2, 1, 5, 3, 5, 6, 4, 9, 8, 7, 9]
    print(random.sample(list1, len(list1)))
    print(random.sample(range(10), 10))
    random.shuffle(list1)
    print(list1)


def test05():
    wd1 = input("请输入第一个单词").strip()
    wd2 = input("请输入第二个单词").strip()
    if (sorted(wd1) == sorted(wd2)):
        print("是像是单词")
    else:
        print("不是相识单词")
    print(wd1)
    print(wd2)

pass

if __name__ == "__main__":
    # test01()
    # test02()  ['1', '25', '54', '2', '3', '6', '21', '12']
    # print(test03())
    # reversed()
    # range()
    test05()
