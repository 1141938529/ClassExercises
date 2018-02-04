
import gevent
import sys
from gevent import monkey
import requests
from gevent.pool import Pool

dicts = {"http://www.baidu.com/": "百度",
         "http://www.qq.com/":"腾讯",
         "http://www.sina.com.cn/":"新浪",
         "http://www.youtube.com/": "谷歌",
         }


def accessNetworks(netDicts):
    try:
        keys =netDicts.keys()
        for key in keys:
            url = key
        res = requests.get(key)
        html = res.text
    except requests.exceptions.ConnectionError:
        html ="获取超时"

    dicts[key] = html
    print(key + " is ok")

        # saveFile(key,netDicts[key])


def saveFile(url, path):
    file = open("./file/"+path+".txt", mode="w", encoding="utf-8")
    html = dicts[url]
    file.write(html)
    file.close()
    pass


def onError(err, str):
    print(str)
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
