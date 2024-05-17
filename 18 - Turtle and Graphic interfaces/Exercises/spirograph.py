from turtle import Turtle, Screen, colormode
from random import randint, choice

colormode(255)


tim = Turtle()
screen = Screen()



tim.color("black")

tim.shapesize(1.4)
tim.speed(0)



n = 0
# for i in range(360):
#     tim.pencolor(randint(0, 255) ,randint(0, 255), randint(0, 255))
#     tim.left(5)
#     tim.circle(100)


def makeSpirograph(size_of_gap):
    for i in range(360//size_of_gap):
        tim.pencolor(randint(0, 255) ,randint(0, 255), randint(0, 255))
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


makeSpirograph(5)


screen.exitonclick()