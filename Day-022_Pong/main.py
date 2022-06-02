from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
computer = Paddle()
screen.update()


screen.listen()

screen.onkey(computer.go_up(), "up")
screen.onkey(computer.go_down(), "up")
screen.exitonclick()
