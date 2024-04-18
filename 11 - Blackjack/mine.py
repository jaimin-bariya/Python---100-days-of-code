from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
PLAYERSCARDS = []
DELEARSCARDS = []
DELEARSHWOCARDS = []


TOTALNUMCARDS = len(cards)

# function to add one cards in list
def AddOneCard(preList):
    newCard = cards[random.randint(0,TOTALNUMCARDS-1)]
    preList.append(newCard)


# funciton to shwo players and delear's cards
def ShowCards(player, delear):
    print(f"\nYour Cards - {player}")
    print(f"Sum of your cards - {sum(player)} \n")
    print(f"Delear's cards - {delear}")
    print(f"Sum of Delear's cards - {sum(delear)} \n")





gameOn = True


wantToPlay = input("Do you Want to play 21 game? TYpe y or n : ").lower()

if wantToPlay == "n":
    print("Thank you, ")
    gameOn = False


while(gameOn):

    hitOn = True
    below17 = True

    os.system("cls")
    print(logo)

    PLAYERSCARDS.clear()
    DELEARSCARDS.clear()
    DELEARSHWOCARDS.clear()


    # ADD cards in user list
    AddOneCard(PLAYERSCARDS)
    AddOneCard(PLAYERSCARDS)

    # generate dealerlist -> 2 cards
    AddOneCard(DELEARSCARDS)
    DELEARSHWOCARDS.append(DELEARSCARDS[0])
    AddOneCard(DELEARSCARDS)


    #Show cards
    ShowCards(PLAYERSCARDS, DELEARSHWOCARDS)

    while(hitOn):

        Hit_Pass = input("\nEnter Hit to add one more cards in your cards or Pass to handover delear : ").lower()

        if Hit_Pass == "hit":
            AddOneCard(PLAYERSCARDS)
            ShowCards(PLAYERSCARDS, DELEARSHWOCARDS)

            if sum(PLAYERSCARDS) > 21:
                hitOn = False
                print("You Lose...\n")

 
        elif Hit_Pass == "pass":
            
            while(below17):

                if sum(DELEARSCARDS) < 17:
                    AddOneCard(DELEARSCARDS)
                else:
                    below17 = False
            

            if sum(DELEARSCARDS) > 21:
                ShowCards(PLAYERSCARDS, DELEARSCARDS)
                print("\nYou Win\n")
            elif sum(DELEARSCARDS) == sum(PLAYERSCARDS):
                print("\nMatch Draw \n")
            elif sum(PLAYERSCARDS) > sum(DELEARSCARDS):
                ShowCards(PLAYERSCARDS, DELEARSCARDS)
                print("\nYou Win\n")
            else:
                ShowCards(PLAYERSCARDS, DELEARSCARDS)
                print("\nYou Lose \n")

    
    
            hitOn = False
        else:
            print("Enter Valid Input ")


    



    wantToPlay = input("Do you Want to play 21 game? TYpe y or n : ").lower()
    if wantToPlay == "n":
        os.system("cls")
        print("Thank you, ")
        gameOn = False








    


