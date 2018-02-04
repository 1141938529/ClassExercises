import gevent

questionDict = {"我们是什么？": "浏览器",
                "我们要什么？": "速度",
                "什么时候要？": "现在" }
def google(question):
    gevent.sleep(1)
    print("google："+questionDict[question])
    pass
def firefox(question):
    gevent.sleep(1)
    print("firefox：" + questionDict[question])
    pass
def oppeng(question):
    gevent.sleep(1)
    print("oppeng：" + questionDict[question])
    pass
def IE(question):
    gevent.sleep(5)
    print("IE：" + questionDict[question])
    pass



if __name__ == '__main__':
    keys = list(questionDict.keys())
    # def joinall(greenlets, timeout=None, raise_error=False, count=None)
    for item in keys:
        print(item)
        gevent.joinall([
            gevent.spawn(google, item),
            gevent.spawn(firefox, item),
            gevent.spawn(oppeng, item),
            gevent.spawn(IE, item),
                        ],timeout=3)

    pass
