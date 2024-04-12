import random
from art import rock, paper, scissors

choices = ['rock', 'paper', 'scissors']

userInput = int(input("what do you choose. type 0 = Rock, 1 = Paper, 2 = Scissors : "))

print("Your Choice :- " + choices[userInput]) 
if userInput == 0:
    print(rock)
elif userInput == 1:
    print(paper)
elif userInput == 2:
    print(scissors)
else:
    print("Enter valid input")


print("\n\n")

computerChoice = random.randint(0,2)
print("Computer Choice :- " + choices[computerChoice])

if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
elif computerChoice == 2:
    print(scissors)


# winner
if userInput == 0 and computerChoice == 1:
    print("Winner is Computer")
elif userInput == 0 and computerChoice == 2:
    print("Winner is You")
elif userInput == 1 and computerChoice == 0:
    print("Winner is You")
elif userInput == 1 and computerChoice == 2:
    print("Winner is Computer")
elif userInput == 2 and computerChoice == 0:
    print("Winner is Computer")
elif userInput == 2 and computerChoice == 1:
    print("Winner is You")
else:
    print("This is a Draw")









