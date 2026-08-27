def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n)

print_num(5)


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(5))






































