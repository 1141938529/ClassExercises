import threading
from socket import socket

import time

host = "127.0.0.1"
port = 12345

mdicts ={}
mlock = threading.Lock()
def sendAll(msg):
    for key in mdicts:
        mdicts[key].send((msg+":"+str(key)).encode("utf-8"))


def RecvMsg(clientSocket,clientAddress):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        # with mlock:
        #     if msg.count(":")>1:
        #         msglist = msg.split(":")
        #         mdicts[msglist[1]].send(msglist[0].encode("utf-8"))
        #     else:
        #         sendAll(msg)
        #         print(msg)
        sendAll(msg)
        print(msg)
    pass


if __name__ == '__main__':
    # 创建 服务端的socket
    serverScoket = socket()
    # 绑定到端口
    serverScoket.bind((host, port))

    # 服务端开始监听
    serverScoket.listen(100)

    # accept() -> (socketobject, address info)
    while True:
        clientSocket, clientAddress = serverScoket.accept()
        mdicts[clientAddress[1]] = clientSocket
        print("欢迎%d加入群聊....."%(clientAddress[1]))
        with mlock:
            sendAll("欢迎%d加入群聊....."%(clientAddress[1]))
        clientSocket.send(("hostID"+str(clientAddress[1])).encode("utf-8"))
        # msgmsg()

        threading.Thread(target=RecvMsg,args=(clientSocket,clientAddress)).start()

    pass

# 发送消息给所有人



