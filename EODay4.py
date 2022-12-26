''' Rock/Paper/Scissors game '''
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
      (___)
'''
# Booleans
PWin = False # Player
SWin = False # System
Draw = False

player_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper, 2 for Scissors:  "))

if player_choice >= 0 and player_choice <= 2:
    system_choice = random.randint(0, 2)

    images = [rock, paper, scissors]
    print("You chose:")
    print(images[player_choice])


    print(f"System choice is: {system_choice}")
    print(images[system_choice])

    if player_choice == 0 and system_choice == 0:
        Draw = True

    if player_choice == 0 and system_choice == 1:
        SWin = True

    if player_choice == 0 and system_choice == 2:
        PWin = True

    if player_choice == 1 and system_choice == 0:
        PWin = True

    if player_choice == 1 and system_choice == 1:
        Draw = True

    if player_choice == 1 and system_choice == 2:
        SWim = True

    if player_choice == 2 and system_choice == 0:
        SWin = True

    if player_choice == 2 and system_choice == 1:
        PWin = True

    if player_choice == 2 and system_choice == 2:
        Draw = True

    if PWin:
        print("You won!!  Well done.")

    if SWin:
        print("You lost.  Ha!!")

    if Draw:
        print("Draw.  Boring!!!")

else:
    print("Invalid choice.  Loser.")