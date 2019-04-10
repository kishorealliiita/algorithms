import os

def knapsack_max_value (wt, val, max_wt):
    n = len (wt) + 1

    matrix = [[0]*(max_wt+1) for i in range (0, n)]

    for i in range (0, n):
        for j in range (0, max_wt+1):
            if i==0 or j==0:
                matrix[i][j] = 0
            elif wt[i-1] <= j:
                matrix[i][j] = max (val[i-1] + matrix[i-1][j-wt[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    
    return matrix[n-1][max_wt]

val = [60, 100, 120]
wt = [10, 20, 30]

print (knapsack_max_value (wt, val, 50))