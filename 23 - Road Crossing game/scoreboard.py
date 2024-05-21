from turtle import Turtle

FONT = ("Arial", 10, "bold")


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.current_level = 1
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(x=-260, y=220)
        self.showLevel()
        
    def showLevel(self):
        self.clear()
        self.write(arg=f"Level {self.current_level}", font=FONT)
    
    def UpdateLevel(self):
        self.current_level += 1
        self.showLevel()

    def GameOver(self):
        self.goto(x=-50, y=0)
        self.color("red")
        self.write(arg=f"Game Over", font=FONT)
