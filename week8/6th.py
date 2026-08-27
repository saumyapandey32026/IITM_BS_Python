f = open("file_6.txt","w")
f.write("abcdefghijklmnopqrstuvwxyz")
f.close()

f = open("file_6.txt","r")
f.seek(3)
data = f.read(5)
print(data)
print(f.tell())























