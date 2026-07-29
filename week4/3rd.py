# t = (6)
# print(type(t))
# print(type(6))
# t = (6,)
# print(type(t))
# print(type(6))

# s = 4,5,3,7,7,2,1
# print(s)
# p = (5,6,7,4)
# a,b,c,d = p
# print(a)
# print(b)
# print(c)
# print(d)

# q = ("saumya pandey",18)
# name,age = "saumya pandey",18
# print(name)

# a1 = 12
# a2 = 34
# a1,a2 = a2,a1
# print(a1)
# print(a2)

# mutable vs immutable
# t_1 = (1,3,4)
# t_1 = t_1 +(100,)
# print(t_1)
# t_1 = t_1 + (300,200)
# print(t_1)

# # list in tuple
# t_2=([1,2],5)
# t_2[0].append(10)
# print(t_2)

import string
# T = string.ascii_letters
# print(T)
# alpha = tuple(T)
# print(alpha)
# ap = set(T)
# print(ap)
# aph = list(T)
# print(aph)
# al = tuple(list(T))
# print(al)

list_1 = string.ascii_letters
print(list_1)
list_2 = "saumyapandey#iitmadras*catalyticdhairya @ cya"
x = list(list_2)
print(x)

r = []
for char in x:                   # x ki jagah list_2 rakho no problem
    if char in list_1:
        r.append(char)
print(r)






