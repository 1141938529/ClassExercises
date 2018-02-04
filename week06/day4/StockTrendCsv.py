'''
·从东方财富网爬取股票型基金走势数据
·http://quote.stockstar.com/fund/stock_3_1_1.html
·将爬到的数据写入CSV文件
'''
import csv
import re
import threading

import requests

baseurl = "http://quote.stockstar.com/fund/stock_3_1_"
# <table width="100%" border="0" cellpadding="0" cellspacing="0" class="trHover" id="table1">
reTable = "<tbody .*>([\s\S]+)</tbody>"

reTable = re.compile(reTable)
reTarget = ">([\w-].+?)<"
reDate = ">([\w.\-%]+?)<"
reDate = re.compile(reDate)

finalList = []
def singleGetData(url):
    print(url)
    global finalList
    html = requests.get(url).text
    table = reTable.search(html).group(1)
    dateList = reDate.findall(table)
    # print(len(dateList))
    # print(table)
    # 清洗过的数据
    for i in range(0, len(dateList), 10):
        mlist = []
        for j in range(10):
            if j == 0:
                dateList[i + j] = "#" + dateList[i + j]
            mlist.append(dateList[i + j])
        finalList.append(mlist)


if __name__ == '__main__':
    tList =[]
    for i in range(3):
        url = baseurl +str(i+1)+".html"
        t = threading.Thread(target=singleGetData,args=(url,))
        t.start()
        tList.append(t)
    for t in tList:
        t.join()

    with open("./基金走势数据.csv",mode="w",newline="") as file:
        print(len(finalList))
        csvWriter = csv.writer(file)
        for mlist in finalList:
            csvWriter.writerow(mlist)
    pass
