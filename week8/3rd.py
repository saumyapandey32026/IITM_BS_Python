# with open(r"C:\Users\saumy\OneDrive\Notes\PYTHON notes\Class Notes\WEEK1 Python\equivalent p.1.png","r") as s:
#     for line in s:
#         print(line)                                 .png hai isliye error aa rha hai


# "r" ki jagah "rb" likhein
# with open(r"C:\Users\saumy\OneDrive\Notes\PYTHON notes\Class Notes\WEEK1 Python\equivalent p.1.png", "rb") as s:
#     print("File successfully open ho gayi!")


# f = open("text.txt","w")          maine ye .txt file create ki yhan aur fir isko notes folder me python notes folder me daal diya 
# f.write("9983839234\n")
# f.write("9293949596\n")
# f.write("8884989090\n")
# f.write("8948567898\n")
# f.write("8948564498\n")
# f.write("8943464498\n")
# f.close()

# f = open(r"C:\Users\saumy\OneDrive\Notes\PYTHON notes\text.txt","r")
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()

f = open(r"C:\Users\saumy\OneDrive\Notes\PYTHON notes\text.txt","r")
s = f.readline()
flag = 0
print("ye hai ", s)
while(s != ''):
    s = f.readline()
    print(s)
    n = int(s)
    if n == 8948567898:
        print("the number is found")
        flag = 1
        break
if flag == 0:
    print("notttt found")

#  without break 
f = open(r"C:\Users\saumy\OneDrive\Notes\PYTHON notes\text.txt","r")
s = f.readline()
while(s != ''):
    n = int(s)
    if n == 8948567898:
        print("the number is found")
    s = f.readline()








