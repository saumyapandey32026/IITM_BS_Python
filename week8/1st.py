f = open("file.txt","w")
f.write("hello saumya")
f.close()

f = open("file.txt","a")
f.write("\nab append sikh lo thoda, dekho newline bhi de diya hai nhi to saumya se chipak kar text aata ye wala")
f.close()

# f = open("file.txt","r")
# data = f.read()
# print(type(data))
# print(data)
# f.close()

f = open("file.txt","r")
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()
# data = f.readline()            is baar ye error dega since file ko close kar diya hai 
# print(data)

f = open("file.txt","r")
line = f.readlines()
print(line)
f.close()

f = open("file.txt","w")
f.write("multiple\n")
f.write("lines\n")
f.close()

lst = ["iitm\n","data\n","science\n"]
# lst = ["iitm","data","science"]    
f = open("file.txt","w")
f.writelines(lst)
f.close()

with open("file.txt","r") as s:
    lekhni = s.read()
print(lekhni)

# with open("newFile","x") as n:
#     new = n.write("new new")

import os                       
os.remove("newFile")


















































