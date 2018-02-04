import requests
from lxml import etree
import time

# 请求头
header_str = {
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
name_list = []
url_str = 'http://www.moko.cc/channels/post/23/1.html'
url_base = 'http://www.moko.cc'


def download_img(name, model_url):
    resp = requests.get(url=model_url, headers=header_str)
    html0 = etree.HTML(resp.text)
    img_url_list = html0.xpath("//p[@class='picBox']/img/@src2")
    for i in range(len(img_url_list)):
        imgs = requests.get(url=img_url_list[i], headers=header_str).content
        with open("D://PyDownload//png//" + name + str(i) + '.png', 'wb') as f:
            f.write(imgs)


res = requests.get(url=url_str, headers=header_str)
html = etree.HTML(res.text)
ul_list = html.xpath("//ul[@class='post small-post']")
for ul in ul_list:
    name = ul.xpath(".//a[@class='nickname']/text()")[0]
    model_url = url_base + ul.xpath(".//div[@class='cover']/a[1]/@href")[0]
    download_img(name, model_url)
    time.sleep(5)
print('main over')
