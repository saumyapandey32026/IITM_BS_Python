n = int(input("your amount : "))
r = int(input("rate : "))

def compound_int(t):
    if t==0:
        return n
    return compound_int(t-1)*(1 + r/100)

print(compound_int(3))                              
























































