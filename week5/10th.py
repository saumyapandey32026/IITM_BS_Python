# FUNCTIONAL PROGRAMMING MAIN IDEAS 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚
# 🦚🦚🦚🦚🦚🦚 1. Function ko variable me store kar sakte hain.
# def greet():
#     print("Namaste!")

# x = greet     # 🦚🦚 1st
# x()
# greet()       # 🦚🦚 2nd 
# y = greet()   # 🦚🦚 3rd

# 🦚🦚🦚🦚🦚🦚 2. Function ko argument bana sakte hain.
# def square(x):
#     return x*x

# def calculate(fun, value):
#     return fun(value)

# print(calculate(square,5))

# 🦚🦚🦚🦚🦚🦚 3. Function return bhi kar sakte hain. 

# def choose():

#     def hello():
#         print("Hello")

#     return hello

# x = choose()
# x()

#  mera doubt section 
# def cal(x):
#     return x*x
# # y = cal
# # print(y(5))
# y = cal(5)
# print(y)
'''Case 1
y = cal
Iska matlab
Function ko store karo.

Diagram:
cal
 │
 ▼
Function object

y
 │
 ▼
Same function object

Ab
print(y(5))
matlab
y(5)
↓
cal(5)
↓
25
Output
25
Yahan y ek function hai.

Case 2
y = cal(5)
Yahan pehle function call hoga.
cal(5)
↓
25

Ab
y = 25
Diagram
y
│
▼
25

Ab
print(y)
Output
25

Agar tum likho
y(5)
to error aayega.
TypeError
'int' object is not callable

Kyunki
25(5)
aisa thodi hota hai. 😂

Ek line me difference
Ye
y = cal
Store karta hai
Function
Ye
y = cal(5)
Store karta hai
Function ka result'''



# 🦚🦚🦚🦚🦚🦚 LAMBDA 
# def add(a,b):
#     return a+b
# print(add(3,7))
# # both are equivalent 
# add = lambda a,b : a+b
# print(add(3,7))


# 🦚🦚🦚🦚🦚🦚 enumerate()
# fruits = ["apple", "banana", "mango"]
# for i in range(len(fruits)):
#     print(i, fruits[i]) 

# with enumerate()  
# fruits = ["apple", "banana", "mango"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# Ye andar se karta kya hai?
# Socho list
# ["apple","banana","mango"]
# enumerate() ise temporarily bana deta hai
# (0,"apple")
# (1,"banana")
# (2,"mango")

# Isliye
# for x in enumerate(fruits):
#     print(x)
# # Output
# (0, 'apple')
# (1, 'banana')
# (2, 'mango')

# Notice
# x ek tuple hai.

#  🦚🦚🦚🦚🦚🦚 zip()
names = ["Ram","Shyam","Aman"]
marks = [90,85,70]

#  NORMAL WAY 
for i in range(len(names)):
    print(names[i], marks[i])

# USING ZIP
for x in zip(names, marks):
    print(x)

for name, mark in zip(names, marks):
    print(name, mark)

# 🦚🦚🦚🦚🦚🦚 Agar length different ho
a = [1,2,3]
b = [10,20]
print(list(zip(a,b)))


#  🦚🦚🦚🦚🦚🦚 map()
numbers = [1,2,3,4]
# Square chahiye.

# Normal
square=[]
for x in numbers:
    square.append(x*x)
print(square)

# map()
result = map(lambda x:x*x, numbers)
print(list(result))

# 2nd eg 
a=[1,2,3]
b=[10,20,30]
result = map(lambda x,y:x+y, a,b)
print(list(result))

#  🦚🦚🦚🦚🦚🦚 filter
numbers=[1,2,3,4,5,6]

# Sirf even chahiye.

# Normal
even=[]
for x in numbers:
    if x%2==0:
        even.append(x)

# Filter
result = filter(lambda x:x%2==0, numbers)
print(list(result))

# 2nd eg
names=["Ram","Aman","Si","Shyam"]

# 3 se bade naam
result=filter(lambda x:len(x)>3,names)
print(list(result))



# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
# Standard functions using 'def'
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Equivalent functions using 'lambda'
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

# Printing the outputs
print(add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))

# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ enumerate()
fruits = ["mango", "apple", "banana", 
          "orange", "pineapple", "watermelon", "guava", 
          "kiwi"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

fruits = ["mango", "apple", "banana", 
          "orange", "pineapple", "watermelon", "guava", 
          "kiwi"]

for fruit in enumerate(fruits):
    print(fruit)


# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️  zip()
fruits = ["mango", "apple", "banana", 
          "orange", "pineapple", "watermelon", "guava", 
          "kiwi"]
size = [5, 5, 6, 6, 9, 10, 5, 4]

print(zip(fruits, size))
print(list(zip(fruits, size)))
print(dict(zip(fruits, size)))
print(dict(zip(size,fruits)))

# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️  map()
a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]
#c = a + 1

def sub(x, y):
    return x - y

def incr(x):
    return x + 1

# Pehle do lists ko subtract kiya
c = map(sub, a, b)

# Fir a ke har element ko 1 se badhaya
c = map(incr, a)
print(list(c))

# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️  Map aur Filter ka mix use   
import math

a = [25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    if n >= 0:
        return n

# Pehle negative numbers filter honge, fir bache numbers ka square root nikalega
c = map(square_root, filter(is_positive, a))
print(list(c))

# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ Map se direct Square Root
import math

a = [25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

c = map(square_root, a)
# print(list(c))



























