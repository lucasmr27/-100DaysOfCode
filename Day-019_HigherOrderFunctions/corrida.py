from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="With turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    posicao = turtle_index * 30 - 75
    tim.goto(x=-230, y=posicao)


screen.exitonclick()
