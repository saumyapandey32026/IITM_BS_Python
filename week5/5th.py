r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
B=[]
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C=[[0,0,0],[0,0,0],[0,0,0]]

dim=3

#C[2][1] is the dot product of the 2nd row of A
# and the 1st column of B

for i in range(dim):
    k = 0
    for j in range(dim):
        C[i][j] += A[i][k]*B[k][j]
        k += 1
print(C)
# C[i][j] = dot product of A[i][...] and B[...][j]

for i in range(dim):
    k = 0
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k]*B[k][j]
print(C)

# using numpy module
import numpy
x = numpy.asmatrix(A)
y = numpy.asmatrix(B)
print(x)
print(y)
print(x*y)








