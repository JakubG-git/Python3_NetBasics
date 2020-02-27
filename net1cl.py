import sys
import socket
PORT = 5000

TCP_IP = '127.0.0.1'

BUF_SIZE = 1024
s = socket.socket()
s.connect((TCP_IP, PORT))
msg = input("-> ")
while msg != 'q':
    s.send(msg.encode())
    data = s.recv(1024)
    print ("Recived from server" ,str(data))
    msg = input("->")
s.close()
