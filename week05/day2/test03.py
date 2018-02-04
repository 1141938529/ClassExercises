import requests


def downloadLittleFiles():
    respond = requests.get("http://127.0.0.1/imgs/dog.jpg")
    with open("./res/dog2.jpg", mode="wb") as mfile:
        mfile.write(respond.content)
    print("下载成功")


if __name__ == '__main__':
    # downloadLittleFiles()
    rsp = requests.get("http://127.0.0.1/imgs/meinv.jpg")
    with open("./res/meinv2.jpg",mode='wb') as mfile:
        for buffer in rsp:
            print(type(buffer))
            mfile.write(buffer)
    print("下载成功")
    pass