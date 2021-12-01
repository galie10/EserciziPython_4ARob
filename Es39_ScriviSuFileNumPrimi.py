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

cento = 100

for numero in range(2,cento):
    isPrimo(numero)
    

    if isPrimo(numero) == True:
        f = open(".\elsa.txt", "w")
        f.write(numero)
        f.write("\n")