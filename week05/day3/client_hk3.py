import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345


def SendMsg(clientSocket):
    while True:
        reply = input("我：")
        clientSocket.send(reply.encode("utf-8"))

def RecvMsg(clientSocket):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        print( msg)


if __name__ == '__main__':

    clientSocket = socket()
    clientSocket.connect((host, port))
    threading.Thread(target=SendMsg,args=(clientSocket,)).start()
    threading.Thread(target=RecvMsg,args=(clientSocket,)).start()
    pass