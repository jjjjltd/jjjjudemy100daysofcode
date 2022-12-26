from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "c"

print(table)



# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse")

# my_screen = Screen()
# timmy.forward(125)
# my_screen.exitonclick()
# def bar():
#     my_variable = 9
 
#     if 16 > 9:
#       my_variable = 16
 
#     print(my_variable)
 
# bar()
# i = 50
# def foo():
#     i = 100
#     return i
 
# foo()
# print(i)
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)
# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))
# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)
# def add(n1, n2):
#   return n1 + n2
 
# def subtract(n1, n2):
#   return n1 - n2
 
# def multiply(n1, n2):
#   return n1 * n2
 
# def divide(n1, n2):
#   return n1 / n2
 
# print(add(2, multiply(5, divide(8, 4))))





# def camel_case(str1, str2):
#     str1 = str1.title()
#     str2 = str2.title()
    
#     return str1 + " " + str2
# str1 = []
# str2 = []

# camel = camel_case("eleanor", "catriona")
# print(camel)

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# print(dict[1])

# print(6 + 4 / 2 - (1 * 2))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# def greet_with(name, location):
#     print(f"name is:  {name}")
#     print(f"location is: {location}")

# # greet_with("John Joyce", "TW17")
# greet_with(location="TW17 0ab", name="John Joyce")
# from caesarart import logo
# print(logo)

# travel_log = {
#     "France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart",], "total_visits": 5},
# }

# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart",], 
#         "total_visits": 5
#     },
# ]
# print (travel_log)