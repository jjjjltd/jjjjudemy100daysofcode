# fizzbuzz game
result = 0
for number in range(1, 101):

    if number % 3 !=0 and number % 5 != 0:
        print(str(number))
    else:

        if number % 3 == 0:
            if number % 5 == 0:
                print(f"FizzBuzz")
            else:
                print (f"Fizz")
        if number % 5 == 0 and number % 3 != 0:
            print(f"Buzz")

