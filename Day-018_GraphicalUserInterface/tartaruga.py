from turtle import Turtle, Screen
import random


def poligono(lados, tamanho=100):
    tim.color(random.choice(colours))
    for _ in range(lados):
        tim.forward(tamanho)
        tim.right(-360/lados)


def andar_bebado(passos=100, distancia=25):
    for _ in range(passos):
        tim.forward(distancia)
        tim.color(random.choice(colours))
        tim.right(random.choice([0, 90, -90, 180]))


colours = ['lime', 'gold', 'red', 'blue', 'yellow', 'orange', 'purple', 'dark violet', 'deep pink', 'deep sky blue']
tim = Turtle()
tim.shape("turtle")
tim.color("red")

andar_bebado()
# for lado in range(3, 10):
#     poligono(lado)
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

screen = Screen()
screen.exitonclick()
