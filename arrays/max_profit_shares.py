import os

def max_profit (arr, k):
    if k < 1:
        return -1

    if len (arr) < 2:
        return -1

    n = 1
    total_profit = 0
    current_profit = 0
    min_so_far = arr[0]
    while k>=0 and n < len(arr):
        diff = arr[n] - min_so_far
        current_profit = max (diff, current_profit)

        if arr[n] < min_so_far:
            total_profit += current_profit
            current_profit = 0
            min_so_far = arr[n]
            k = k-1
        
        n = n+1
    
    #always add last current profit to total.
    total_profit += current_profit
    
    return total_profit

arr = [2,4,1]
arr1 = [3,2,6,5,0,3]

print (max_profit (arr1, 2))