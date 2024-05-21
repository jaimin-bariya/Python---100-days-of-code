from turtle import Screen
from cars_manager import CarManager
from myturtle import MyTurtle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=500, width=600)
screen.bgcolor("white")
screen.title("Welcome to the Road Crossing Game")
screen.tracer(0)
screen.listen()

#object creation 
cars = CarManager()
mytim = MyTurtle()
myScore = ScoreBoard()



#key listining
screen.onkeypress(key="Up", fun=mytim.goUp)
screen.onkeypress(key="Down", fun=mytim.goDown)






is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.05)

    cars.createCar()
    cars.moveCars()


    #detect collision of mytim with anycar
    for car in cars.all_cars:

        if car.distance(mytim) < 20:
            myScore.GameOver()
            is_game_on = False
            print("made collision")
        
        elif mytim.ycor() >= 235:
            print("level plus")
            mytim.resetPlayer()
            myScore.UpdateLevel()
            time.sleep(2)

        





screen.exitonclick()