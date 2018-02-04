import random

import requests
from lxml import etree

header_str = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/htmlapplication/xhtml+xmlapplication/xml;q=0.9image/webpimage/apng*/*;q=0.8',
    # 'Accept-Encoding': 'gzip deflate',
    'Accept-Language': 'zh-CNzh;q=0.9',

}
url = 'http://ip.filefab.com/index.php'

# //h1[@id='ipd']//span/text()
http_ip = [
    '58.251.209.123:8118',
    '61.135.217.7:80',
    '122.114.31.177:808',
    '61.155.164.111:3128',
    '61.155.164.109:3128',
    '61.155.164.110:3128',
    '60.191.134.165:9999',

    '58.244.52.31:8080',

    '221.226.20.158:8080',
    '110.73.52.222:8123',
    '61.155.164.107:3128',
    '27.40.129.200:61234',
]
https_ip = [
    '61.155.164.106:3128',
    '1.195.59.27:9797',
    '219.136.173.194:9797',
    '122.72.18.34:80',
    '58.87.89.234:3128',
    '114.215.18.7:3128',
    '114.215.108.183:3128',
    '121.43.178.58:3128',
    '122.72.18.35:80',
    '60.5.117.135:9999',
    '112.74.94.142:3128',
]
proxy_ip = {
    'http': random.choice(http_ip),
    'https': random.choice(https_ip)
}
print(proxy_ip)
res = requests.get(url=url, headers=header_str, proxies=proxy_ip)
html = etree.HTML(res.text)
ip = html.xpath("//h1[@id='ipd']//span/text()")
print(ip)
