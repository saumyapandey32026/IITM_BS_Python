# import random as r
# print(r.random())
# print(r.randint(10,12))
# print(r.randrange(10,12))

# # assignment operator right to left
# a,b,c = 3,4,2
# print(a)
# print(b)
# print(c)
# a = b = c
# print(a)
# print(b)
# print(c)

# d = 10
# m = 5
# y = 2026
# b = "saumya"
# print("today's date is", d,m,y)
# print("today's date is", d,m,y,sep="/")
# print("today's date is", d,m,y,b,"ram",sep="/")
# print("today's date is\t", d,m,y,sep="/")
# print("today's date is\n", d,m,y,sep="/")
# print("today's date is", end= " ")
# print(d,m,y,sep="/")

# formatting is something where I need to pay attention
# n = 2
# m = 5
# print(f"{n}*{m} = {n*m}")
# print('{0}*{1} = {2}'.format(n,m,n*m))
# print("%d * %d = %d" % (n,m,n*m))
# print('{0:5d}'.format(0))
# print('{0:5f}'.format(0))
# print('{0:10f}'.format(3))
# print('{0:15f}'.format(3))
# print('{0:20f}'.format(3))

# l = [2,4,3,5]
# # l.extend(4)           int is not iterable
# l.append(4)
# print(l)
# l.extend([3,4])
# print(l)
# l.extend((40,5))
# print(l)
# l.extend({4:"ram",54:"shyam"})
# print(l)
# b = [20,40,33,50,43]
# x = b.pop(2)
# print(x)
# print(b.pop(3))
# print(b)
# b.sort(reverse=True)
# print(b)
# b.insert(1,"riya")
# print(b)
# b.remove("riya")
# print(b)
# b.reverse()
# print(b)
# b.clear()
# print(b)

# c = ["ram",45,90,4.5,"cya"]
# x2 = c[:]
# print(x2)
# print(x2[:])

# d = [3,56,2]
# e = [4,3,5]
# x3 = d+e
# x4 = e*2
# x5 = sorted(e)
# x6 = sorted(x3)
# x7 = sorted(x4)
# print(x3)
# print(x4)
# print(x5)
# print(x6)
# print(x7)

# s = {2,4,3,"rajiya",54}
# print(s.pop())
# s.pop(3)           ye error dega since set me indexing nhi hoti 
# print(s)
# s.update(200)   200 is int and it is not iterable   
# s.update([2,45,32])
# s.update("XYZ")
# s.update("saumya","radha","MOHAN")
# # s.update({"saumya":100, 50:"queen"})
# print(s)
# s.add(500)            # takes exactly one argument 
# print(s)
# s.add("ramya")
# print(s)
# s.remove('M')
# s.remove('rajiya')
# s.remove('radha')      error aa jayega isme
# s.discard('radha')         # par isme nhi aayega  
# print(s)
# s.clear()
# print(s)

# a = {2,3,39,2}
# b = {40,39,50}
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(a.copy())

# c = {23,45,34}
# # c.add([40,30])     error since set ke elements unique hote hain, can't be mutable
# c.add((30,40))
# print(c)

# # TUPLES 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚
# t = 4,5,3
# print(t)

# GrPA 1 WEEK 4 
# int_iterable = range(1,10,3)
# print(int_iterable)
# a = reversed(int_iterable)
# print(a)
# b = list(reversed(int_iterable))
# print(b)

s1 = {1,4,3}
s2 = {4,65,87}
# s1.update(s2)
# print(s1)
# s1.update(s1)
# print(s1)
# s2.update(s1)
# print(s2)
# s1.difference_update(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1^(s2))
print(s1-s2)
print(s1)

a = {1,2,3,4}
b = {1,2,3,4,5,6}
print(a.isdisjoint(b))













