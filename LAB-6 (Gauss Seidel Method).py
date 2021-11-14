import numpy as np

def approx_error(x1, x0):
   return np.abs((x1 - x0)/x1)
   approx = approx_error(x1,x0)
   return approx

f1 = lambda x,y,z :(17-y+2*z)/20
f2 = lambda x,y,z :(-18-3*x+z)/20
f3 = lambda x,y,z :(25-2*x+3*y)/20
x0=0
y0=0
z0=0

count = 1
e= float(input('Enter Tolarable error: '))
print('\nCount\t\tx\t\ty\t\tz\n ')

condition=True
while condition:

    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print(('%d\t%0.6f\t%0.6f\t%0.6f\n' %(count, x1 , y1 , z1)))

    e1 = approx_error(x1,x0);
    e2 = approx_error(y1,y0);
    e3 = approx_error(z1,z0);

    count +=1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2>e and e3>e

print('\nSolution of Gauss Seidel Method is : x=%0.6f,y=%0.6f and z=%0.6f\n'%(x1 , y1 , z1))
