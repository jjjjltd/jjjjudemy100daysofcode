#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = 2
# nr_symbols = 3
# nr_numbers = 4

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []

# for letter in letters(0, nr_letters):
#  password = random.choice(letters)
# password.append(letters[random.randint(0, len(letters)-1)])
     
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Total_length = nr_letters + nr_numbers + nr_symbols
letter_count = 0
symbol_count = 0
number_count = 0

print(f"Total length: {Total_length}, letters:  {nr_letters}, syms:  {nr_symbols}, nums:  {nr_numbers}")

while len(password) < Total_length:

    selection = random.randint(0, 2)
    if selection == 0:
        if letter_count < nr_letters:
            password.append(letters[random.randint(0, len(letters)-1)])
            letter_count += 1

    if selection == 1:
        if number_count < nr_numbers:
            password.append(numbers[random.randint(0, len(numbers)-1)])
            number_count += 1

    if selection == 2:
        if symbol_count < nr_symbols:
            password.append(symbols[random.randint(0, len(symbols)-1)])
            symbol_count += 1

str = ""
print(f"\nLetters {letter_count}, Symbols:  {symbol_count}, Numbers: {number_count}, ")

print(f"\nYour password is: {str.join(password)}, length:  {len(password)}")
