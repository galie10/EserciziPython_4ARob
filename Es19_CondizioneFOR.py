classi = ["4arob", "3arob", "5brob", "4achi", "3ainf"]
indirizzi = {"rob":"Smart-Robot","chi":"Chimica", 
                "inf":"Informatica"}

indice = 0
for indice, classe in enumerate(classi): #il ciclo avviene simultaneamente sulla posizione e sull'elemento con enumerate, solo se indice parte da 0
    indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice} nella lista: ")
    print(f"la classe {classe} è dell'indirizzo {indirizzo}", end="\n\n")