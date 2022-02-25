from operator import truediv
from turtle import Turtle,Screen
tartaruga = Turtle()
sfondo = Screen()

class Quadrato():
    def __init__ (self):
        self.lato = 4
        self.ok = False
        self.punto = int(input("Inserisci un punto da confrontare. "))

    def area(self):
        return self.lato * self.lato
    
    def perimetro(self):
        return self.lato * 4 
         
    def isEsterno(self,punto,ok):
        if(punto <= self.area):
            ok = True
        else: 
            ok = False
        return ok
    
    def draw(self):
        cordX = 0
        cordY = 0
        tartaruga.penup()
        tartaruga.goto(cordX, cordY)
        for _ in range(4):
            tartaruga.forward(self.lato)
            tartaruga.right(90)
def main():
    l1 = Quadrato()
    l1.area()
    l1.perimetro()
    l1.draw()
    l1.isEsterno

if __name__ == "__main__":
    main()