from turtle import Turtle, Screen
import time


def move_right(cobra):
    new_position = [(cobra[0][0]+20, cobra[0][1])]
    cobra = new_position + cobra[0:-1]
    return cobra


def move_up(cobra):
    new_position = [(cobra[0][0], cobra[0][1]+20)]
    cobra = new_position + cobra[0:-1]
    return cobra


def move_left(cobra):
    new_position = [(cobra[0][0]-20, cobra[0][1])]
    cobra = new_position + cobra[0:-1]
    return cobra


def move_down(cobra):
    new_position = [(cobra[0][0], cobra[0][1]-20)]
    cobra = new_position + cobra[0:-1]
    return cobra


def move(snake, positions):
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
    positions = move_right(positions)
    move(snake, positions)
for _ in range(10):
    time.sleep(0.5)
    positions = move_up(positions)
    move(snake, positions)


screen.exitonclick()
