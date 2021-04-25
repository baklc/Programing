from socket import *
serverSock=socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',8888))
serverSock.listen(1)
while True:
    clientSock, addr = serverSock.accept()
    print("--connected--",addr)
    while True:
        msg=clientSock.recv(1024).decode('utf-8')
        if msg=='0':
            print("on")
        elif msg=='1':
            print("off")
        else:
            print("--disconnected--")
            break
    clientSock.close()