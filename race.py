import turtle as t
from turtle import Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race?"
                                   " Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
pos_x = -230
pos_y = -140

for _ in range(len(colors)):
    turtle = t.Turtle("turtle")
    turtle.color(colors[_])
    turtle.penup()
    turtle.goto(x=pos_x, y=pos_y)
    turtles.append(turtle)
    pos_y += 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is a winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is a winner!")
        random_distance = random.randint(1, 20)
        turtle.forward(random_distance)

screen.exitonclick()
