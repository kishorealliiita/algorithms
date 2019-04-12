import os

def coin_sum_recur (arr, n, m):
    if m == 0:
        return 1
    
    if m < 0:
        return 0
    
    if n <= 0 and m >= 1:
        return 0

    return coin_sum_recur (arr, n-1, m) + coin_sum_recur (arr, n, m-arr[n-1])
    

arr = [1,2,3]

#print (coin_sum_recur (arr, 3, 4))


def coin_change_dp (arr, m):
    res = [0] * (m+1)

    res[0] = 1
    for i in range (0, len(arr)):
        for j in range (0, m+1):
            if arr[i]  <= j:
                res[j]  += res[j-arr[i]]
    
    return res[m]

print (coin_change_dp (arr, 4))