import multiprocessing

# 发送数据 conn 是发送端
def sendData(event,conn):
    while True:
        # msg = input("我：")
        conn.send("hello")
        event.set()

        event.wait()
        recvmsg = conn.recv()
        print("recv："+recvmsg)
    conn.close()
    pass

# 发送数据 conn 是接收端
def recvData(event,conn):
    while True:
        event.wait()
        msg = conn.recv()
        print("send:"+msg)
        # msg = input("我：")
        conn.send("fuck")
        event.set()
    conn.close()
    pass


if __name__ == "__main__":
    event = multiprocessing.Event()
    mypipe = multiprocessing.Pipe(duplex=True)
    multiprocessing.Process(target=sendData, args=(event,mypipe[1])).start()
    multiprocessing.Process(target=recvData, args=(event,mypipe[0])).start()
    pass
