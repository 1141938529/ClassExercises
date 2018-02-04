import requests


def requestPost():
    parse = {"name": "zhangsan", "age": 20}
    json = '[{"name":"嘟嘟","haircolor":"花色","like_foods":["可乐","啤酒"]},' \
           '{"name":"摩卡","haircolor":"纯白色","like_foods":["狗粮","面包","小花生"]},' \
           '{"name":"苏拉","haircolor":"灰色","like_foods":["junkfood","辣条"]},' \
           '{"name":"思诺","haircolor":"暗黑色","like_foods":["米饭","面条"]},' \
           '{"name":"小煤球","haircolor":"碎花色","like_foods":["鱼","老鼠"]}]'
    responds = requests.post("https://httpbin.org/post", json=json)
    print(responds.text)


def requestDownLoad():
    reqs = requests.get(
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1508843237955&di=c9b402e241850de06dade23274e90d2c&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fzhidao%2Fwh%253D600%252C800%2Fsign%3D849abd67b7003af34defd466051aea64%2F060828381f30e9240ad0c15f4d086e061d95f76c.jpg")
    mbytes = reqs.content
    with open("./res/dog.jpg", "wb") as mfile:
        mfile.write(mbytes)
        mfile.close()
    print("下载成功")


def postFile():
    mfile = open("./res/dog.jpg", "rb")
    # mfile.close()
    reqs = requests.post("https://httpbin.org/post", files={"mfile": mfile})
    print(reqs.text)


if __name__ == '__main__':
    # requestPost()
    # requestDownLoad()
    postFile()
    pass
