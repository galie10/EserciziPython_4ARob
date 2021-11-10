import math

x1 = int(input("Inserisci la coordinata della x: "))
x2 = int(input("Inserisci la coordinata della seconda x: "))
y1 = int(input("Inserisci la coordinata della y: "))
y2 = int(input("Inserisci la coordinata della seconda y: "))

tupla = (x1, x2, y1, y2)

distanza = math.sqrt((tupla[0] - tupla[1]) **2 + (tupla[2] - tupla[3]) ** 2)

print(distanza)