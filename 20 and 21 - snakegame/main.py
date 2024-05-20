from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard


import random, time


SPEED = 0.40



#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Object creation
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)









is_game_on = True

while is_game_on:


    # 2 - Snake moving
    screen.update()
    
    if score.current_score > 25:
        SPEED = 0.05
    elif score.current_score > 20:
        SPEED = 0.10
    elif score.current_score > 15:
        SPEED = 0.15
    elif score.current_score > 10:
        SPEED = 0.20
    elif score.current_score > 5:
        SPEED = 0.25
    elif score.current_score > 3:
        SPEED = 0.30


    time.sleep(SPEED)

    snake.move()


    #collision with food
    if snake.head.distance(food) < 15:
        food.refreash()
        score.increaseScore()
        snake.extend()
        print(score.current_score)
    

    if snake.checkCollisionWall() or snake.checkCollisionTail():

        score.gameOver()

        is_game_on = False
    


screen.exitonclick()
              




