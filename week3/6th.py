# adds the first 10 integers  
# 1st way
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

# 2nd way 
n = int(input("enter a number : "))
sum = 0
for i in range(1,n+1):               # first n natural no.s ka sum ke liye n+1 kiya 
    sum = sum + i
print(sum)