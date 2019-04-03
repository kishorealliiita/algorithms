import os

def rotateby90 (matrix, m, n):
    a = [[0] * n for i in range (m)]

    for row in matrix:
        print(' '.join([str(elem) for elem in row]))

    for i in range (0, n):
        for j in range (0,m):
            x = (n-1) - i
            y = j
            a[y][x] = matrix[i][j]

    for row in a:
        print(' '.join([str(elem) for elem in row]))

a = [[1, 2, 3, 4], [5, 6, 7, 8], [7, 8, 9, 10], [2,3,4,5]]

rotateby90 (a, 4, 4)

