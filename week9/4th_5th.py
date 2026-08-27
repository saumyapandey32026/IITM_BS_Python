def check0(l):
    if len(l) == 0:
        return 0
    if l[0] == 0:
        return 1
    else:
        return check0(l[1:len(l)])

ans = check0([1,2,0,6,0,4,0,5,8,9,45,0])
print(ans)










































