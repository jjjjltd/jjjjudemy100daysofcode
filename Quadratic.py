import math

x = math.sqrt(9)
y = 4**3

# -b + sqrt(b**2 - 4 * a * c)
#  / 2 * a


a = 1
b = 10
c = 5

def quad(a, b, c, op):
    b_squared = b**2
    ac4 = 4 * a * c
    x = b_squared - ac4
    root = math.sqrt(abs(x))
    root_div = root / (2 * a)
    if op == "+":
        end_result = -1*b + root_div 
    else:
        end_result = -1*b - root_div

    print(f"Workings_:",op,
    "\n a=", a,
    "\n b=", b,
    "\n c=", c, "\n",
    "\n b_squared= ", b_squared, 
    "\n 4ac= ", ac4,
    "\n 2a= ", 2*a,
    "\n Square Root of ", b_squared, " - ", ac4, ") = ", root,
    "\n Root / 2*a = ", root_div,
    "\n -b", op, "Divided Root = ", end_result, "\n\n") 
    return end_result


print(f"x= ", quad(a, b, c, "+"), " or x=  ", quad(a, b, c, "-"))