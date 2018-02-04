import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345


def msgmsg():
    while True:
        data = clientSocket.recv(1024).decode("utf-8")
        print("客户端：", data)
        msg = input("我:")
        clientSocket.send(msg.encode("utf-8"))
        if data == "拜拜":
            print("对方即将断开连接.....")
            time.sleep(2)
            break

def SendMsg(clientSocket):
    while True:
        reply = input("我：")
        clientSocket.send(reply.encode("utf-8"))

def RecvMsg(clientSocket):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        print("")
        print("客户端：", msg)

if __name__ == '__main__':
    # 创建 服务端的socket
    serverScoket = socket()

    # 绑定到端口
    serverScoket.bind((host, port))

    # 服务端开始监听
    serverScoket.listen(100)

    # accept() -> (socketobject, address info)
    clientSocket, clientAddress = serverScoket.accept()

    # msgmsg()
    threading.Thread(target=SendMsg,args=(clientSocket,)).start()
    threading.Thread(target=RecvMsg,args=(clientSocket,)).start()
    pass
