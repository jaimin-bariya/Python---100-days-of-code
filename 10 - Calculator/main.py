from art import logo
import os



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b


operations = {
    "+": add,
    "-": sub,
    "/": divide,
    "*": multiply
}

gameOn = True

print(logo)
num1 = int(input("Enter your 1st number : "))

while(gameOn):
    
    operation = input("Enter Operation from below \n+ \n- \n* \n/ \nEnter : ")
    num2 = int(input("Enter sencond number : "))

    answer = operations[operation](num1, num2)
    print(answer)

    con = input("Do you want to restart calculator or exit - type c/e : ").lower()
    if con == "c":
        num1 = answer
        
    elif con == "e":
        print("Thanks you, See you soon")
        gameOn = False



