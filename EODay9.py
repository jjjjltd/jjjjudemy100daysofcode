import os
from caesarart import gavel

def find_highest(bidders):
    highest = 0
    name = ""
    for bid in bidders:
        if bidders[bid] > highest:
            name = bid
            highest = bidders[bid]

    print(f"The winnder is: {name}, with a bid of £{highest}.")
next = True
print(gavel)
print("Welcome to the secret auction program.")
bidders = {}
while next == True:
    name = input("What is your name?\n")
    bid = float(input("What's your bid? £"))
    bidders[name] = round(bid,2)

    goon = input("Are there any other bidders?  'yes' or 'no'\n").lower()
    if goon == "no":
        next = False
    
    os.system('cls')

find_highest(bidders)