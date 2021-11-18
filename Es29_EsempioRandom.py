import random 

giocatore1 = input("Inserisci il nome del giocatore 1: ")
giocatore2 = input("Inserisci il nome del giocatore 2: ")

lancio1 = random.randint(1, 6)
lancio2 = random.randint(1, 6)

if(lancio1 > lancio2):
    print(f"Ha vinto il giocatore {giocatore1} con il numero {lancio1}")
elif lancio2 > lancio1: print(f"Ha vinto il giocatore {giocatore2} con il numero {lancio2}")
else: print("PAREGGIO")

