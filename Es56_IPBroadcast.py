def controlloIP(ip, mask):
    continua = True
    
    while(continua == False):
        if(ip[32-mask:] == 0):
            print("L'ip è corretto. ")
            continua = True
        
    return ip


def ip_broad(ip,mask):
    ip[32-mask:] + '0' + ip[:]
    print("\n", ip)


def primo_ip(ip):
    ip[-3] + '1' + ip[:]
    print(ip)


#def ultimo_ip(ip):


def bin2dec(stringa):
    somma = 0
    for indice,carattere in enumerate(stringa[::-1]):
        somma += int(carattere) * (2**indice)
    return somma


def dec2bin(numero,nbit):
    bina = bin(int(numero))[2:]
    bina = "0" * (nbit-len(bina))+bina  
    return bina


def IP_dec2bin(IP_dec):
    bin = ""
    ip = IP_dec.split(".")
    for k in range(4):
        bin += ((dec2bin(int(ip[k]),8))) + "."
    return bin[:-1]


def IP_bin2dec(IP_bin):
    dec = ""
    ip = IP_bin.split(".")
    for k in range(4):
        dec += str(bin2dec(ip[k])) + "."
    return dec[:-1]


def main():
    stringa = "100"
    numero = 9
    IP_rete = input("Inserisci l'ip di rete. ")
    Sub_mask = int(input("Inserisci la subnet mask nel modo /n. "))
    IP_rete = controlloIP(IP_dec2bin(IP_rete), Sub_mask)
    ip_broad(IP_dec2bin(IP_rete), Sub_mask)
    primo_ip(IP_rete)

    print("/n",ip_broad)


if __name__ == "__main__":
    main()