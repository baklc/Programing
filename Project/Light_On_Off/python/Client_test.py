from socket import *
while True:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('server ip', 'port')) # server ip ,ex: 192.168.123.134 // port ,ex 8888, port must be integer
    print("connect complete")
    while True:
        a = str(input("send data : "))
        if a=="exit()":
            clientSock.send("exit".encode('utf-8'))
            break
        else:
            clientSock.send(a.encode('utf-8'))
            print("Done")
    clientSock.close()