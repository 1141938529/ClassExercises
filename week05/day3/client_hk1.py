import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345


def SendMsg(clientSocket):
    while True:
        reply = eval(input("请输入回复的人："))
        msg = input("请输入回复内容：")
        clientSocket.send({reply:msg}.encode("utf-8"))

def RecvMsg(clientSocket):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        print( msg)


if __name__ == '__main__':

    clientSocket = socket()
    clientSocket.bind((host, 1234))
    clientSocket.connect((host, port))
    threading.Thread(target=SendMsg,args=(clientSocket,)).start()
    threading.Thread(target=RecvMsg,args=(clientSocket,)).start()
    pass