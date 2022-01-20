from turtle import Turtle, Screen
import random

tartaruga = Turtle()
sfondo = Screen()
tartaruga.speed(5)

def stella(countRepeat):
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
    countRepeat += 1
    if countRepeat >= 50:
        return
    else:
        stella(countRepeat)

countRepeat = 0
stella(countRepeat)
sfondo.exitonclick()