from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
cash = MoneyMachine()
menu = Menu()

is_on = True

while is_on:

    options = menu.get_items()
    choice = input(f"What would you like?  {options}:  ").lower()

    if choice == "off":
        is_on = False
    
    elif choice == "report":
        machine.report()
        cash.report()

    else:
        drink = menu.find_drink(choice)
        print(f"{drink.cost}")
        if machine.is_resource_sufficient(drink):
           if cash.make_payment(drink.cost):
               machine.make_coffee(drink)

               