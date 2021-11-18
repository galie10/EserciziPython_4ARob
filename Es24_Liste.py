lista = [15, 21, 51, 4]
max = 0
k = 0

for parola in lista:
    if lista[k] > max:
        max = lista[k]
        k = k + 1

print(max)