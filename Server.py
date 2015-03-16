
import socket
import os
import select
import sys


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

PORT = 8080
HOST = '127.0.0.1'
RECV_BUFFER = 4098

server_socket.bind((HOST, PORT))
server_socket.listen(100)

while True:
    c, ad = server_socket.accept()
    
    r = c.recv(4098)
    c1=r.split(":")[0]
    c2=r.split(":")[1]
    print c1
    print c2
    C = int(c1) + int(c2)
    Cmul = int(c1) * int(c2)
    print "c1 + c2 = ", C
    print "c1 * c2 = ", Cmul
    c.send(str(C)+":"+str(Cmul))
    
server_socket.close()


