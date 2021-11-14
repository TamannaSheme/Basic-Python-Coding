# Defining Function
import numpy as np


def function(x):
    return x ** 3 - x - 4


maxiter = 50
error = 5  # percent

# initial guess
a = 1.00  # lower range
b = 2.00  # upper range


def approx_error(iteration, x_r_new, x_r_old):
    if iteration == 0:
        return 9999999  # setting larger value to beat the error condition
    else:
        return (x_r_new - x_r_old) / x_r_new


if function(a) * function(b) > 0:
    print("The function cannot be solved with those initial guesses.")
else:
    print("Iteration No. \t\t a \t b \t\t X_root \t f(x_root) \t approx_error")
    print("_____________________________________________________________________________")

    x_rn = 0
    x_ro = 0
    for i in range(maxiter):

        x_rn = (a + b) / 2
        approx = approx_error(i, x_rn, x_ro)

        print(str(i + 1) + "\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.12f\t" % (a, b, x_rn, function(x_rn), approx))

        if (approx * 100) < error:
            print("-----------------------------")
            print("Root found: " + str(x_rn))
            break
        if function(a) * function(x_rn) > 0:
            a = x_rn
        else:
            b = x_rn
            x_ro = x_rn

    if i is maxiter - 1:
        print("Maxiter reached. And the approximate root is: " + str(x_rn))

#another method

def f(x):
    return x**3-x-4

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)
