import turtle
from turtle import Turtle, Screen

tim = turtle.Turtle()
screen = Screen()


tim.shape("turtle")
tim.color("orange")
tim.shapesize(1)




def draeShapes(sides):
    angle = 360 / sides
    for i in range(sides):
        tim.color("orange")
        if (sides % 2 == 0 and i == sides/2):
            tim.color("green")
        
        tim.forward(100)
        tim.right(angle)

        




for i in range(3, 11):
    draeShapes(i)


screen.exitonclick()