import requests
from lxml import etree
import json
import time

url_str = "https://www.douyu.com/directory/all"
url_base = "https://www.douyu.com/gapi/rkc/directory/0_0/"
header_str = {
    'Connection': 'keep-alive',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    # 'Referer': 'https://www.douyu.com/directory/all',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
}
res = requests.get(url=url_str, headers=header_str)
html = etree.HTML(res.text)

# 第一页的数据
anchor_list = html.xpath("//ul[@id='live-list-contentbox']//span[@class='dy-name ellipsis fl']/text()"
                         "|//ul[@id='live-list-contentbox']//span[@class='dy-num fr']/text()")
for i in range(0, len(anchor_list), 2):
    with open('D://PyDownload//主播名单.txt', 'a',encoding='utf8') as f:
        f.write(anchor_list[i] + ' | ' + anchor_list[i + 1] + '\n')

index = 1
while True:
    time.sleep(2)
    index += 1
    url = url_base + str(index)
    html0 = requests.get(url=url, headers=header_str).text
    info = json.loads(html0)
    page_anchor_list = info['data']['rl']
    for anchor in page_anchor_list:
        with open('D://PyDownload//主播名单.txt', 'a', encoding='utf8') as f:
            f.write(str(anchor['nn']) + ' | ' + str(anchor['ol']) + '\n')
    if index == 10:
        break
# https://www.douyu.com/gapi/rkc/directory/0_0/2
