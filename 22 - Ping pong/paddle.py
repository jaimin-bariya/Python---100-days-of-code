from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(position)
        

    def drawLine(self):
        line = Turtle()
        line.color("white")
        line.pensize(2)
        line.speed(0)
        line.penup()
        line.hideturtle()
        line.setposition(0, 250)
        line.setheading(270)
        
        #find distance and make dotted line from (0,250) to (0,-250)

        distance = line.distance(0,-250)
        for _ in range(int(distance//20)):
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)

    
    def goUp(self):
        if self.ycor() < 220:
            newY = self.ycor() + 20
            self.sety(newY)

    def goDown(self):
        if self.ycor() > -220:
            newY = self.ycor() - 20
            self.sety(newY)
    

       