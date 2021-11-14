def f(x):
    return x * x - 2 * x + 3


def g(x):
    return (x * x + 3) / 2


def fixed_point_iteration(x_old, e, N):
    print('\n====Fixed point iteration====')
    print('\niteration\t\txi\t\t\t\tXi+1 =g(xi)\t\tError')
    step = 1
    flag = 1
    condition = True
    while condition:
        x_new = g(x_old)
        error = abs((x_new - x_old) / x_new) * 100
        print('%d\t\t\t\t%0.6f\t\t%0.6f\t\t%0.6f' % (step, x_old, x_new, error))
        x_old = x_new
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x_new)) > e
    if flag == 1:
        print('\nRequired root is:%0.6f' % x_new)
    else:
        print('\nNot convergent')

# Input Section
print('====Input Section==========')
print('Enter the Inputs:')



x0 = input('Enter Guess: ')
e = input('Specified Error: ')
N = input('Maximum Step: ')
# Converting x0 and e to float
x0 = float(x0)
e = float(e)
# Converting N to integer
N = int(N)
fixed_point_iteration(x0, e, N)
