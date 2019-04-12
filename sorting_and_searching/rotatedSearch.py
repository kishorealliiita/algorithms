import os

def rotate_search (arr, n):
    if len (arr) == 0:
        return -1
    
    pivot = findPivot (arr, 0, len(arr))
    print (pivot)

    if pivot == -1:
        return binary_search (arr, 0, len(arr), n)
    elif arr[pivot] == n:
        return pivot
    elif arr[pivot] < n and arr[0] > n:
        return binary_search (arr, pivot+1, len(arr), n)
    else:
        return binary_search (arr, 0, pivot,  n)

def binary_search (arr, low, high, n):
    if low > high:
        return -1
    mid = (low + high)//2

    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return binary_search (arr, low, mid, n)
    else:
        return binary_search (arr, mid+1, high, n)

def findPivot (arr, low, high):
    if low > high:
        return -1
    
    mid = (low+high)//2

    if arr[mid] > arr[mid+1]:
        return mid+1
    elif arr[mid-1] > arr[mid]:
        return mid
    elif arr[low] > arr[mid]:
        return findPivot (arr, low, mid)
    else:
        return findPivot (arr, mid+1, high)
    

arr = [4,5,1,2,3]

print (rotate_search (arr, 5))


