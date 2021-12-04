n = (int)(input("Inserisci un numero: "))
k = 1
numeri = 1000
lista = [(2**k) for k in range(1,numeri) if 2**k < n] 
print(lista)

