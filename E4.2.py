
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a # comma. ")
# This is how you would spare yourself doing dull data entry every time!
# names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# This relates to 'test hard coding' the data entry directly into names_string - commented out above (line 10)
# buyer = names_string[random.randint(0, len(names_string)-1)]
buyer = names[random.randint(0, len(names)-1)]
print(f"{buyer} is going to buy the meal today!")