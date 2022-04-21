import socket
#                      IPv4             UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.123",5000)) #SOLO SUI SERVER

while True:
    dati, ind_client = s.recvfrom(4096) #4096 è la dimensione in byte
    print(f"{dati.decode()} ricevuti da {ind_client}")