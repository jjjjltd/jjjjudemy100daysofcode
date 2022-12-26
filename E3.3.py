# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Leap = False

if year % 4 == 0:
    Leap = True
    if year % 100 == 0:
        Leap = False
    
    if year % 400 == 0:
        Leap = True

if Leap:
    print("Leap year.")
else:
    print("Not leap year.")