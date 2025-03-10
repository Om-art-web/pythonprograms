def addMatrix(a, b):
    m1, n1 = sizeMatrix(a)
    m2, n2 = sizeMatrix(b)
    if m1 != m2:
        return None
    if n1!=n2:
        return None
    returnvalue = createMatrix(m1, n1)
    for i in range(m1):
        for j in range(n1):
            returnvalue[i][j] = a[i][j]+b[i][j]

    return returnvalue
def subMatrix(a,b):
    m1,n1 = sizeMatrix(a)
    m2,n2=  sizeMatrix(b)
    if m1!=m2:
        return None
    if n1!=n2:
        return None
    returnvalue=createMatrix(m1,n1)
    for i in range(m1):
        for j in range(n1):
            returnvalue[i][j]=a[i][j]-b[i][j]

        return returnvalue
    
def multiplyMatrix(a,b):
    m1,n1 = sizeMatrix(a)
    m2,n2=  sizeMatrix(b)
    if m1!=m2:
        return None
    if n1!=n2:
        return None
    returnvalue=createMatrix(m1,n1)
    for i in range(m1):
        for j in range(n1):
            for k in range(n1):
                returnvalue[i][j]+=a[i][k]*b[k][j]
            return returnvalue


def createMatrix(m, n):
    row = [0 for x in range(n)]
    mat = [row.copy() for x in range(m)]
    return mat


def sizeMatrix(a):
    r = len(mat)
    c = len(mat[0])
    return r, c


def printMatrix(a):
    print()
    r, c = sizeMatrix(a)
    for i in range(r):
        for j in range(c):
            print(a[i][j], end="\t")
        print()
    print()


def compareMatrix(a, b):
    m1, n1 = sizeMatrix(a)
    m2, n2 = sizeMatrix(b)
    if m1 != m2:
        return False
    if n1 != n2:
        return False
    for i in range(m1):
        for j in range(m2):
            if a[i][j] != b[i][j]:
                return False
    return True
        


mat = [[6, 8,7], [2, 1, 1]]
mat2 = [[1, 2, 1], [3, 7, 1]]

result = compareMatrix(mat, mat2)
print(result)
# add = addMatrix(mat, mat2)
sub= subMatrix(mat,mat2)
# multiply=multiplyMatrix(mat,mat2)
# printMatrix(mat)
# printMatrix(mat2)
# printMatrix(add)
printMatrix(sub)
# printMatrix(multiply)