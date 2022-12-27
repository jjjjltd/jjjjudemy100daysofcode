MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_lookup = {
    "e":  "espresso",
    "c":  "cappuccino",
    "l":  "latte",

}

profit = 0

def report(resources, profit):
    for ingredient in resources:
        print(f"{ingredient}, {resources[ingredient]}")

    print(f"{profit}")
def check_supply(coffee_ingredients, resources):
    # print(coffee_ingredients)
    supply = True
    for ingredient in coffee_ingredients:
        # print(f"{coffee_ingredients[ingredient]} vs {resources[ingredient]}")
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print("Coffee needs {ingredient).  Sorry, we only have {resources[ingredient]}")
            supply = False
    return supply
        
def make_coffee(coffee_ingredients, resources):
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]

def sufficient_coins(cost):
    print(f"Please pay price £{cost}")
    quarters = int(input("Mo. of Quarters:  "))
    dimes = int(input("Mo. of Dimes:  ")) 
    nickels = int(input("No. of Nickels:  "))
    pennies = int(input("No. of Pennies:  "))   

    total_pennies = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100

    print(f"Price: {cost}, total pennies: {total_pennies}")
    if cost > total_pennies:
        return False
    else:
        change = total_pennies - cost
        print(f"Here's your change: {change}.")
        return True

def run_machine():
    global profit 
    selection = input("What would you like? e:espresso, c: capuccino, l: latte:  ").lower()

    if selection == "off":
        return
    
    elif selection == "report":
        report(resources, profit)

    else:
        if(check_supply(MENU[coffee_lookup[selection]]["ingredients"], resources)):
            if(sufficient_coins(MENU[coffee_lookup[selection]]["cost"])):
                make_coffee(MENU[coffee_lookup[selection]]["ingredients"], resources)
                # print(f"{MENU[coffee_lookup[selection]]['cost']}")
                profit += MENU[coffee_lookup[selection]]['cost']
                report(resources, profit)
                print("Thank you for your custom!!☕")

run_machine()