import threading
from socketserver import TCPServer, BaseRequestHandler

host = "127.0.0.1"
port = 12345

class myRequestHandle(BaseRequestHandler):
    # request为客户端socket 对象；client_address为客户端地址；server 为服务器TCPServer对象
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def setup(self):
        print("setup")
        print("服务器已与%s建立连接"%(self.client_address[1]))
        super().setup()

    def handle(self):
        threading.Thread(target=SendMsg,args=(self.request,)).start()
        threading.Thread(target=RecvMsg,args=(self.request,)).start()
        pass

    def finish(self):
        print("finish")
        self.request.close()
        super().finish()


def SendMsg(clientSocket):
    while True:
        reply = input("我：")
        clientSocket.send(reply.encode("utf-8"))
    pass
def RecvMsg(clientSocket):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        print("客户端：", msg)
    pass

if __name__ == '__main__':
    server = TCPServer((host,port),myRequestHandle)
    server.serve_forever()
    pass