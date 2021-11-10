nome = input("Inserisci il nome: ")

n = 1
k = 2

lung = {len(nome)}

for lung in nome:
    nome = nome[:n] + "*" + nome[k:]
    k = k + 1
    n = n + 1

print(nome)

