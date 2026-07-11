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

# using for loop 
# n = int(input("number : "))
# if(n>0):
#     fac = 1
#     for i in range(1,n+1):
#         fac = fac*i
#     print(fac)
# else:
#     print("not defined")

# 2nd. no. of digits in the given number
# num = abs(int(input("number = ")))
# count = 1
# while(num > 9):
#     num = num//10
#     count = count + 1
# print(count)

#using for loop
# num = abs(int(input("number = ")))   # agar abs nhi bnaya to negative numbers me - ko bhi ek character samjhakar no. of digits badha dega 1
# strNum = str(num)                      
# count = 0
# for i in strNum:
#     count += 1
# print(count)


# 3rd. Reverse the digits
# num = int(input("number = "))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10

# while(absNum > 0):
#         r = absNum % 10
#         absNum = absNum // 10
#         rev = rev * 10 + r
# if(num>0):
#         print(rev)
# else:
#         print(-rev)


# using for loop 
# num = int(input("enter a number : "))
# absStrNum = str(abs(num))
# rev = ''
# for i in absStrNum:
#     rev = i + rev
# if num >= 0:
#     print(rev)
# else:
#     print("-" + rev)



#   Palindrome or not
# num = int(input("enter a number : "))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum//10
# while absNum > 0:
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r
# if num>0:
#     rev = rev 
# else:
#     rev = rev - 2*rev
# if num == rev:
#     print("palindrome")
# else:
#     print("not a palindrome")


# using for loop 
# num = int(input("enter a number : "))
# absStrNum = str(abs(num))
# rev = ''
# for c in absStrNum:
#     rev = c + rev
# if num > 0:
#     rev = int(rev)
# else:
#     rev = "-" + rev
#     rev = int(rev)
# if num == rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# yar thoda sa aur dimag lgakar mai bhi ye kar sakti thi🤣🤣

# num = int(input("enter a number : "))
# absStrNum = str(abs(num))
# rev = ''
# for c in absStrNum:
#     rev = c + rev
# if num < 0:
#     rev = '-' + rev
# if num == int(rev):
#     print("palindrome")
# else:
#     print("not a palindrome")


# whether the given number is prime ??
# num = int(input("enter a number: "))
# absNum = abs(num)
# for i in range(2,num):
#     if absNum % i == 0:
#         print("not prime")
#     else:
#         print("prime")
 

 # sum of no. of digits 
# num = int(input("enter a number : "))
# absStrNum = str(abs(num))
# sum = 0

# for i in range(1,(len(absStrNum)+1)):
#     absNum = int(absStrNum)                     # ye wali line ke wajah se baar baar absNum update hokar same value le le rha hai, isliye for loop nhi use kro
#     digit = absNum % 10
#     absNum = absNum // 10
#     sum = sum + digit
# print(sum)

#  ye dekho sahi tarika -
# n = int(input("enter a number: "))
# absNum = abs(n)
# sum = 0
# while absNum > 0:
#     digits = absNum % 10
#     absNum = absNum // 10
#     sum = sum + digits
# print(sum)


# divisible by 3 or 5 , less than given number
n = int(input("enter a number : "))
sum = 0
sum_2 = 0
sum_3 = 0
list = []
for i in range(1,n):
    if i%3 == 0:
        sum = sum + 1
        print(i)
        print(sum ,"times divisible by 3")
    elif i%5 == 0:
        sum_2 += 1
    else:
        sum_3 += 1
# print(sum ,"times divisible by 3")
print(sum_2 ,"times divisible by 5")
print(sum_3 ,"times not divisible")
        















