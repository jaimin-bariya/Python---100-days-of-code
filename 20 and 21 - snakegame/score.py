from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Poetsen One", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0

        self.hideturtle()
        self.color("White")
        self.penup()
        self.setposition(x=0, y=280)

        self.write(f"Score : {self.current_score}", align=ALIGNMENT, font=FONT)
        
    
    def increaseScore(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score : {self.current_score}", align="center", font=("Arial", 12, 'bold'))

    
    def gameOver(self):
        self.home()
        self.color("red")
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)


