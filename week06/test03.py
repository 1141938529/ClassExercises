'''
·多线程爬取网易主页的所有图片，存入D:\PyDownload\imgs\下，使用时间戳做名字；
'''
import os
import random
import re
import threading
from urllib.request import urlretrieve

import requests
import time

path = "D://PyDownload//imgs//"
url = "http://www.163.com"
#  <img src="...." > <img .*src="(http.*?)".*>
reImg = "<img .*src=\"(http.+?)\".*>"

reImg = re.compile(reImg)


def downloadPic(url):
    fileName = path+str(int(time.time()))+str(random.randint(100,999))+".jpg"
    urlretrieve(url,filename=fileName)


if __name__ == '__main__':
    tList= []
    html = requests.get(url).text
    netList = reImg.findall(html)
    if not os.path.exists(path):
       os.makedirs(path)
    for net in netList:
        t = threading.Thread(target=downloadPic, args=(net,))
        t.start()
        tList.append(t)
    for t in tList:
        t.join()
    print("图片已经全部下载完成")
