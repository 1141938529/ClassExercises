from urllib import request
from urllib.request import Request


def urllibrequest():
    respond = request.urlopen("https://httpbin.org/get")
    # print(type(respond),respond)
    html = respond.read().decode("utf-8")
    print(html)


if __name__ == '__main__':
    # urllibrequest()
    request.urlretrieve("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2302918630,1086443006&fm=27&gp=0.jpg","./res/meinv.jpg")
    print("下载成功")
    pass
