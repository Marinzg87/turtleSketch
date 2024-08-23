import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()


def forward():
    """Function will move forward the object by 10"""
    tim.forward(10)


def right():
    """Function will turn right the object by 15 degree"""
    tim.right(15)


def left():
    """Function will turn left the object by 15 degree"""
    tim.left(15)


def backward():
    """Function will move backward the object by 10"""
    tim.backward(10)


def clear():
    """Function will clear the screen and set the object position to 0, 0"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
