import threading
from socketserver import ThreadingTCPServer, StreamRequestHandler

host = "127.0.0.1"
port = 12345

class myThreadrequestHandler(StreamRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)


    def handle(self):
        super().handle()
        threading.Thread(target=SendMsg,args=(self.request,self.client_address)).start()
        threading.Thread(target=RecvMsg,args=(self.request,self.client_address)).start()


def SendMsg(clientSocket,address):
    while True:
        reply = input(str(address[1])+":")
        clientSocket.send(reply.encode("utf-8"))
    pass
def RecvMsg(clientSocket,address):
    while True:
        msg = clientSocket.recv(1024).decode("utf-8")
        print(str(address[1])+":"+ msg)
    pass
if __name__ == '__main__':
    server = ThreadingTCPServer((host, port),myThreadrequestHandler)
    server.serve_forever()
    pass
