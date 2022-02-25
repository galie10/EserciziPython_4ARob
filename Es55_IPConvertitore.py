#1.Chiedere ip di rete
#2.Chiedere all'utente la subnet mask
#3.Controllo Ip di rete

def bin2dec(stringa):
    somma = 0
    for indice,carattere in enumerate(stringa[::-1]):
        somma += int(carattere) * (2**indice)
    return somma

def dec2bin(numero,nbit):
    bina = bin(int(numero))[2:]
    bina = "0" * (nbit-len(bina)) + bina  
    return bina

def IP_dec2bin(IP_dec):
    bin = ""
    ip = IP_dec.split(".")
    for k in range(4):
        bin += ((dec2bin(int(ip[k]),8)))
    return bin

def IP_bin2dec(IP_bin):
    dec = ""
    for k in range(0,32,8):
        dec += str(bin2dec(IP_bin[k:k+8])) + "."
    return dec[:-1]

def ControlloIp(Ip_rete,nbit):
    Ip_reteBinario = IP_dec2bin(Ip_rete)
    if Ip_reteBinario[nbit:] == (32-nbit) * "0":
        return True
    else:
        return False

def IpBroadcast(Ip_rete,nbit):
    Ip_reteBinario = IP_dec2bin(Ip_rete)
    Ip_reteBroadcast = Ip_reteBinario[:nbit] + (32-nbit) * "1"
    return IP_bin2dec(Ip_reteBroadcast)    

def PrimoIp(Ip_rete,nbit):
    Ip_reteBinario = IP_dec2bin(Ip_rete)
    Ip_retePrimo = Ip_reteBinario[:nbit] + (32-nbit-1) * "0" + "1"
    return IP_bin2dec(Ip_retePrimo)  

def UltimoIp(IpBroadcast):
    IpBinario = ""
    IpBinario = IP_dec2bin(IpBroadcast)
    Ip_ultimo = IpBinario[:-1] + "0"
    return IP_bin2dec(Ip_ultimo)

def main():
    IP_rete = input("Inserisci un ip di rete:")
    nbit = int(input("Inserisci numero bit di rete (Esmepio: 24):"))
    ip_Broadcast = IpBroadcast(IP_rete,nbit)
    print(f"Broadcast: {ip_Broadcast}")
    print(f"Primo indirizzo:{PrimoIp(IP_rete,nbit)}")
    print(f"Ultimo indirizzo:{UltimoIp(ip_Broadcast)}")

if __name__ == "__main__":
    main()