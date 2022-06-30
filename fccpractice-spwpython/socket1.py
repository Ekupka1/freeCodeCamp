#12 EX pfe - Makes a socket make a command and gather data (header and contents) and hacks a website

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr43.org', 80))
cmd = 'GET http://data.pr43.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send()

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()