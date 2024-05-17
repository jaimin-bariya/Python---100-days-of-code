from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("orange")
tim.shapesize(1.5)

def drawDashsquare():
    for i in range(20):
        dashedLine()
    tim.left(90)


def dashedLine():
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

for _ in range(4):
    drawDashsquare()


screen.exitonclick()