# a_ = 4
# _a = 7
# a_va =   4

# y = 2.345
# print(int(-y))

# flag = True
# if flag == True:
#     print("works")

# if flag:
#     print("works")


# bool_var = bool(input("True or False : "))
# bool_var = False
txt = input("True or False: ")
bool_var = (txt == "True")
x = 4
if bool_var:
     x = x + 10 
     print("ye if ke sath " ,x)    
bool_var = not bool_var 
if bool_var: 
    x = x + 1 
    print("ye if execute hi nhi hoga since False ho gya hai " , x)
else: 
    x = x - 1 
    print("ye else ke sath :" , x)
print("at the end x apni updated value ke sath " ,x)


# E_1 = bool(input("E_1 = "))
# E_2 = bool(input("E_2 = "))
# E_3 = bool(input("E_3 = "))
# if E_1:
#     a = 1
# if E_2:
#     a = 2
# if E_3:
#     a = 3
# print(a)

# print('\\')

# a,b,c,d = input("enter ")
# print(a , b , c , d)  
# print(a)
# print(b)
# print(c)
# print(d)

# a,b,c,d = input("enter ").split()
# print(a , b , c , d)  
# print(a)
# print(b)
# print(c)
# print(d)

#  3rd.
# x,y,z = 1,2,3
# x=y=z                    #  assignments operator associativity : right to left
# print(x)


name = input() 
if name.isalpha(): 
    print('This is a valid name') 
else: 
    print('This is not a valid name')

