alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', " "]

stringa = input("Inserisci una frase: ")
stringaMaiusc = stringa.upper()
n = int(input("Inserisci un numero per criptare o decriptare la frase: "))

def ricerca(alfabeto, c):
    ok = False
    k = 0
    while ok == False & k < len(alfabeto):
        if c == alfabeto[k]:
            ok = True
        else:
            k = k + 1
    return k

def criptare(stringa):
    nuova = ""
    y = 0
    for let in stringa:
        x = ricerca(alfabeto, let)
        if x <= 23:
            nuova = nuova + alfabeto[x + n]
        else:
            nuova = nuova + alfabeto[(x + n) % len(alfabeto)]
        y = y + 1
    return nuova

def decriptare(stringa, n):
    nuova = ""
    y = 0
    for let in stringa:
        x = ricerca(alfabeto, let)
        if x >= 2:
            nuova = nuova + alfabeto[x - n]
        else:
            nuova = nuova + alfabeto[(x + n) % len(alfabeto)]
        y = y + 1
    return nuova

cond = True
while cond == True:
    scelta = int(input("Inserisci 1 per criptare o 0 per decriptare: "))
    if scelta == 1 or scelta == 0:
        cond = False
    else:
        cond = True

if scelta == 1:
    crip = criptare(stringaMaiusc)
else:
    crip = decriptare(stringaMaiusc, n)

print(f"Stringa criptata: {crip}")


