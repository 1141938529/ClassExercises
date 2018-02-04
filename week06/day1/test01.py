import re
import requests
# ·爬取网易主页上的所有子链接
# <a target="_blank" href="http://view.news.qq.com/original/intouchtoday/n4060.html">
# 电竞选手直播时恐吓女友：家暴不只是“打老婆”</a>
reUrl = '<a .*href="(http.+?)".*>.*</a>'
reUrl = re.compile(reUrl)
# "<a .*href=\"(http.+?)\".*>"
if __name__ == '__main__':
    html = requests.get("http://www.qq.com/").text
    reslist = re.findall(reUrl,html)
    for url in reslist:
        print(url)
    pass
