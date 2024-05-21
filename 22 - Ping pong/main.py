from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

#position of paddle
PADDLE_POSITION = [(-440, 0), (430, 0)]
SCORE_POSITION = [(-40, 200), (40, 200)]



# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=500)
screen.title("Welcome to the Ping Pong Game")
Winning_score = int(screen.textinput(title="Winning Score", prompt="Decide the winning score : "))
screen.tracer(0)


def want_to_play_again(winner):
    global paddle1_score, paddle2_score, is_game_on
    user_choice = screen.textinput(title=f"Winner is {winner}", prompt="Do you want to play again? type (y/n)").lower()

    if user_choice == "y":
        paddle1_score.current_score = 0
        paddle2_score.current_score = 0
        is_game_on = True
        return True
    else:
        return False



# Object Creation
paddle1 = Paddle(PADDLE_POSITION[0])
paddle2 = Paddle(PADDLE_POSITION[1])
line = paddle1.drawLine()
ball = Ball()
paddle1_score = Score(SCORE_POSITION[0])
paddle2_score = Score(SCORE_POSITION[1])





screen.listen()
#for paddle 1
screen.onkeypress(key="w", fun=paddle1.goUp)
screen.onkeypress(key="s", fun=paddle1.goDown)

#for paddle 2
screen.onkeypress(key="Up", fun=paddle2.goUp)
screen.onkeypress(key="Down", fun=paddle2.goDown)


is_game_on = True

while is_game_on:

    screen.update()
    time.sleep(0.05)

    ball.MoveBall()

    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.Bounce_y()
        
    
    elif ball.distance(paddle2) < 50 and ball.xcor() > 420 or ball.distance(paddle1) < 50 and ball.xcor() < -420:
        ball.Bounce_x()
        

    elif ball.xcor() > 480:
        print("loss paddle 2")
        ball.reset_position()
        paddle1_score.increase1()
        
    
    elif ball.xcor() < -480:
        print("loss paddle 1")
        ball.reset_position()
        paddle2_score.increase1()

    
    if paddle1_score.current_score >= Winning_score:
        is_game_on = False
        want_to_play_again("Right Player")


    
    if paddle2_score.current_score >= Winning_score:
        is_game_on = False
        want_to_play_again("Left Player")
            
        
        





screen.exitonclick()


