def isPrimo(num):
    contatore,divisore = 0,2
    primo = False
    while divisore<=num/2 and contatore == 0:          
        if num%divisore == 0:
            contatore=+1
        divisore+=1
    
    if contatore == 0:
        primo = True
    else:
        primo = False
    return primo

numero = int(input("Inserisci un numero per vedere se è primo: "))

if isPrimo(numero) == True:
    print("Il numero è primo.")
else:
    print("Il numero non è primo")
