from turtle import Turtle, Screen, colormode
from random import randint, choice

colormode(255)


tim = Turtle()
screen = Screen()



tim.shape("turtle")
tim.color("black")
tim.pensize(10)
tim.shapesize(1.4)
tim.speed(0)


ANGLES = [90, 180, 270, 360]

def moveTim():
    tim.pencolor(randint(0,255), randint(0,255), randint(0,255))
    tim.setheading(choice(ANGLES))
    tim.forward(20)


for i in range(100):
    moveTim()









screen.exitonclick()