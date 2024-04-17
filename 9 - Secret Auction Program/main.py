import os
from art import logo

anyElse = True

bidGame = {}

print(logo)

while(anyElse):
    name = input("Enter Your name here : ").lower()
    money = int(input("Enter Your bid amount here :"))
    bidGame[name] = money

    other = input("Is there anyone else for bidding? Type y/n: ").lower()
    os.system("cls")
    if other == "n":
       highest_bidder = max(bidGame, key=bidGame.get)
       print(f"The Winner is {highest_bidder} with bid amount {bidGame[highest_bidder]}")
       anyElse = False
