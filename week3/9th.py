print("Today is ")
print(5,7,2026, sep = "/")

# ISKO AISE LIKHKAR DEKHO :-
print("Today is" , end=" ")
print(5,7,2026, sep = "/")


n = int(input("enter a number : "))

for i in range(1,11):
    # print(n , "X" , i , "=" ,n*i)
    # print(f'{n} x {i} = {n*i}')
    # print('{0} x {1} = {2}'.format(n,i,n*i))
    print('%d x %d = %d' % (n,i,n*i))



pi = 22/7
print(pi)
print(f'value of PI = {pi}')
print('value of PI = {0}'.format(pi))
print('value of PI = %f' % (pi))

# Formatting 
print(f'value of PI = {pi:.2f}')
print('value of PI = {0:.2f}'.format(pi))
print('value of PI = %.2f' % (pi))

print("{0}".format(1))
print("{0}".format(11))
print("{0}".format(111))
print("{0}".format(1111))
print("{0}".format(11111))

# Right allign
print("{0:5d}".format(1))
print("{0:5d}".format(11))
print("{0:5d}".format(111))
print("{0:5d}".format(1111))
print("{0:5d}".format(11111))











