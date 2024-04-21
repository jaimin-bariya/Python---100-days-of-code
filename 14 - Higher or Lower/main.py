from art import logo, vs
from game_data import data
from random import choice
from os import system


def get_new_comparition(a):
    b = data[data.index(a)]

    while (data.index(a) == data.index(b)):
        b = choice(data)
    
    return b



def check_answer(user_ans, a, b, score):

    if user_ans == "A" and a["follower_count"] > b["follower_count"]:
        print(f"You are correct, Current score {score + 1}")
        return score + 1
    elif user_ans == "B" and a["follower_count"] < b["follower_count"]:
        print(f"You are correct, current score {score + 1}")
        return score + 1
    else:
        print(f"Sorry, that's wrong. Final Score {score}")
        return score






def game():

    score = 0

    compare_a = choice(data)

    useranswer = True 

    while(useranswer):

        print(logo)
        
        print(f"Compare A: {compare_a["name"]}, {compare_a["description"]} from {compare_a["country"]} - {compare_a["follower_count"]}")
        print(vs)
        against_b = get_new_comparition(compare_a)
        
        print(f"Against B: {against_b["name"]}, {against_b["description"]} from {against_b["country"]} - {against_b["follower_count"]}")

        user_prediciton = input("Who has more followers? Type A or B : ").upper()

        system("cls")
        
        new_score = check_answer(user_prediciton, compare_a, against_b, score)

        if score == new_score:
            useranswer = False
        else:
            compare_a = against_b
            score = new_score


game()

