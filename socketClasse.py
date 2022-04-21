import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.121",5000))

while True:
    stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(),("192.168.0.123",5000))
    stringa = s.recv(4096)
    print(stringa.decode())