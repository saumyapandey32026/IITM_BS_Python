def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1)+n

print(sum(10))


# rate = 10% given 
def comp(p,n):
    if n == 1:
        return p*1.1
    else:
        return(comp(p,n-1)*1.1)

print(comp(2000,3))













































