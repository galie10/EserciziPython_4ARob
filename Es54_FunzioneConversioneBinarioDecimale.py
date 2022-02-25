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
    IP_dec = "192.168.163.0"
    IP_bin = "10101010.10101010.10101010.10101010"
    print(f"binario = {stringa}, decimale = {bin2dec(stringa)}")
    print(f"IP da binario a decimale {IP_bin2dec(IP_bin)}")
    print(IP_dec2bin(IP_dec))

if __name__ == "__main__":
    main()