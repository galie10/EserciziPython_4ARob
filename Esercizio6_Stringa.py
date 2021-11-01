stringa ="Ciao mi chiamo Marco"

print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

stringaNuova = stringa[1:19]
print(f"{stringaNuova}")
stringaNuova = stringa[0::2]
print(f"{stringaNuova}")
stringaNuova = stringa[::-1]
print(f"{stringaNuova}")
stringa = "Dizionario"
stringaNuova = stringa[0:2] + "?" + stringa[3:]
print(f"{stringaNuova}")


