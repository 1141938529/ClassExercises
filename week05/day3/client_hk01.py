import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345

machineID = "mine"

def SendMsg(clientSocket):
    while True:
        reply = input("")
        clientSocket.send((machineID+":"+reply).encode("utf-8"))


def RecvMsg(clientSocket):
    global machineID
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        if msg.startswith("hostID"):
            # 本机的端口值  str类型
            machineID = msg[6:]
            pass
        mlist =msg.split(":")
        if len(mlist)>1:
           print(mlist[1]+":"+mlist[0])


if __name__ == '__main__':

    clientSocket = socket()
    clientSocket.connect((host, port))
    threading.Thread(target=SendMsg,args=(clientSocket,)).start()
    threading.Thread(target=RecvMsg,args=(clientSocket,)).start()
    pass