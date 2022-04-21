import turtle

wn = turtle.Screen()
f = open("./miofile.txt","r")
lista = [" "]

for i in range(10):
    for i in range(2):
        turtle. forward(100)
        lista[0] = "forward"
        f.write(lista[0] + "\n")
        turtle. right(60)
        f.write(lista.append("60") + "\n")
        turtle. forward(100)
        f.write(lista.append("100") + "\n")
        turtle. right(120)
        f.write(lista.append("120") + "\n")
    turtle. right(36)
    f.write(lista.append("36") + "\n")

turtle.exitonclick()