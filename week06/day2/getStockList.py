'''
.东方财富网爬取沪深个股列表
·http://quote.eastmoney.com/stocklist.html
·将爬到的数据写入CSV文件

'''
import re

# <a target="_blank" href="http://quote.eastmoney.com/sh203008.html">0501R028(203008)</a>
import requests

from week06.SpiderUtils import printList, writeCsvFile

url = "http://quote.eastmoney.com/stocklist.html"
reStockName = '<a .+>(\w+\(\d{6}\))</a>'
reStockCode = '\w+\((\d{6})\)'
reStockName = re.compile(reStockName)
reStockCode= re.compile(reStockCode)
if __name__ == '__main__':
    finalList = []
    html = requests.get(url).content.decode("gbk")
    stockNameList = reStockName.findall(html)
    # print(len(stockNameList))
    # printList(stockNameList)

    for stockName in stockNameList:
        if reStockCode.search(stockName):
            finalList.append([stockName])
        pass

    writeCsvFile(r"D:\PyDownload\沪深个股列表.csv",finalList)
    pass
