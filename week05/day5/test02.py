import re


def reMatch():
    pattern = "[pP]ython"
    mstr1 = "python 我的最爱，哇哇哦哦"
    mstr2 = "Python 我的最爱，哇哇哦哦"
    mstr3 = "ssssaaPython 我的最爱，哇哇哦哦"
    print(re.match(pattern, mstr1))
    print(re.match(pattern, mstr2))
    print(re.match(pattern, mstr3))


def reSearch():
    pattern = "[pP]ython"
    mstr1 = "asassassaspython 我的最爱，哇哇哦哦"
    mstr2 = "saaaaaaaPyathon 我的最爱，哇哇哦哦"
    mstr3 = "ssssaaPython 我的最爱，哇哇哦哦"
    print(re.search(pattern, mstr1))
    print(re.search(pattern, mstr2))
    print(re.search(pattern, mstr3))


def reFindall():
    pattern = "[pP]ython|派森|拍森"
    mstr1 = "我叫python，法力无边，派森大法，法力无边，拍森嗨呀"
    mstr2 = "拍森ssssaPythonsss"
    mstr3 = "ssssssssssssss"
    mlist1 = re.findall(pattern, mstr1)
    mlist2 = re.findall(pattern, mstr2)
    mlist3 = re.findall(pattern, mstr3)
    print(mlist1)
    print(mlist2)
    print(mlist3)


if __name__ == '__main__':
    reMatch()
    # # reSearch()
    # # reFindall()
    # pattern = "[pP]ython|派森|拍森"
    # mstr1 = "我叫python，法力无边，派森大法，法力无边，拍森嗨呀,我爱Python。派森啊"
    # str1=re.sub(pattern,"fuck",mstr1)
    # print(str1)
    # pass
    import re

    mstr = "('book','ajax','id','1','sky','6bffd153bf8c3722e3c2e7cd23f74567','t','1515175044');"

    mre = r".*sky','(\w+)'*"

    print(re.match(mre, mstr).group(1))