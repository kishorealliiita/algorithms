import os
import sys

def reverse_pairs (arr):
    n = len(arr)
    res = [0] * n
    if n==0:
        return -1
    
    if n==1:
        return -1

    res [n-1] = 0
    min_so_far = arr[n-1]

    #index.
    n = n-2

    while n>=0:
        if arr[n] > 2*min_so_far:
            res[n] = res [n+1] + 1
        else:
            res[n] = res [n+1]
        min_so_far = min (min_so_far, arr[n])
        n = n-1
    
    return res[0]

arr = [1,3,2,3,1]
arr1 = [2,4,3,5,1]

print (reverse_pairs (arr1))




    