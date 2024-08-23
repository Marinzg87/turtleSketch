import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()


def forward():
    """Function will move forward the object by 10"""
    return tim.forward(10)


def right():
    pass


def left():
    pass


def backward():
    pass


def clear():
    """Function will clear the screen"""
    return t.clear()



screen.listen()
screen.onkey(key="c", fun=clear)
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.exitonclick()