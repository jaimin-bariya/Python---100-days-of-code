from turtle import Turtle, Screen

# objects creation 
timmy = Turtle()
screen = Screen()



# turtle specification 
timmy.shape("turtle")
timmy.color("orange")
timmy.shapesize(1)


#function to 100 forward and move right (west)
def forwardAndMove():
    timmy.forward(100)
    timmy.right(90)



for _ in range(4):
    forwardAndMove()




screen.exitonclick()