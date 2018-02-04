import requests
from lxml import etree
import time

url_login = 'https://passport.weibo.cn/sso/login'
url_web = 'https://weibo.cn/'

header_web = {
    'Host': 'weibo.cn',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}

header_login = {
    'Host': 'passport.weibo.cn',
    'Connection': 'keep-alive',
    'Origin': 'https://passport.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}
form = {
    'username': '18070493584',
    'password': '1141938529',
    'savestate': '1',
    'r': 'http://weibo.cn/',
    'ec': '0',
    'pagerefer': '',
    'entry': 'mweibo',
    'wentry': '',
    'loginfrom': '',
    'client_id': '',
    'code': '',
    'qq': '',
    'mainpageflag': '1',
    'hff': '',
    'hfp': '',
}
sess = requests.session()
res = sess.post(url=url_login, headers=header_login, data=form)
print(res.text)
for i in range(5):
    res = sess.get(url=url_web, headers=header_web)
    html = etree.HTML(res.content)
    url_web = "https://weibo.cn" + html.xpath("//div[@id='pagelist']//a[1]/@href")[0]
    post_list = html.xpath("//span[@class='ctt']/text()")
    print(post_list)
    time.sleep(4)
