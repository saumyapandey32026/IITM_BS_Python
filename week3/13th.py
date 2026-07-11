for i in range(1,6):
    print(i)


# break
for i in range(1,6):
    if i == 3:
        break
    print(i)
print("finished")

# continue 
for i in range(1,6):
    if i == 3:
        continue  
    print(i)
print("finished")

# 2nd example   even numbers skip ho jayenge   
for i in range(1,11):

    if i % 2 == 0:
        continue

    print(i)

# pass 
for i in range(1,6):
    if i == 3:
        pass
    print(i)
print("finished")



















