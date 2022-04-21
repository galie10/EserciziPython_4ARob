str = ("Luca", "Babbo", "Nati", "Invincibile")

lung = 0
parolapiulunga = " "

for parola in str:
    if len(parola) > lung :
        lung = len(parola)
        parolapiulunga = parola

print(parolapiulunga)