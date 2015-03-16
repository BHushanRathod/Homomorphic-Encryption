import socket
import os
import select
import sys


HOST = '127.0.0.1'
PORT = 8080

p,q1,q2=map(int,raw_input("enter p,q1,q2").split())
r1,r2=map(int,raw_input("enter r1,r2").split()) 
b1,b2=map(int,raw_input("enter b1,b2").split())

b = b1^b2
print "b = ", b
bx = b1&b2
print "b = ", bx
c1 = (int(p) * int(q1)) + (2 * int (r1)) + int(b1)
print c1
c2 = (int(p) * int(q2)) + (2 * int(r2)) + int(b2)
print c2
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

print 'Connected to remote host'

s.send(str(c1)+":"+str(c2))

while True:

    r = s.recv(4098)
    C=r.split(":")[0]
    Cmult=r.split(":")[1]
    print "C =", C
    print "Cmultiplication = ", Cmult
    Noise1 = int(C) % p
    Noise2 = int(Cmult) % p
    print "C % p : ", Noise1
    print "Cmult % p : ", Noise2

    if Noise1 % 2 == 0:
        print "Expected : even. Noise = ", Noise1
    else:
        print "Expected : odd. Noise = ", Noise1
    print ""

    if Noise2 % 2 == 0:
        print "Expected : even. Noise = ", Noise2
    else:
        print "Expected : odd. Noise = ", Noise2

s.close()


