from caesarart import higherlower
from caesarart import vs
from EODay14Data import data
import random

playon = True
wincount = 0 
choice1 = 0

while playon:

    choice1 = random.randint(1, len(data)-1)
    choice2 = choice1

    c1name = data[choice1]["name"]
    c1followers = data[choice1]["follower_count"]
    c1desc = data[choice1]["description"]

    while choice1 == choice2:
        choice2 = random.randint(0, len(data)-1)
        c2name = data[choice2]["name"]
        c2followers = data[choice2]["follower_count"]
        c2desc = data[choice2]["description"]



    print("Who has the most follower?")
    print(higherlower)
    print(f"Is it 1. {c1name}, {c1desc}?" )
    print(vs)
    print(f"Is it 2. {c2name}, {c2desc}?" )
    higher = int(input(f"Enter 1 for {c1name}, 2 for {c2name} "))

    if higher == 1:

        if c1followers < c2followers:
            playon = False
        else:
            wincount += 1
    elif higher == 2:
        if c2followers < c1followers:
            playon = False
        else:
            wincount += 1

    print(f"{c1name} has {c1followers}m, {c2name} has {c2followers}m")

print(f"You lose f***tard, but you did get {wincount} right.")