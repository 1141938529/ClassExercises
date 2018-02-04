import time


def genernater():
    for i in range(10):
        yield i
        time.sleep(1)

def fibonacc(n):
    a= 0
    b= 1
    yield a
    for i in range(n):
        a,b = b,a+b
        time.sleep(1)
        yield a

if __name__ =="__main__":
    gen = fibonacc(10)
    # print(gen)
    # for item in gen:
    #     print(item)
    # pass
    while True:
        try:
            print(next(gen))
        except StopIteration:
            break