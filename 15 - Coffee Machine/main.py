from menu import *

def Report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money {profit} $")


def is_resource_sufficient(order_ingredients):
    """return true if sufficient, false if not"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def payment_process():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(payment, cost):
    """Return true if money is more than or equal to cost of product, otherwise false"""
    if payment >= cost:

        global profit

        change = round(payment - cost,2)
        print(f"Here is your - {change}")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice, ingredients):
    """deduct ingredients and serve coffee"""
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"cost of your coffe {MENU[choice]["cost"]}")
    print(f"Here is your {choice} ☕, Enjoy")



isOn = True
while (isOn):
    userChoice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if userChoice == "off":
        isOn = False
        break

    elif userChoice == "report":
        Report()

    elif userChoice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[userChoice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = payment_process()

            if is_transaction_successful(payment, MENU[userChoice]["cost"]):
                make_coffee(userChoice, MENU[userChoice]["ingredients"])



    