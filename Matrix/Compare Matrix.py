def sizeMatrix(a):
    m = len(mat)
    n = len(mat[0])
    return m, n


def printMatrix(a):
    print()
    m, n = sizeMatrix(a)
    for i in range(m):
        for j in range(n):
            print(a[i][j], end="\t")
        print()
    print()
def compareMatrix(a,b):
    m1,n1=sizeMatrix(a)
    m2,n2=sizeMatrix(b)
    # print(m1,n1,m2,n2)
    if m1!=m2:
        return False
    if n1!=n2:
        return False
    for i in range(m1):
        for j in range(n2):
            if a[i][j]!=b[i][j]:
                return False
    return True

mat=[[1,1,1],[1,1,1]]
mat2=[[1,1,1],[1,1,2-1]]
result=compareMatrix(mat,mat2)
print(result)