alpha = 'abcdefghijklmnopqrstuvwxyz'

i = 30
print(alpha[i % 26])  # Output: e

s = "sudarshan"

t = ''
i = 0   
alpha.index(s[2])  
print(alpha.index(s[2]))  
print((alpha.index(s[2])+5)%26)  
print(alpha[(alpha.index(s[2])+5)%26])  

t = t + alpha[(alpha.index(s[i])+5)%26]
print(t)  
t = t + alpha[(alpha.index(s[i+2])+5)%26]
print(t)  









