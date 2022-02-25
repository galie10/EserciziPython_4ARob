from turtle import Turtle,Screen
import random
tartaruga = Turtle()
sfondo = Screen()

class Stella():
    def __init__ (self, stella,dim):
        self.stella = []
        self.dim
        self.stella

    def draw(self):
        coordX = random.randint(-250,250)
        coordY = random.randint(-250,250)
        tartaruga.penup()
        tartaruga.goto(coordX,coordY)
        tartaruga.pendown()
        count = 0
        angle = 144
        while count <= 5:
            tartaruga.forward(100)
            tartaruga.right(angle)
            count += 1
        dim += 1
        if dim >= 50:
            return
        else:
            Stella.draw(self)

s1 = Stella()
s1.draw(Stella,0)
sfondo.exitonclick()