import gevent


def func1():
    gevent.sleep(0)
    print("红军不怕远征难")
    gevent.sleep(4)
    print("金山水拍云崖暖")


def func2():
    gevent.sleep(1)
    print("万水千山只等闲")
    gevent.sleep(4)
    print("大渡桥横铁索寒")


def func3():
    gevent.sleep(2)
    print("五岭逶迤腾细浪")
    gevent.sleep(4)
    print("更喜眠山千里雪")


def func4():
    gevent.sleep(3)
    print("乌蒙磅礴走泥丸")
    gevent.sleep(4)
    print("三军过后尽开颜")


if __name__ == "__main__":
    # def joinall(greenlets, timeout=None, raise_error=False, count=None):
    gevent.joinall(
        [gevent.spawn(func1),
         gevent.spawn(func2),
         gevent.spawn(func3),
         gevent.spawn(func4)]

    )
    pass
