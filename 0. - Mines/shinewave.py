from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


screen.setup(width=1000, height=500)

#added 

tim.penup()
tim.goto(x=-450, y=0)
tim.pendown()
tim.forward(900)
tim.speed(0)

tim.penup()
tim.goto(x=-450, y=0)
tim.pendown()

tim.setheading(90)


def upPart():
    for _ in range(90):
        tim.forward(2)
        tim.right(2)

def downPart():
    for _ in range(90):
        tim.forward(2)
        tim.left(2)



while(tim.xcor() < 350):
    upPart()
    downPart()



screen.exitonclick()