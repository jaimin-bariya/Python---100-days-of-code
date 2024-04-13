# loops - for, while, range
# if else
# list, strings, modules - random




import random
from art import stages, logo
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
LIVES = 6
user_guessed_letters = []


# test code
print(f"chosen word is {chosen_word}")



display = ["_"]*word_length





isGameOn = True

print(logo)

while(isGameOn):




    print(f"Your lives {LIVES}")
    guess = input("Guess a letter : ").lower()
    


    if guess in user_guessed_letters:
        print(f"You have already guessed this {guess} letter, guess another letter")
    else: 
        user_guessed_letters.append(guess)
        if guess in chosen_word:
            for position in range(word_length):
                if guess == chosen_word[position]:
                    display[position] = guess
        else:
            print(f"You guess letter {guess} is not in the word, You lose a life")
            LIVES -= 1
            if LIVES == 0:
                print(f" \nYour lives {LIVES}")
                print("You lose")
                isGameOn = False

        
        print(f"{''.join(display)}")
        print(stages[LIVES])



    if "_" not in display:
        print(" \n You won")
        isGameOn = False
