import requests
from lxml import etree

sess = requests.session()
url_str = 'https://www.zhihu.com/'
url_login = 'https://www.zhihu.com/signin'

headers_login = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Origin': 'https://www.zhihu.com',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryr4n1lPwYedLXqB4G',
    'accept': 'application/json, text/plain, */*',
    'X-UDID': 'ALBgrk5Y5wyPTsBF_ArRTEIu4d7lygWjSTg=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'X-Xsrftoken': 'c36da997-3209-4cde-8c70-9ccdda939b6a',
    'Referer': 'https://www.zhihu.com/signin',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

form_info = {
    'Content-Disposition: form-data; name="client_id"': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
    'Content-Disposition: form-data; name="grant_type"': 'password',
    'Content-Disposition: form-data; name="timestamp"': '1514463724528',
    'Content-Disposition: form-data; name="source"': 'com.zhihu.web',
    'Content-Disposition: form-data; name="signature"': '066ce609c7c0b798fbc997872c23d10db7b1a4c4',
    'Content-Disposition: form-data; name="username"': '+8618070493584',
    'Content-Disposition: form-data; name="password"': '5775211314',
    'Content-Disposition: form-data; name="captcha"': '',
    'Content-Disposition: form-data; name="lang"': 'cn',
    'Content-Disposition: form-data; name="ref_source"': 'other_undefined',
    'Content-Disposition: form-data; name="utm_source"': 'baidu',
}

headers1 = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',

}
res_login = sess.post(url=url_login, data=form_info, headers=headers_login)

res_web = sess.get(url=url_str,headers=headers1)
html = etree.HTML(res_web.text)
title_list = html.xpath("//h2[@class='ContentItem-title']//text()")
print(title_list)