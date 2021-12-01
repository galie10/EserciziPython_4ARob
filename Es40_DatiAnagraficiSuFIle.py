nome = input("Inserisci il nome della persona. ")
cognome = input("Inserisci il cognome della persona. ")
data = input("Inserisci la data di nascita della persona. ")

dizionario = {"nome: ":nome, "cognome: ":cognome, "data: ":data}

f = open(".\dinic.txt", "w")
f.write(f"Il nome della persona è : " + dizionario["nome: "])
f.write(f"\nIl cognome della persona è : " + dizionario["cognome: "])
f.write(f"\nLa data di nascita della persona è: " + dizionario["data: "])
