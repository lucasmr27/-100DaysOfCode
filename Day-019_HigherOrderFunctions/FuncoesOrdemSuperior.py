from turtle import Turtle, Screen

tin = Turtle()
screen = Screen()


def move_forwards():
    tin.forward(18)


def move_backwards():
    tin.forward(-18)


def turn_left():
    new_heading = tin.heading() + 10
    tin.setheading(new_heading)


def turn_right():
    new_heading = tin.heading() - 10
    tin.setheading(new_heading)


def clear():
    tin.clear()
    tin.penup()
    tin.home()
    tin.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(clear, "c")
screen.exitonclick()
