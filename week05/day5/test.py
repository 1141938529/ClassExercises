import re

if __name__ == '__main__':

    # print(re.search("\w","0"))
    # print(re.search("[a-z0-9_]+@[a-z\d]+\.([a-z]\d).*","0"))
    # 123456-1992-07-21-813x
    reMy = "[1-9]\d{5}-(19\d{2})|(200\d)|(201[0-7])-(((0[13578])|(1[02]))-(([012]\d)|(3[01])))|(((0[469])|(11))-([012]\d)|(30))|(02(([01]\d)|(2[0-8])))-\d{3}[0-9X]"
    res = re.match(reMy,"362204-1192-07-21-813X")
    print(res)
    pass