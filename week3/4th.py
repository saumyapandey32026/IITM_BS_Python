# Q1.
# n = int(input("number : "))
# if(n>1):
#     i = 1
#     fac = 1
#     while(i<=n):
#         fac = fac * i
#         i += 1
#     print(fac)
# else:
#     print("not defined")


#Q2.  no. of digits in the given number
# num = abs(int(input("enter a number : ")))     # abs isliye since -ve no.s bhi included hain , -9 me no. of digits 1
# digits = 1
# while(num > 9):
#     num = num // 10
#     digits = digits + 1  
# print(digits)


#Q3. Reverse the digits in the given number
# num = int(input("enter a number : "))
# absNum = abs(num)

# if(num >=  0):
#     rev = num % 10
#     num = num // 10
#     while(num > 0):
#         r = num % 10
#         num = num // 10
#         rev = rev * 10 + r
#     print(rev)
# else:
#     rev = absNum % 10
#     absNum = absNum // 10
#     while(absNum > 0):
#         r = absNum % 10
#         absNum = absNum // 10
#         rev = rev * 10 + r
#     print(rev - 2*rev)

#Method 2
# num = int(input("enter a number : "))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10
# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r
# if(num>0):
#     print(rev)
# else:
#     print(-rev)               # print(rev - 2*rev)

        
# Q5. palindrome or not?
n = abs(int(input("enter a number :")))
original = n
rev = n % 10
n = n // 10
while(n > 0):
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
if(original == rev):
    print("palindrome")
else:
    print("not a palindrome")

# Method 2.  Sir ka method
# num = int(input("enter a number : "))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10
# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r
# if(num<0):
#     rev = rev - 2*rev
# if(num == rev):
#     print("palindrome")
# else:
#     print("not a palindrome")








