from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

screen.listen()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def counter_clockwise():
    tim.setheading(tim.heading() + 10)

def clockwise():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeypress(key='W', fun=forward)
screen.onkeypress(key='S', fun=backward)
screen.onkey(key='A', fun=counter_clockwise)
screen.onkey(key='D', fun=clockwise)
screen.onkeypress(key='C', fun=clear)










screen.exitonclick()