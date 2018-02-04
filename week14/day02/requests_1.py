import requests
from lxml import etree

# 请求头
header_str = {
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
url_str = 'http://sell.gandianli.com/list.php?catid=3234&page=1'
res = requests.get(url=url_str, headers=header_str)
html = etree.HTML(res.text)
result = html.xpath("//ul[@class='extension_ul']/li/div[1]/a[1]/@title")
imgs = html.xpath("//ul[@class='extension_ul']/li/div[@class='img']//img/@src")
price = html.xpath("//ul[@class='extension_ul']/li/div[@class='extension_right']/span/text()")
adress = html.xpath("//ul[@class='extension_ul']/li/div[@class='extension_right']/p[1]/a/text()")
for p in imgs:
    if p.strip():
        img = requests.get(url=p,headers=header_str).content
        filename = p.split('/')[-1]
        with open('D://PyDownload//png//'+filename,'wb') as f:
            f.write(img)
        