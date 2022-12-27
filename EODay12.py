import random
import os
from caesarart import guillotine

hidden_number = random.choice(range(1,100))

print(guillotine)
print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100")
option = input("Choose a difficulty.  Type 'easy' or 'hard': ")

if option == 'easy':
    guesses = 10
else:
    guesses = 5

remaining_guesses = guesses
right = False

while right == False:

    guess = int(input("Make a guess: "))
    remaining_guesses -= 1

    if guess == hidden_number:
        input(f"Wow, you got it with {remaining_guesses} left.  Well done!!  Press any key to exit.")
        right = True

    if not right:

        print(f"You have {remaining_guesses} attempts to guess the number.")

        if guess > hidden_number:
            print("Too high.")
        else:
            print("Too low.")

        if remaining_guesses > 0:
            print("guess again")
        else:
            print(f"My guess was {hidden_number}.  Unlucky!")
            right = True