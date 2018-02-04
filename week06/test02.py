'''
    写一个函数，传入一个文件夹路径，实现递归遍历并统计该文件夹下的文件数量
'''
import csv
import json
import os
import threading

import threadpool

num = 0
def findFiles(path):
    global num
    for file in os.listdir(path):
        if os.path.isfile(path+"/"+file):
            num+=1
        else:
            findFiles(path+"/"+file)
    return num
    pass

'''
·并发10条线程求1到一亿的和
 '''
result = 0
def getsum(start,end):
    global result
    total = 0
    for i in range(start,end):
        total +=i

    result +=total


def getSum():
    tList = []
    for i in range(10):
        t = threading.Thread(target=getsum, args=(10 ** 4 * i + 1, 10 ** 4 * (i + 1)))
        t.start()
        tList.append(t)
    for t in tList:
        t.join()
    print(result)

'''
·读取D:\PyDownload\stocks\600123_大神集团.csv并打印其内容；
·读取D:\PyDownload\stocks\600123_大神集团.json并打印其内容；
'''
def readCsvFile(path):
    with open(path,mode="r") as file:
        csvReader = csv.reader(file)
        for item in csvReader:
            print(item)
    pass
def writeCsvFile(mstr,path):
    with open(path,mode="w") as file:
        csvWriter = csv.writer(file)
        for item in mstr:
            csvWriter.writerow(item)
    pass
def readJsonFile(path):
    with open(path,mode="r",encoding="utf-8") as file:
        content = file.read()
        pyobj = json.loads(content)
        print(pyobj)
    pass
def writeJsonFile(mdicts,path):
    with open(path,mode="w",encoding="utf-8") as file:
        jsonObj = json.dumps(mdicts)
        file.write(jsonObj)
    pass

if __name__ == '__main__':
    # getSum()
   pass