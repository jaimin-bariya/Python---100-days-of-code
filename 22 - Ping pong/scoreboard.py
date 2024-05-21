from turtle import Turtle

FONT = ("Arial", 30, 'bold')


class Score(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(position)
        self.showScore()
        

    def showScore(self):
        self.clear()
        self.write(arg=f"{self.current_score}", align="center", font=FONT)
        
    def increase1(self):
        self.current_score += 1
        self.showScore()
    
    
        