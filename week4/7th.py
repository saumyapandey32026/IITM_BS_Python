# def greetings():
#     print("hello")
# greetings()

# def add(a,b):
#     ans = a+b
#     print(ans)
# print(type(add(2,4)))
# add(-1,9)

# def discount(cost,d):
#     ans = cost - (cost*(d/100))
#     print(ans)
# discount(100,8)
# print(type(discount(100,8)))

# print(add(3,7) + discount(200,10))              # for now it will give you error since you are not returning anything



# def add(a,b):
#     ans = a+b
#     return ans
# print(type(add(2,4)))
# def discount(cost,d):
#     ans = cost - (cost*(d/100))
#     return ans  
# print(type(discount(100,2)))
# print(add(1,7) + discount(100,10)) 

# def subt(c,d):
#     s = c - d
#     return s
#     # print(s)  kewal print mat likhna return bhi karna otherwise nonetype....
# c = 34
# d = 30
# s = subt(c,d)+10
# print(s)


# def discount(cost,d):
#     ans=cost-(cost*(d/100))
#     return ans

# print("Enter the cost price")
# c=int(input())
# print("Enter the discount")
# disc=int(input())

# print("The final discount is: ", discount(c,disc))


#Let us write a few functions on lists.

# def list_min(l):
#     mini=l[0]
#     for i in range(len(l)):
#         if (l[i]<mini):
#             mini=l[i]
#     return mini

# def list_maxi(l):
#     maxi=l[0]
#     for i in range(len(l)):
#         if (l[i]>maxi):
#             maxi=l[i]
#     return maxi

# l=[1,2,3,4,5,-10,6,4]
# print(list_min(l))
# print(list_maxi(l))

# def list_appendbefore(l,z):
#     app = z.append(l)
#     return (z)
#     # return app        ye mat karna since append kuchh return nhi karta wo bas list ko update kar deta hai  
# l1 = [1,3,4,7]
# z1 = [100,200]
# print(list_appendbefore(l1,z1))


# def l_appendbefore(l,z):
#     newl = []
#     for i in range(len(l)):
#         newl.append(l[i])
#         # return newl
#     for i in range(len(z)):
#         newl.append(z[i])
#     return newl
# print(l_appendbefore(l1,z1))
























