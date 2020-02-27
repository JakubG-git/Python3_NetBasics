import socket
def Main():
    host = socket.gethostname()
    port = 5002
    s = socket.socket()
    s.connect((host,port))
    msg = input("->>")
    while msg != 'q':
        s.send(msg.encode())
        print("Wysylanie" , msg)
        data = s.recv(1024).decode()
        print("Odebrano z serwera:" , str(data))
        msg = input("->")
    s.close()
if __name__ == "__main__":
    Main()