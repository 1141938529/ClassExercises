'''
·爬取网易主页上的所有图片
·所爬图片下载到：D:/PyDownload/
·以序号.jpg命名图片
'''
import re
import threading
from urllib.request import urlretrieve

import requests
# <img alt="王伟忠：做《康熙》属巧合"
# src="http://img1.gtimg.com/news/pics/hv1/174/56/2247/146125629.jpg">
from week06.SpiderUtils import printList

reImgUrl ='<img .*src="(http.*?)".*>'
reImgUrl = re.compile(reImgUrl)

def downloadImg(url,path):
    urlretrieve(url,filename = path)
    print(url,"下载成功")
    pass

if __name__ == '__main__':
    html = requests.get("http://www.qq.com/").text
    Urllist = reImgUrl.findall(html)
    # print(html)
    printList(Urllist)
    print("--------------------------------------",len(Urllist))
    # 对URLlist 分别下载
    i = 0
    tList = []
    for url in Urllist:
        path = "D:/PyDownload/"+str(i)+".jpg"
        t = threading.Thread(target=downloadImg,args=(url,path))
        t.start()
        i+=1
        tList.append(t)

    for t in tList:
        t.join()
    print("main over")
    pass
