'''
·在今日头条中搜索美女，得到待爬取的美女组图
·捕获其json数据
·分析其json数据
·将组图爬取下载到D:\\PyDownload\\
·创建组图同名的文件夹
·将所有图片下载到对应的组图文件夹下
'''
import json
import os
import threading
from urllib.request import urlretrieve

import re
import requests

url = 'https://www.toutiao.com/search_content/?' \
      'offset=0&format=json&keyword=meinv&autoload=true&count=20&cur_tab=1'
basePath = 'D:\\PyDownload\\'

reImgName = ".*\/(.*)"
reImgName = re.compile(reImgName)


def downloadImg(url, path):
    print()
    urlretrieve(url, filename=path)


if __name__ == '__main__':
    html = requests.get(url).text
    mJson = json.loads(html)
    grounpChartList = mJson["data"]
    # print(grounpChartList[0])
    tList = []
    for grounpChart in grounpChartList:
        # 判断是否是组图的字典
        if "title" in grounpChart:
            title = grounpChart["title"]
            dirPath = basePath + title + '\\'

            # 判断文件夹是否存在
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            image_detailList = grounpChart["image_detail"]
            for image_detail in image_detailList:
                imgUrl = image_detail["url"]
                imgName = reImgName.search(imgUrl).group(1)
                t = threading.Thread(target=downloadImg, args=(imgUrl, dirPath + imgName+".jpg"))
                t.start()
                tList.append(t)
        print("所有文件都开始下载 了.......")
    for t in tList:
        t.join()

    print("main over")