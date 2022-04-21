scelta = int(input("Inserisci l'operazione che vuoi effettuare: "))

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

if scelta == 0:
   ris = n1 + n2
elif scelta == 1:
    if n1 > n2:
        ris = n1 - n2
    else: ris = n2 - n1
elif scelta == 3:
    ris = n1 * n2
else:
    if n1 > n2:
        ris = n1 / n2
    else: ris = n2 / n1

print(ris)

