
#1
x_val = [1, 2, 3]
for x in x_val: ##Looping without indices
 print(x)

#2
for i in range(len(x_val)): ##Looping with indices
 print(x_val[i])

#3
cities = ('Dhaka', 'Tokyo', 'Seoul', 'Tehran', 'Doha')
countries = ('BD', 'JP', 'SK', 'IR', 'QR')
for city, country in zip(cities, countries):
 print(f'The city is {city} and corresponding country {country}')

#4
for index, number in enumerate(x_val):
 print(f'xa_val[{index}] = {number}')

#5
def f(x):
 return x**3
print(f(3))

#6
from scipy.integrate import quad
print(quad(lambda x: x**2, 0 , 3))

#7
f = (lambda x: x**3)(3)
print(f)

#8
import numpy as np
a = np.zeros(3, dtype = int)
print(a.shape)
print(a)
print(type(a))


#9
import numpy as np
a = np.zeros(10)
print(a)
print(type(a))
print(a.shape)
print(np.linspace(2, 4, 50))


#10
import matplotlib.pyplot as plt
import numpy as np
a = np.zeros(10)
b= np.linspace(2, 4, 50)
plt.plot(b)
plt.title("Hijbiji")
plt.xlabel("Hiji")
plt.ylabel("Biji")
plt.show()

#11
import matplotlib.pyplot as plt
import numpy as np
d = np.array((12, 16 , 14, 18), dtype = float)
e = np.array((13, 17, 19, 21))
print(d@e)

#12
import matplotlib.pyplot as plt
import numpy as np
a = np.random.randn(5)
print(a)

#13
import matplotlib.pyplot as plt
import numpy as np
b = np.copy(a)
print(b)

#14
import matplotlib.pyplot as plt
import numpy as np

a = np.sqrt(2 * np.pi)
print(a)

#15
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3])
b = np.sin(x)
print(b)

#16
import matplotlib.pyplot as plt
import numpy as np
def f(x):
 return 1 if x > 0 else 0
print(f(1))
