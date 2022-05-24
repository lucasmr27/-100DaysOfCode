from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)


def poligono(lados, tamanho=100):
    tim.color(random.choice(colours))
    for _ in range(lados):
        tim.forward(tamanho)
        tim.right(-360/lados)


def andar_bebado(passos=200, distancia=25):
    tim.pensize(10)
    for _ in range(passos):
        tim.forward(distancia)
        # tim.color(random.choice(colours))
        tim.color((mudar_cor()))
        tim.right(random.choice([0, 90, -90, 180]))


def mudar_cor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def spirograph(x):
    for _ in range(x):
        tim.circle(50)
        tim.right(360 / x)
        tim.forward(10)
        tim.color(mudar_cor())


colours = ['lime', 'gold', 'red', 'blue', 'yellow', 'orange', 'purple', 'dark violet', 'deep pink', 'deep sky blue']
tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed('fastest')

tim.penup()
tim.right(90)
tim.forward(250)
tim.right(90)
tim.forward(250)
tim.right(180)

for y in range(10):
    for x in range(10):
        tim.dot(20, mudar_cor())
        tim.forward(50)
    tim.right(-90)
    tim.forward(50)
    tim.right(-90)
    tim.forward(500)
    tim.right(180)

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
