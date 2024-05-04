from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

moneymachine.report()
coffeemaker.report()

isOn = True

while (isOn):

    choice = input(f"Choose your drink {menu.get_items()}: ")


    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif choice in ["latte", "espresso", "cappuccino"]:
        drink = menu.find_drink(choice)
        print(f"Cost of the {drink.name} is {drink.cost}")

        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)







