def initialize_mat(dim):
    c = []
    for i in range(dim):
        c.append([])
        for j in range(dim):
            c[i].append(0)
    return c

m = initialize_mat(3)
print(m)





def dot_prod(u,v):                # assume that u and v have same order
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + u[i]*v[i]
    return ans

x = [3,4]
y = [2,3]
print(dot_prod(x,y))
print(dot_prod([10,20],[4,3]))





A = [[1,2,3],[5,6,7],[8,9,10]]
def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l 

print(row(A,2))




def column(M,j):
    dim = len(M)
    l = []
    for i in range(dim):
        l.append(M[i][j])
    return(l)

print(column(A,1))

       
x = [[10,4,-2],[4,1,3],[8,2,11]]
y = [[1,2,15],[5,10,7],[1,-4,10]]

def mat_mul(A,B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            # C[i][j] = ith row of A * jth column of B
            C[i][j] = dot_prod(row(A,i),column(B,j))
    # return(C[i][j])            # return C kro tab puri matrix milegi 
    return C

print(mat_mul(x,y))




















