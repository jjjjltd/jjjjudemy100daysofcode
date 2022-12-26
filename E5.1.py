total_height = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total_height += student_heights[n]

# print(f"{total_height} divided by {n+1}")
average = round(total_height / (n + 1))
print(str(average))