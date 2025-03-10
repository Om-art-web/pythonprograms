
def size(mat):
    return len(mat), len(mat[0])


def XReverseMatrix(mat):
    my, mx = size(mat)
    for y in range(my):
        left = 0
        right = mx-1
        while left < right:
            mat[y][left], mat[y][right] = mat[y][right], mat[y][left]
            left += 1
            right -= 1
    return mat


def YReverseMatrix(mat):
    my, mx = size(mat)
    top = 0
    down = my-1

    while top < down:
        for x in range(mx):
            mat[top][x], mat[down][x] = mat[down][x], mat[top][x]
        top += 1
        down -= 1
    return mat


def printMatrix(mat):
    my, mx = size(mat)
    print()
    for y in range(my):
        for x in range(mx):
            print(mat[y][x], end="\t")
        print()


def doubleMatrix(mat):
    my, mx = size(mat)
    print()
    for y in range(my):
        left = 0
        right = mx-1
        while left < right:
            mat[y][right] = mat[y][left]
            left += 1
            right -= 1
    return mat


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# printMatrix(a)
# YReverseMatrix(a)
printMatrix(a)
doubleMatrix(a)
printMatrix(a)
