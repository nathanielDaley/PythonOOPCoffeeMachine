from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

VALID_USER_INPUTS = ["espresso", "latte", "cappuccino", "off", "report"]

def get_user_input():
    u_input = input("What would you like? Type \"espresso\" \"latte\" or \"cappuccino\": ").lower()
    while not u_input in VALID_USER_INPUTS:
        print("Invalid input")
        u_input = input("What would you like? Type \"espresso\" \"latte\" or \"cappuccino\": ").lower()

    return u_input


coffee_machine_on = True
while coffee_machine_on:
    user_input = get_user_input()

    if user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif user_input == "off":
        coffee_machine_on = False
    else:
        drink = my_menu.find_drink(user_input)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)