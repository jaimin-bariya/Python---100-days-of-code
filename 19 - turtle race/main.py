from turtle import Turtle, Screen
import random

COLORS = ['red', 'orange', 'green', 'yellow', 'purple', 'blue']
STARTPOSITION_X = -350
STARTPOSITION_Y = -80
ALL_TURTLE = []
WINNER = None

# screen setups
screen = Screen()
screen.setup(width=800, height=300)



user_bet = screen.textinput(title="Choose your bet", prompt="On which turtle you wanna ber (type color name)?").lower()


for turtle_index in range(len(COLORS)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(COLORS[turtle_index])
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.goto(x=STARTPOSITION_X, y=STARTPOSITION_Y)
    STARTPOSITION_Y += 30
    ALL_TURTLE.append(new_turtle)

    






is_race_on = False


if user_bet:
    is_race_on = True



while(is_race_on):
    


    for tur in ALL_TURTLE:
        random_distance = random.randint(0, 10)
        tur.forward(random_distance)

        if tur.xcor() >= 350:
            is_race_on = False
            WINNER = tur.pencolor()

            if WINNER == user_bet:
                print(f"You won this bet, the winner of this match is {WINNER}")
            else:
                print(f"you lose this bet, the winner of this match is {WINNER}")

            
            
    

screen.exitonclick()