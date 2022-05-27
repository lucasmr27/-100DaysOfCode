from turtle import Turtle, Screen
import time


def move_right():
    global positions
    new_position = [(positions[0][0]+20, positions[0][1])]
    positions = new_position + positions[0:-1]


def move_left():
    global positions
    new_position = [(positions[0][0]-20, positions[0][1])]
    positions = new_position + positions[0:-1]


def move_up():
    global positions
    new_position = [(positions[0][0], positions[0][1]+20)]
    positions = new_position + positions[0:-1]


def move_down():
    global positions
    new_position = [(positions[0][0], positions[0][1]-20)]
    positions = new_position + positions[0:-1]


def move(positions):
    global snake
    for parte in range(len(snake)):
        snake[parte].goto(positions[parte])


screen = Screen()
screen.bgcolor("black")
positions = [(20, 0), (0, 0), (-20, 0), (-40, 0), (-60, 0)]
snake = []
for body in range(len(positions)):
    snake.append(Turtle("square"))
    snake[body].penup()
    snake[body].speed("fastest")
    snake[body].color("black", "gray")
    snake[body].goto(positions[body])

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# while True:

for _ in range(10):
    time.sleep(0.5)
    move_right()
    move(positions)
for _ in range(10):
    time.sleep(0.5)
    move_up()
    move(positions)


screen.exitonclick()
