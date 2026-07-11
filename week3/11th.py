s = "vibgyor"
t = "vibgyor"
count = 0
for i in range(7):
    for j in range(7):
        print(i,j,s[i],s[j])
        count += 1
print(count , "no. of ways to wear shirts for 2 students")