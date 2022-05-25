from turtle import Turtle, Screen

tin = Turtle()
screen = Screen()


def move_up():
    tin.setheading(90)
    tin.forward(18)


def move_down():
    tin.setheading(270)
    tin.forward(18)


def move_left():
    tin.setheading(180)
    tin.forward(18)


def move_right():
    tin.setheading(0)
    tin.forward(18)


screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()