from socket import socket

import time

host = "127.0.0.1"
port = 12345
if __name__ == '__main__':
    # 创建 服务端的socket
    serverScoket = socket()

    # 绑定到端口
    serverScoket.bind((host, port))

    # 服务端开始监听
    serverScoket.listen(100)

    # accept() -> (socketobject, address info)
    clientSocket, clientAddress = serverScoket.accept()

    while True:
        data = clientSocket.recv(1024).decode("utf-8")
        print("客户端：", data)
        msg = input("我:")
        clientSocket.send(msg.encode("utf-8"))
        if data == "拜拜":
            print("对方即将断开连接.....")
            time.sleep(2)
            break

    clientSocket.close()
    print("已断开连接。")
    time.sleep(3)
    pass
