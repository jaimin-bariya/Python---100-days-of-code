from turtle import Turtle
import random, time

RANDOM_START = [-10, 10]


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = random.choice(RANDOM_START)
        self.y_move = random.choice(RANDOM_START)

    
    def MoveBall(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def Bounce_y(self):
        self.y_move *= -1
        

    def Bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.home()
        self.x_move = random.choice(RANDOM_START)
        self.y_move = random.choice(RANDOM_START)
    
