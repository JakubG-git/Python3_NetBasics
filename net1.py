import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),60))
s.listen(1)
con , addr = s.accept()
print('Adres IP', addr)
while True:
    data = con.recv(1024)
    if not data:
        break
    print ("Dane odebrane od uzytkownika:" , str(data))
    data = str(data).upper()
    print ("Wysylanie" , str(data))
    con.send(data)
con.close

