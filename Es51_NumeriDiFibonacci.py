serie = []

def fibonacci(ultimo,penultimo,limite):
    num = ultimo + penultimo
    
    if num < limite:
        serie.append(num)
        fibonacci(num,ultimo, limite)
    
    return serie      

limite = int(input("Inserisci il numero massimo oltre cui i valori della serie non vengono stampati: "))
print(fibonacci(1,1,limite))