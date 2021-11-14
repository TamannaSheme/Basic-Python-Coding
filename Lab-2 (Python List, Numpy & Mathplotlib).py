# ANSWER TO THE QUESTION NO: 1
import numpy as np
#1) Create an array of shape (2, 3, 4) of zeros
a = np.zeros((2, 3, 4))
print(a)

print()
#2) Create an array of (2, 3, 4) of ones.

a = np.ones((2, 3, 4))
print(a)

print()
#3) Create an array with values 0 to 999 using the “np.arange” function

b = np.arange(start=0, stop=1000, step=1)
print(b)

#4) Create an array from the list [2, 3.2, 5.5, -6.4, -2.2, 2.4] and assign it to the variable “a”

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(a)



#5) Print a[1] and print a[1:4]

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(a)
print(a[1])
print(a[1:4])


"""6) Create a 2D array from the following list and assign it to the varaiable “a”: [[2, 3.2, 5.5, -
6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]]"""

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])
print(a)

#7 Python Programming to explain
# numpy.linspace() function
import numpy as np
# restep set to True
print("When retstep is True:", np.linspace(2.0, 3.0, num=5, retstep=True), "\n")
print("When retstep is False:", np.linspace(2.0, 3.0, num=5, retstep=False), "\n")
# To evaluate the cos() in long range
x = np.linspace(0, 2, 10)
print("Value\n", np.cos(x))

# ANSWER TO THE QUESTION NO: 2

import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
z = 1/(1 + np.exp(-x))
plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")
plt.show()

##########
x = np.linspace(-100, 100, 200)
z = 1/(1 + np.exp(-x))
plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")
plt.show()
