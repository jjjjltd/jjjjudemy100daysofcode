# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

name1score = name1.count("t") + name1.count("r") + \
name1.count("u") + name1.count("e") + name2.count("t") + \
name2.count("r") + name2.count("u") + name2.count("e")

name2score = name1.count("l") + name1.count("o") + \
name1.count("v") + name1.count("e") + name2.count("l") + \
name2.count("o") + name2.count("v") + name2.count("e")


lovescore = str(name1score) + str(name2score)
lovescore_int = int(lovescore)

if lovescore_int <10 or lovescore_int > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")

elif lovescore_int >= 40 and lovescore_int <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")