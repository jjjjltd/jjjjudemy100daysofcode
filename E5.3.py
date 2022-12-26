start = int(input("Enter starting range number: "))
end = int(input("Enter ending range number: ")) + 1

Total_Evens = 0
for number in range(start, end):
    if number % 2 == 0:
        Total_Evens += number

print(str(Total_Evens))

