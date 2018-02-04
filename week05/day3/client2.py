import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345


def target(clientSocket):
    while True:
        reply = input("我：")
        clientSocket.send(reply.encode("utf-8"))
        msg = clientSocket.recv(1024).decode("utf-8")
        print("服务器：", msg)
        if reply == "拜拜":
            print("对方即将断开连接.....")
            time.sleep(2)
            break
    clientSocket.close()


if __name__ == '__main__':

    clientSocket = socket()
    clientSocket.connect((host, port))
    threading.Thread(target=target,args=(clientSocket,)).start()
    pass