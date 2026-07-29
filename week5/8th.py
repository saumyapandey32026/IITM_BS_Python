# # Problem 1 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚

# sen = input("enter a sentence : ")
# #🦚🦚🦚🦚🦚
# # def upper(s):              🦚🦚🦚🦚🦚ye tha mera confusion 
# #     upper = 0
# #     for c in s:
# #         for k in c:
# #             if k.isupper():
# #                 upper += 1
# #     return upper
# # uSen = upper(sen)
# def upper(s):
#     upper = 0
#     for c in s:
#         if c.isupper():
#             upper += 1
#     return upper
# uSen = upper(sen)
# print(f'\nnumber of upper case letters in sentence : {uSen}')

# #🦚🦚🦚🦚🦚
# # def lower(s):
# #     lower = 0
# #     for c in s:
# #         for k in c:
# #             if c.islower():
# #                 lower += 1
# #     return lower
# # lSen = lower(sen)
# def lower(s):
#     lower = 0
#     for c in s:
#         if c.islower():
#             lower += 1
#     return lower
# lSen = lower(sen)
# print(f'\nnumber of lower case letters in sentence : {lSen}')


# #🦚🦚🦚🦚🦚
# # def total_char(s):
# #     tchar = 0
# #     for c in s:
# #         for k in c:
# #              tchar += 1
# #     return tchar
# # tchar = total_char(sen)
# def total_char(s):
#     tchar = 0
#     for c in s:
#              tchar += 1
#     return tchar
# tchar = total_char(sen)
# print(f'\ntotal number of characters in sentence : {tchar}')
# # my mrthod 🦚🦚🦚🦚🦚


# #🦚🦚🦚🦚🦚
# def nWords(s):
#     w = s.split()
#     return len(w)
# totalWords = nWords(sen)
# sir ka method : 🦚🦚🦚🦚🦚 
# def nWords(s):             
#     words = 1
#     for c in s:
#         if c == " ":
#             words += 1
#     return words
# totalWords = nWords(sen)

# print(f'number of words in sentence : {totalWords}')



# 🦚🦚🦚🦚🦚🦚🦚EXTRA🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 yaar punctuation and special chars htane ka tarika

# import string

# def clean_and_count_words(s):
#     # Yeh saare punctuation marks (!, @, #, $, ., , etc.) ki list nikalta hai
#     punctuations = string.punctuation
    
#     # Yeh ek mapping table banata hai jo punctuations ko 'None' (kuch nahi) me badal deta hai
#     table = str.maketrans('', '', punctuations)
    
#     # Sentence se punctuation hatayein
#     cleaned_s = s.translate(table)
    
#     # Ab words count karein
#     words = cleaned_s.split()
#     return len(words)

# # Test karte hain
# sen = "Hello, World! Kaise ho? #Python_Programming..."
# print(f"Total Words: {clean_and_count_words(sen)}") 
# # Output: 5 (Hello, World, Kaise, ho, PythonProgramming)





# 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚PROBLEM 2 PERIMETER AND AREA OF CIRCLE AND RECTANGLE

#🦚🦚🦚🦚🦚🦚 yhan dekho jab input rectangle tab error aata tha since circle wala if execute hi nhi hua aur rect. wale if ke pahle hi return area hai , isliye error 
# shape = input("what is the shape : ")
# def Area():
#     if shape == "circle":
#         r = int(input("enter radius of circle : "))
#         area = (22/7)*r*r
#     return area             
#     if shape == "rectangle":
#         l = int(input("enter lth of rectangle: "))
#         b = int(input("enter width of rectangle : "))
#         area = l*b
#     return area 

# print(Area())

#🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 method 2.
# shape = input("what is the shape : ")
# def Area():
#     if shape == "circle":
#         r = int(input("enter radius of circle : "))
#         area = (22/7)*r*r            
#     elif shape == "rectangle":
#         l = int(input("enter lth of rectangle: "))
#         b = int(input("enter width of rectangle : "))
#         area = l*b
#     return area 

# print(Area())

#🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 3rd way
# shape = input("what is the shape : ")
# def Area():
#     if shape == "circle":
#         r = int(input("enter radius of circle : "))
#         area = (22/7)*r*r
#         return area             
#     elif shape == "rectangle":
#         l = int(input("enter lth of rectangle: "))
#         b = int(input("enter width of rectangle : "))
#         area = l*b
#         return area 
#     else:
#         return "Invalid shape"

# print(Area())


#🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚  Perimeter 
# def Perimeter():
#     if shape == "circle":
#             r = int(input("enter radius of circle : "))
#             peri = 2*(22/7)*r
#             return peri            
#     elif shape == "rectangle":
#             l = int(input("enter lth of rectangle: "))
#             b = int(input("enter width of rectangle : "))
#             peri = 2*(l+b)
#             return peri 
#     else:
#             return "Invalid shape"
# print(Perimeter())


# 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 is baar perimeter area dono ek sath 
# shape = input("what is the shape : ")
# def PerimeterArea():
#     if shape == "circle":
#             r = int(input("enter radius of circle : "))
#             peri = 2*(22/7)*r
#             area = (22/7)*r*r
#             return peri, area            
#     elif shape == "rectangle":
#             l = int(input("enter lth of rectangle: "))
#             b = int(input("enter width of rectangle : "))
#             peri = 2*(l+b)
#             area = l*b
#             return peri , area
#     else:
#             return "Invalid shape"
# print(PerimeterArea())

#🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 perimeter ya area jo bolo aap 
# shape = input("what is the shape : ")
# want = input("kya calculate karu ? \n")
# def PerimeterArea():
#     if shape == "circle":
#             r = int(input("enter radius of circle : "))
#             if want == "perimeter":
#                    peri = 2*(22/7)*r
#                    return peri
#             elif want == "area":
#                     area = (22/7)*r*r
#                     return area            
#     elif shape == "rectangle":
#             l = int(input("enter lth of rectangle: "))
#             b = int(input("enter width of rectangle : "))
#             if want == "parameter":
#                 peri = 2*(l+b)
#                 return peri
#             elif want == "area":
#                 area = l*b
#                 return peri , area
#     else:
#             return "Invalid shape"
# print(PerimeterArea())




#  🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚  yaar agar input cicle ya rectangle nhi balki exit aaye tab output stop execution aaye ye code kaise likhu
# 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 m1
# shape = input("What is the shape: ")

# def Area():
#     if shape == "exit":
#         return "Stop Execution"

#     elif shape == "circle":
#         r = int(input("Enter radius: "))
#         return (22/7) * r * r

#     elif shape == "rectangle":
#         l = int(input("Enter length: "))
#         b = int(input("Enter breadth: "))
#         return l * b

#     else:
#         return "Invalid Shape"

# print(Area())
# Input:
# exit
# Output:
# Stop Execution

# 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 m2    Method 2 - exit() function, Agar tum sach me program ko wahi khatam karna chahti ho.
# shape = input("What is the shape: ")

# if shape == "exit":
#     print("Stopping execution...")
#     exit()

# def Area():
#     if shape == "circle":
#         r = int(input())
#         return (22/7) * r * r

#     elif shape == "rectangle":
#         l = int(input())
#         b = int(input())
#         return l * b

# print(Area())
#  #Input:
# exit
# Output:
# Stopping execution...
# Uske baad program wahin khatam.

# 🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 m3    Method 3 - break (Menu programs ke liye) , Agar repeatedly input lena hai.

# while True:
#     shape = input("Shape: ")

#     if shape == "exit":
#         print("Stopping...")
#         break

#     elif shape == "circle":
#         r = int(input("Radius: "))
#         print((22/7) * r * r)

#     elif shape == "rectangle":
#         l = int(input("Length: "))
#         b = int(input("Breadth: "))
#         print(l * b)

#     else:
#         print("Invalid Shape")

# Ye tab tak chalta rahega jab tak user exit na likhe.

# Example:

# Shape: circle
# Radius: 5
# 78.57

# Shape: rectangle
# Length: 4
# Breadth: 6
# 24

# Shape: exit
# Stopping...

'''Problem 2: Write a Python code using functions to calculate area and perimeter'''
'''Approach 1: Standard code'''
# PI = 22 / 7

# def circle_area(r):
#     return (PI * r * r)

# def circle_perimeter(r):
#     return (2 * PI * r)

# def rectangle_area(l, b):
#     return (l * b)

# def rectangle_perimeter(l, b):
#     return (2 * (l + b))

# r = float(input('\nEnter the radius of the circle: '))
# cArea = circle_area(r)
# print(f'\nArea of circle with radius {r} = {cArea} sq. units')
# cPerimeter = circle_perimeter(r)
# print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units\n')

# l = float(input('Enter the length of the rectangle: '))
# b = float(input('\nEnter the breadth of the rectangle: '))
# rArea = rectangle_area(l, b)
# print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq. units')
# rPerimeter = rectangle_perimeter(l, b)
# print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units\n')


'''Problem 2: Write a Python code using functions to calculate area and perim...'''
'''Approach 2: Menu driven code'''
# PI = 22 / 7

# def circle_area(r):
#     return (PI * r * r)

# def circle_perimeter(r):
#     return (2 * PI * r)

# def rectangle_area(l, b):
#     return (l * b)

# def rectangle_perimeter(l, b):
#     return (2 * (l + b))

# polygon = ""
# while (polygon != 'exit'):
#     print('\nPOLYGONS\ncircle\nrectangle\nexit')
#     polygon = input('\nChoose the polygon type or exit: ')
    
#     if (polygon == 'circle'):
#         r = float(input('Enter the radius of the circle: '))
#         print(f'Area = {circle_area(r)}, Perimeter = {circle_perimeter(r)}')
        
#     elif (polygon == 'rectangle'):
#         l = float(input('Enter the length of the rectangle: '))
#         b = float(input('Enter the breadth of the rectangle: '))
#         print(f'Area = {rectangle_area(l, b)}, Perimeter = {rectangle_perimeter(l, b)}')
        
#     elif (polygon == 'exit'):
#         break
        
#     else:
#         print('Please select the correct polygon type or exit')



'''Problem 2: Write a Python code using functions to calculate area and perimeter'''
'''Approach 2: Menu driven code'''

# PI = 22 / 7
# import math            # more accurate PI value
# PI = math.pi

# def circle_area(r):
#     return (PI * r * r)

# def circle_perimeter(r):
#     return (2 * PI * r)

# def rectangle_area(l, b):
#     return (l * b)

# def rectangle_perimeter(l, b):
#     return (2 * (l + b))

# polygon = ""
# while (polygon != 'exit'):
#     print("\nPOLYGONS\ncircle\nrectangle\nexit")
#     polygon = input("\nChoose the polygon type or exit: ")
#     property = ""
    
#     if (polygon == 'circle'):
#         r = float(input('\nEnter the radius of the circle: '))
#         while (property == ""):
#             print('\nCIRCLE PROPERTIES\narea\nperimeter\nback')
#             property = input('\nChoose the circle property or go back: ')
            
#             if (property == 'area'):
#                 print(f"Area of circle = {circle_area(r)}")
#                 property = "" # Menu dobara dikhane ke liye
#             elif (property == "perimeter"):
#                 print(f"Perimeter of circle = {circle_perimeter(r)}")
#                 property = "" # Menu dobara dikhane ke liye
#             elif (property == "back"):
#                 break
#             else:
#                 print('Please select the correct polygon property')
#                 property = ""
                
#     elif (polygon == 'rectangle'):
#         l = float(input('\nEnter the length of the rectangle: '))
#         b = float(input('Enter the breadth of the rectangle: '))
#         while (property == ""):
#             print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
#             property = input('\nChoose the rectangle property or go back: ')
            
#             if (property == 'area'):
#                 print(f"Area of rectangle = {rectangle_area(l, b)}")
#                 property = ""
#             elif (property == "perimeter"):
#                 print(f"Perimeter of rectangle = {rectangle_perimeter(l, b)}")
#                 property = ""
#             elif (property == "back"):
#                 break
#             else:
#                 print('Please select the correct polygon property')
#                 property = ""
                
#     elif (polygon == 'exit'):
#         break
#     else:
#         print("Please select the correct polygon type or exit")



# PROBLEM 3  🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚🦚 given co-ordinates will form triangle or not  ??
'''Problem 3: Write a Python code using functions which checks whether the 3 points form a triangle'''
'''Approach 1: Using distance between points'''

# def distance(xi, yi, xj, yj):
#     return ((((xj - xi) ** 2) + ((yj - yi) ** 2)) ** 0.5)

# def isTriangle(max, a, b):
#     if ((a + b) > max):
#         print('\nTriangle')
#     else:
#         print('\nNot a triangle')

# x1 = float(input('Enter x coordinate of 1st point: '))
# y1 = float(input('Enter y coordinate of 1st point: '))
# x2 = float(input('\nEnter x coordinate of 2nd point: '))
# y2 = float(input('Enter y coordinate of 2nd point: '))
# x3 = float(input('\nEnter x coordinate of 3rd point: '))
# y3 = float(input('Enter y coordinate of 3rd point: '))

# d1 = distance(x1, y1, x2, y2)
# print(f'\nDistance between points ({x1}, {y1}) and ({x2}, {y2}) = {d1}')
# d2 = distance(x2, y2, x3, y3)
# print(f'\nDistance between points ({x2}, {y2}) and ({x3}, {y3}) = {d2}')
# d3 = distance(x3, y3, x1, y1)
# print(f'\nDistance between points ({x3}, {y3}) and ({x1}, {y1}) = {d3}')

# if (d1 > d2):
#     if (d1 > d3):
#         isTriangle(d1, d2, d3)
#     else:
#         isTriangle(d3, d1, d2)
# elif (d2 > d3):
#     isTriangle(d2, d1, d3)
# else:
#     isTriangle(d3, d1, d2)


'''Problem 3: Write a Python code using functions which checks whether the in...'''
'''Approach 2: Using slope of lines connecting two points'''
import math

def slope(xi, yi, xj, yj):
    if (xi == xj):
        return (math.inf)
    else:
        return ((yj - yi) / (xj - xi))

x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('\nEnter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('\nEnter x coordinate of 3rd point: '))
y3 = float(input('Enter y coordinate of 3rd point: '))

s1 = slope(x1, y1, x2, y2)
print(f'\nSlope of the line connecting points ({x1}, {y1}) and ({x2}, {y2}) = {s1}')

s2 = slope(x2, y2, x3, y3)
print(f'\nSlope of the line connecting points ({x2}, {y2}) and ({x3}, {y3}) = {s2}')

# Triangle check karne ka logic (Agar slope barabar hai to points ek hi line mein hain)
if (s1 == s2):
    print('\nNot a triangle (Points are collinear)')
else:
    print('\nTriangle')



































































# thoda sa split aur strip ko dekhlo saumya
# s = "2026-07-080"
# print(s.split("-"))
# print(s.split("0"))

# char = "**sau*mya**pandey**"
# print(char.strip("*"))
# s = "H#$@ELL#O1@21##"
# print(s.strip("@#$"))
# m = "@@saum@ya@@@"
# print(m.strip("@@"))
# s = "ababHellobaba"
# print(s.strip("ab"))


















































