import os

def makeRowAndColZero (A, n, m):
    if not A:
        return A
    
    for i in range (0,n):
        for j in range (0,m):
            if A[i][j] == 0 and i !=0 and j != 0:
                A[i][0] = 0
                A[0][j] = 0
    
    for i in range (0,n):
        for j in range (0,m):
            if A[i][j] == 0:
                if A[0][j] == 0 and A[i][0] == 0:
                    k = 0
                    while k < n:
                        A[k][j] = 0
                        k += 1
                    k = 0
                    while k < m:
                        A[i][k] = 0
                        k += 1
    
    for row in A:
        print(' '.join([str(elem) for elem in row]))

    return A

A = [[1,2,3,4], [1,0,2,3], [1,1,1,1], [2,3,0,5]]

makeRowAndColZero (A,4,4)


