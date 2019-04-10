import os

def longest_subsequence (s1, s2):
    row = len(s1) + 1
    col = len (s2) + 1

    matrix = [[None] * col for i in range (0, row)]

    for i in range (0, row):
        for j in range (0, col):
            if i==0 or j==0:
                matrix[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max (matrix[i-1][j], matrix[i][j-1])
    
    return matrix[row-1][col-1]

print (longest_subsequence ("aggtab", "gxtxayb"))