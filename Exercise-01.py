#Exercise-01
"""Find root of ax^2 + bx + c, consider fixed x value but
take multiple values for co-efficient. Hints: def f(x, co-efficient),
co-efficient = (2, 1)."""
# Python program to find roots of quadratic equation
import math


# function for finding roots
def findRoots(a, b, c):

    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))


    if dis_form > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis_form == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    findRoots(a, b, c)
