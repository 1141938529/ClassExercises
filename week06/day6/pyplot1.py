import socket
host = "127.0.0.1"
port = 1234
if __name__ == '__main__':
    sereveSocket = socket.socket()
    sereveSocket.bind((host,port))
    sereveSocket.listen(100)
    clientsocket, clientAddress=sereveSocket.accept()
    replay = sereveSocket.recv(1000).decode("utf-8")
    print(replay)
