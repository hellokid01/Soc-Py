from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",10000))
print "UDP server started..."
while True:
    data, addr = s.recvfrom(1000)
resp = "Get off my lawn!"
s.sendto(resp,addr)