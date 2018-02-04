import csv

datalist = [
    {"name": "张三", "age": 20, "hobby": "看片"},
    {"name": "lisi", "age": 20, "hobby": "coding"},
    {"name": "wangwu", "age": 40, "hobby": "读书"},
    {"name": "zhaoliu", "age": 20, "hobby": "coding"},
]


def writeCsv():
    fileobj = open("./res/人员信息表.csv", mode="w", newline="")
    csvWrite = csv.writer(fileobj)
    csvWrite.writerow(list(datalist[0].keys()))
    for item in datalist:
        csvWrite.writerow(list(item.values()))
    fileobj.close()


def readCsv():
    fileobj = open("./res/人员信息表.csv", mode="r")
    csvReader = csv.reader(fileobj)
    for item in csvReader:
        print(item)


if __name__ == '__main__':
    # writeCsv()
    readCsv()
    pass
