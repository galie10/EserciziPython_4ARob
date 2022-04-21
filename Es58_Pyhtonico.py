'''
lista = ["ciao", "d", "buongiorno"]

#NOOO
for i in range(len(lista)):
    print(lista[i])

#SII
for elem in lista:
    print(elem)

contatore = 0

#NOO
for elem in lista:
    print(contatore,elem)
    contatore = contatore + 1

#SII
for contatore,elem in enumerate(lista):
    print(contatore,elem)

'''

saluti = ["buongiorno", "ciao", "ehi"]
nomi = ["prof", "Luca", "tu"]

for saluto,nome in zip(saluti,nomi):
    #cicla su due liste in parallelo (solo se uguali)
    print(f"{saluto} {nome}")
