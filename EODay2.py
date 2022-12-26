print("Welcome to the tip calculator")
total = input("What was the total bill?  £")
percent = input("What percentage tip would you like to give?  10, 12 or 15? ")
people = input("How many people to split the bill? ")

float_total = float(total)
float_percent = float(percent) / 100
int_people = int(people)

float_total = float_total + (float_total * float_percent)

payable = round(float_total/ int_people, 2)
payable_format = "{:.2f}".format(payable)
print(f"Each person should pay: £{payable_format}")