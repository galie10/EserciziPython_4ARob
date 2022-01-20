na = (int)(input("Inserisci il numero di alunni che si vuole inserire. "))
name = ""
f = open("nomeast.txt", "w")

for k in range(0,na):
    nome = input("Inserisci il nome dell'alunno ")
    lung = {len(nome)}
    name = nome[:1] + (lung-1) * "*"
    f.write(name)
    

