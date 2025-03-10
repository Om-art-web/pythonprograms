
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

mat = [[1, 2, 3 ], [3, 4, 5]]
print(mat, len(mat))
print(mat[1], len(mat[0]))
printMatrix(mat)


