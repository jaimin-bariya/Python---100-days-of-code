from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)

        #generate random x and y
        xcorFood = random.randint(-280, 280)
        ycorFood = random.randint(-280, 280)

        self.goto(x=xcorFood, y=ycorFood)


    def refreash(self):
        xcorFood = random.randint(-280, 280)
        ycorFood = random.randint(-280, 280)
        self.goto(x=xcorFood, y=ycorFood)
