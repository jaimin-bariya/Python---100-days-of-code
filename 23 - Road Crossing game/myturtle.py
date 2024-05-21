from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.goto(x=0, y=-230)
        self.setheading(90)


    def goUp(self):
        new_y = self.ycor() + 10
        self.sety(new_y)

    def goDown(self):
        new_y = self.ycor() - 10
        self.sety(new_y)

    def resetPlayer(self):
        self.goto(x=0, y=-230)