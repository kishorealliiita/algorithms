import os

def longest_increasing_seq (arr):
    n = len(arr)

    res = [0]*n 

    res [0] = 1
    for i in range (1,n):
        res[i] = 1
        for j in range (0,i):
            if arr[i] > arr [j] and res[i] < res[j] + 1:
                res[i] = res[j] + 1
    
    return max(res)
    

arr = [10,20,30,10,50,30]

print (longest_increasing_seq (arr))