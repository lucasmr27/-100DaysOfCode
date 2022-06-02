from turtle import Turtle, Screen
from paddle import Paddle



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.update()

screen.listen()

game_is_on = True
while game_is_on:
    screen.onkey(r_paddle.go_up, key="w")
    screen.onkey(r_paddle.go_down, key="s")
    screen.onkey(l_paddle.go_up, key="Up")
    screen.onkey(l_paddle.go_down, key="Down")
    screen.update()

screen.exitonclick()
