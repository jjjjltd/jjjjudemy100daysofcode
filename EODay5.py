#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for i in range(1, nr_letters + 1):
#     password.append(letters[random.randint(0, len(letters)-1)])

# for i in range(1, nr_symbols + 1):
#     password.append(symbols[random.randint(0, len(symbols)-1)])

# for i in range(1, nr_numbers + 1):
#     password.append(numbers[random.randint(0, len(numbers)-1)])

str = ""

print(str.join(password))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Total_length = nr_letters + nr_numbers + nr_symbols
letter_count = 1
symbol_count = 1
number_count = 1
for i in range(1, Total_length):

    selection = random.randint(0, 2)
    if selection == 0:
        if letter_count <= nr_letters:
            password.append(letters[random.randint(0, len(letters)-1)])
            letter_count += 1

    if selection == 1:
        if number_count <= nr_numbers:
            password.append(numbers[random.randint(0, len(numbers)-1)])
            number_count += 1

    if selection == 2:
        if symbol_count <= nr_symbols:
            password.append(symbols[random.randint(0, len(symbols)-1)])
            symbol_count += 1



str = ""
print(f"Symbols:  {symbol_count}, Numbers4: {number_count}, Letters {letter_count}")
print(str.join(password))