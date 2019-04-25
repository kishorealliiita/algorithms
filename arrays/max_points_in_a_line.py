import os

def get_slope (p1, p2):
    m = abs (p2[1] - p1[1])/abs (p2[0] - p1[0])
    return m

def max_points (arr):
    if not arr:
        return -1

    arr = sorted(arr)
    pm = dict()
    p1 = arr[0]
    horizontal_lines=0

    for i in range (1, len(arr)):
        if arr[i][0]-p1[0] == 0 and arr[i][1]-p1[1] != 0:
            horizontal_lines += 1
            continue
        
        m = get_slope (p1, arr[i])
        p1 = arr[i]
        if m not in pm:
            pm[m] = 2
        else:
            pm[m] += 1
    
    max_val = 0
    for k,v in pm.items():
        max_val = max (v, max_val)

    return max_val + horizontal_lines

arr = [[1,1], [2,2], [3,3]]
arr1 = [[1,1], [3,2], [5,3], [4,1], [2,3], [1,4]]

print (max_points (arr1))