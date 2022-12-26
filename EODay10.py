from caesarart import calc
print(calc)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for action in operations:
    # print(f"{action}, {operations[action]}")
    print(action)
symbol = input("Pick an action from above. ")

print(f"{num1} {symbol} {num2} = {operations[symbol](num1, num2)}")