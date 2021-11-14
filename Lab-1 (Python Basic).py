# 1. Strings in Python
print("Hello, World!")
print('My name is Tamanna.')
print("Hello Tamanna !!")
print('!!!!12345!!!!')
print('This is CSE 225 Ist Lab Report!!!!')
print('Python Basics Lab')

# More Strings in Python
print('python' + 'is' + 'easy')
print('python' + 'is' + 'fantastic')
print('JAVA' *2)
print('2' *5)
print('3' *30)
print('100' + 'TAKA')

# Variable with Strings in Python

a = 'x'
print(a)

b ='FOOTBALL'
print(b)

c = 'd'
p = c
print(p)

n = 'I am Tamanna.'
print(n)

name1 = 'EAST WEST UNIVERSITY'
name1 = 'COMPUTER SCIENCE AND ENGINEERING'
print(name1)

message1 = 'WELCOME TO'
message2 = 'CSE 225 LAB CLASS'

print(message1 + message2)

# Taking Input String input from USERS in Python.

print('Hello there! What is your name?')
Name = input()
print('Nice to meet you' + Name + '!')
print('How old are you,' + Name + '?')
age = input()
print('So, your age is ' + age)



# 2.String length and String traversal
a =' jackpot'
print(len(a))

for a_name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + a_name + ".  Please come to my party on Saturday!"
    print(invitation)

a = "STRING"
i = 0
while i < len(a):
    c = a[i]
    print(c)
    i = i + 1

# 3. String Slicing
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

# 4. ‘in’ operator, looping and counting

x=0
while x<5:
    print(x)
    x = x+1


y = 8
while y <= 10:
    print(y)
    y = y+1

m = 11
while m <= 20:
    print(m)
    m = m + 2

z = 0
while z <= 20:
    print('PYTHON LAB TASK')
    z = z + 3


for i in range(1,4):
        print('LOCKDOWN')

for i in range(1,4,2):
        print('SHUTDOWN')

for i in range(5,-1,-1):
        print(i)

for i in range(1,10,4):
        print('GOOD MORNING')



txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# conditional Statements Using String in Python

print('Enter your command: ')
robot_move = input()

if robot_move == 'front':
    print('Moving Front')
elif robot_move == 'back':
    print('Moving Back')
else:
    print('Stand Still')

# USE OF INFINITE LOOP AND BREAK STATEMENT
while True:
    print('Please enter your name: ')
    name = input()
    if name == 'SUPERMAN':
        break
    print('THANK YOU')

# USE OF CONTINUE STATEMENT
while True:
    print('Who are you?')
    name = input()
    if name != 'BATMAN':
        continue
    print('Hello There' + name + 'what is your passcode?')
    password = input()
    if password == 'Ice-cream':
        break

# 5. Comparison operator
a = 21
b = 10
c = 0

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if not b == a:
   print ("Line 3 - a is not equal to b")
else:
   print ("Line 3 - a is equal to b")

if ( a < b ):
   print ("Line 4 - a is less than b")
else:
   print ("Line 4 - a is not less than b")

if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")

a = 5;
b = 20;
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to  b")
else:
   print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 7 - b is either greater than  or equal to b")
else:
   print ("Line 7 - b is neither greater than  nor equal to b")


# 6. String Methods, parsing

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

def p():
 print('THIS IS MY FIRST PYTHON FUNCTION')
p()

def sum(a,b):
    return a+b
a = sum(3,7)
print(a)

def print_my_name(name):
    print('Your name is ' + ' ' + name)
my_name = input()
print_my_name(my_name)

var = print('ok')
print(type(var))

z = 10
print(type(z))

p = 'jurassic park'
print(type(p))

l = 23.567
print(type(l))

def fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)
        for i in range(1,n):
            z = x + y
            x = y
            y = z
            print(z)
fibonacci(10)

original_string = "ab_cd_ef"
split_string = original_string.split("_")
print(split_string)

a_string = "ab_cd_ef"

parsed_string = a_string.split("_", 1)
print(parsed_string)

#7. Lists and operation

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = list(("apple", "banana", "cherry"))
print(thislist)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c )

c *= a
print ("Line 3 - Value of c is ", c)

c /= a
print ("Line 4 - Value of c is ", c)

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']



# Program to calculate the factorial of a positive integer:

n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
    raise ValueError('You must enter a non negative integer')

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(factorial)

row = int(input('Enter any number for your pattern:'))

count = 0;
for i in range(0, row):
    for j in range(0, row-i-1):
         print(end=" ")

    count = count+1
    for k in range(0, i+count):
        print("*", end = "")

    print(" ")



def check_even_odd(n):
    if n%2 ==0:
        print('The number is even')
    else:
        print('The number is odd')
n = int(input('Enter any Integer:'))
check_even_odd(n)

import math
def check_prime(n):
    count = 0
    for i in range(2, math.floor(math.sqrt(n))+1):

        if n % i == 0:
            print('The number is not prime')
            break
        count = count+1
    if count+2 == math.floor(math.sqrt(n)+1):
        print('The number is prime ')

n = int(input('Enter any Integer:'))
check_prime(n)

x = int(input('ENTER THE VALUE OF X:'))
y = int(input('ENTER THE VALUE OF Y:'))
if x == y:
		print("x and y are equal")
else:
		if x < y:
			print("x is less than y")
		else:
			print("x is greater than y")
num = int (input('Enter any integer:'))

for i in range(1,11):
	print(num," ", '*', " ", i ," ", '=', num*i)
n = int(input('Enter an integer:'))
reverse = 0
while n>0:
	digit = n%10
	reverse = (reverse*10)+digit
	n = n//10
print(' Reverse of the given integer is: ', reverse)


import calendar

year = int(input('Enter any year:'))
month= int(input('Enter any month:'))
print(calendar.month(year,month))

x= input('Enter your name:')
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

  x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
