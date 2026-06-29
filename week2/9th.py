#  Question no. 1st 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 even or odd number
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")   

#Question no. 2nd 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 find whether the given number ends with 0 or 5
# n = int(input("Enter a number: "))

# 1st. ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
# if(n%5 == 0):
#     print(f"{n} ends with 0 or 5")
# else:
#     print(f"{n} doesn't end with 0 or 5")

# 2nd. ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
# if (n%5 == 0):
#     if((n//5)%2 == 0):
#         print(n, "ends with 0")
#     elif((n//5)%2 == 1):
#         print(n, "ends with 5")
# else:
#     print(n, "doesn't ends with 0 or 5")

# 3rd. ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ 
# if(n % 5 == 0):
#     if(n % 10 == 0):
#         print("ends with 0")
#     else:
#         print("ends with 5")
# else:
#     print("other than 0 or 5")

# Question no. 3rd 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 Grade of students 
# marks = int(input("your marks: "))

# ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ yhan kuchh extra unnecessary steps likhe hain
# if marks >= 90:
#     print("A grade")
# elif 90>marks>=80:
#     print("B grade")
# elif 80>marks>=70:
#     print("C grade")
# elif 70>marks>=60:
#     print("D grade")
# elif 60>marks>=50:
#     print("E grade")
# else:
#     print("I grade")

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ yhan kuchh redundency kam hui 
# if marks >= 90:
#     print("A grade")
# elif marks>=80:
#     print("B grade")
# elif marks>=70:
#     print("C grade")
# elif marks>=60:
#     print("D grade")
# elif marks>=50:
#     print("E grade")
# else:
#     print("I grade")

# Question no. 4th 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ ye code bhayank galat hai  
# time = input("longer or shorter ?")
# price = input("lower or higher ?")
# if (time == "longer"):
#     if (price == "higher"):
#         print("via train")
#     elif(price == "lower"):
#         print("coach")
# elif(time == "shorter"):
#         if (price == "higher"):
#            print("daytime flight")
#         elif(price == "lower"):
#            print("red eye flight")
# print("Arrive city B")

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ ye hai sahi tarika
print("travel from city A to B")
Time = int(input("enter time: "))
Longer = int(input("define longer : "))
if(Time >= Longer):
    Price = int(input("Enter price : "))
    Higher = int(input("Define higher : "))
    if (Price >= Higher):
        print("train")
    else:
        print("coach")
else:
    Price = int(input("Enter price : "))
    Higher = int(input("Define higher : "))
    if (Price >= Higher):
        print("daytime flight")
    else:
        print("red eye flight")
print("Arrive city B")












