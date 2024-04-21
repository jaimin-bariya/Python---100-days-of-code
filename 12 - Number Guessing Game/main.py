from random import randint
from art import logo
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPT = 5





def check_answer(guess, answer, attempt):
    
    if guess < answer:
        print("Too low")
        print("Guess again")
        return attempt - 1

    elif guess > answer:
        print("Too High")
        print("Guess again")
        return attempt - 1
    
    else:
        print(f"You got it!, Your guess {guess} is correct")




def game():
    print(logo)
    print("Welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")
    level = input("Choose difficulty level easy or hard").lower()


    if level == "easy":
        attempt = 10
    elif level == "hard":
        attempt = 5
    else:
        print("valid input")
    
    answer = randint(1, 100)


    guess = 0

    while (guess != answer):

        print(f"You have {attempt} attempts remaining to guess the number.")

        guess = int(input("Guess any number :"))

        attempt = check_answer(guess, answer, attempt)


        if attempt == 0:
            print("You lose this game, best of luck for next time...")
            return
        

game()



