import string

def create_caesar_dictionary():
    l = string.ascii_lowercase
    l = list(l)

    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i+3)%26]
    print(d)

create_caesar_dictionary()



f=open('sherlock.txt','r')
g=open('encrypted_sherlock.txt','w')

c=f.read(1)
d = create_caesar_dictionary()
while (c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()











