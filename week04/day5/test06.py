'''

·使用生成器分三次生成谷歌（访问不到）、新浪、腾讯三个【网址-存储文件名称】键值对；
·使用三条协程分别获取网址页面内容；
·获取成功后，使用文件形式将页面文本存储到文件中，路径和文件名使用参数传递；
·获取超时的页面，存储“获取超时”到对应文件即可；
·全部六条协程结束后，输出“job done!”

'''

import gevent
import sys
from gevent import monkey
import requests

dicts = {"http://www.baidu.com/": "百度",
         "http://www.qq.com/":"腾讯",
         "http://www.sina.com.cn/":"新浪",
         "http://www.youtube.com/": "YouTube",
         }


def accessNetworks(netDicts):
    try:
        keys =netDicts.keys()
        for key in keys:
            url = key
        res = requests.get(key)
        html = res.text
    except requests.exceptions.ConnectionError:
        html = "获取超时"
        pass

    dicts[key] = html
    print(key + " is ok")
    saveFile(key,netDicts[key])


def saveFile(url, path):
    file = open("./file/"+path+".txt", mode="w", encoding="utf-8")
    html = dicts[url]
    file.write(html)
    file.close()
    pass


def onError():
    print("发生错误！")
    pass

def gennenater():
    for key in  dicts:
        yield {key:dicts[key]}
    pass

if __name__ == '__main__':
    # sys.setrecursionlimit(1500)
    # print(gennenater())
    gen = gennenater()
    mlist =[]
    monkey.patch_all()
    # def joinall(greenlets, timeout=None, raise_error=False, count=None):/
    for item in gen :
        mlist.append(item)
    gevent.joinall(
        [
            gevent.spawn(accessNetworks, mlist[0]),
            gevent.spawn(accessNetworks, mlist[1]),
            gevent.spawn(accessNetworks, mlist[2]),
            gevent.spawn(accessNetworks, mlist[3]),
        ]
    )
    # print(dicts)
